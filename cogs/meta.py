from discord.ext import commands
from cogs.utils import checks, formats, time, context
from cogs.utils.paginator import Pages
import discord
from collections import OrderedDict, deque, Counter
import os
import datetime
import asyncio
import copy
import unicodedata
import inspect
import itertools
from typing import Union


class Prefix(commands.Converter):
    async def convert(self, ctx, argument):
        user_id = ctx.bot.user.id
        if argument.startswith((f'<@{user_id}>', f'<@!{user_id}>')):
            raise commands.BadArgument(
                'That is a reserved prefix already in use.')
        return argument


class FetchedUser(commands.Converter):
    async def convert(self, ctx, argument):
        if not argument.isdigit():
            raise commands.BadArgument('Not a valid user ID.')
        try:
            return await ctx.bot.fetch_user(argument)
        except discord.NotFound:
            raise commands.BadArgument('User not found.') from None
        except discord.HTTPException:
            raise commands.BadArgument(
                'An error occurred while fetching the user.') from None


class HelpPaginator(Pages):
    def __init__(self, help_command, ctx, entries, *, per_page=4):
        super().__init__(ctx, entries=entries, per_page=per_page)
        self.reaction_emojis.append(
            ('\N{WHITE QUESTION MARK ORNAMENT}', self.show_bot_help))
        self.total = len(entries)
        self.help_command = help_command
        self.prefix = help_command.clean_prefix
        self.is_bot = False

    def get_bot_page(self, page):
        cog, description, commands = self.entries[page - 1]
        self.title = f'{cog} Commands'
        self.description = description
        return commands

    def prepare_embed(self, entries, page, *, first=False):
        self.embed.clear_fields()
        self.embed.description = self.description
        self.embed.title = self.title

        self.embed.set_footer(
            text=f'"{self.prefix}help <command>" を使用すると、より詳細なヘルプを表示します')

        for entry in entries:
            signature = f'{entry.qualified_name} {entry.signature}'
            self.embed.add_field(
                name=signature, value=entry.short_doc or "No help given", inline=False)

        if self.maximum_pages:
            self.embed.set_author(
                name=f'Page {page}/{self.maximum_pages} ({self.total} commands)')

    async def show_help(self):
        """このメッセージを表示します"""

        self.embed.title = 'Paginator help'
        self.embed.description = 'ヘルプページへようこそ'

        messages = [f'{emoji} {func.__doc__}' for emoji,
                    func in self.reaction_emojis]
        self.embed.clear_fields()
        self.embed.add_field(name='これらのリアクションの意味',
                             value='\n'.join(messages), inline=False)

        self.embed.set_footer(
            text=f'このヘルプの前は {self.current_page} ページ目を参照していました')
        await self.message.edit(embed=self.embed)

        async def go_back_to_current_page():
            await asyncio.sleep(30.0)
            await self.show_current_page()

        self.bot.loop.create_task(go_back_to_current_page())

    async def show_bot_help(self):
        """このBotの使い方を表示します"""

        self.embed.title = 'Using the bot'
        self.embed.description = 'ヘルプページへようこそ'
        self.embed.clear_fields()

        entries = (
            ('<引数>', 'この引数が __**必須**__ であることを意味します'),
            ('[引数]', 'この引数が __**任意**__ であることを意味します'),
            ('[A|B]', ' __**A でも B でもよい**__ ことを意味します'),
            ('[引数...]', '複数の引数を持つことができますが\n'
             '__**括弧を入力してはいけません**__')
        )

        self.embed.add_field(name='このBotの使い方', value='このヘルプページの読み方は以下の通りです')

        for name, value in entries:
            self.embed.add_field(name=name, value=value, inline=False)

        self.embed.set_footer(
            text=f'このヘルプの前は {self.current_page} ページ目を参照していました')
        await self.message.edit(embed=self.embed)

        async def go_back_to_current_page():
            await asyncio.sleep(30.0)
            await self.show_current_page()

        self.bot.loop.create_task(go_back_to_current_page())


class PaginatedHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__(command_attrs={
            'cooldown': commands.Cooldown(1, 3.0, commands.BucketType.member),
            'help': 'ボット、コマンド、カテゴリに関するヘルプを表示します'
        })

    async def on_help_command_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(str(error.original))

    def get_command_signature(self, command):
        parent = command.full_parent_name
        if len(command.aliases) > 0:
            aliases = '|'.join(command.aliases)
            fmt = f'[{command.name}|{aliases}]'
            if parent:
                fmt = f'{parent} {fmt}'
            alias = fmt
        else:
            alias = command.name if not parent else f'{parent} {command.name}'
        return f'{alias} {command.signature}'

    async def send_bot_help(self, mapping):
        def key(c):
            return c.cog_name or '\u200bNo Category'

        bot = self.context.bot
        entries = await self.filter_commands(bot.commands, sort=True, key=key)
        nested_pages = []
        per_page = 9
        total = 0

        for cog, commands in itertools.groupby(entries, key=key):
            commands = sorted(commands, key=lambda c: c.name)
            if len(commands) == 0:
                continue

            total += len(commands)
            actual_cog = bot.get_cog(cog)
            # get the description if it exists (and the cog is valid) or return Empty embed.
            description = (
                actual_cog and actual_cog.description) or discord.Embed.Empty
            nested_pages.extend(
                (cog, description, commands[i:i + per_page]) for i in range(0, len(commands), per_page))

        # a value of 1 forces the pagination session
        pages = HelpPaginator(self, self.context, nested_pages, per_page=1)

        # swap the get_page implementation to work with our nested pages.
        pages.get_page = pages.get_bot_page
        pages.is_bot = True
        pages.total = total
        await pages.paginate()

    async def send_cog_help(self, cog):
        entries = await self.filter_commands(cog.get_commands(), sort=True)
        pages = HelpPaginator(self, self.context, entries)
        pages.title = f'{cog.qualified_name} Commands'
        pages.description = cog.description

        await pages.paginate()

    def common_command_formatting(self, page_or_embed, command):
        page_or_embed.title = self.get_command_signature(command)
        if command.description:
            page_or_embed.description = f'{command.description}\n\n{command.help}'
        else:
            page_or_embed.description = command.help or 'No help found...'

    async def send_command_help(self, command):
        # No pagination necessary for a single command.
        embed = discord.Embed(colour=discord.Colour.blurple())
        self.common_command_formatting(embed, command)
        await self.context.send(embed=embed)

    async def send_group_help(self, group):
        subcommands = group.commands
        if len(subcommands) == 0:
            return await self.send_command_help(group)

        entries = await self.filter_commands(subcommands, sort=True)
        pages = HelpPaginator(self, self.context, entries)
        self.common_command_formatting(pages, group)

        await pages.paginate()


class Meta(commands.Cog):
    """Discord や Bot 自体に関連する実用的なコマンド"""

    def __init__(self, bot):
        self.bot = bot
        self.old_help_command = bot.help_command
        bot.help_command = PaginatedHelpCommand()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self.old_help_command

    async def cog_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(error)

    @commands.command(name='quit', hidden=True)
    @commands.is_owner()
    async def _quit(self, ctx):
        """ボットを終了します"""
        await self.bot.logout()

    @commands.command()
    async def avatar(self, ctx, *, user: Union[discord.Member, FetchedUser] = None):
        """任意のユーザーのアバターを表示します"""
        embed = discord.Embed()
        user = user or ctx.author
        avatar = user.avatar_url_as(static_format='png')
        embed.set_author(name=str(user), url=avatar)
        embed.set_image(url=avatar)
        await ctx.send(embed=embed)

    @commands.command()
    async def info(self, ctx, *, user: Union[discord.Member, FetchedUser] = None):
        """任意のユーザーの情報を表示します"""

        user = user or ctx.author
        if ctx.guild and isinstance(user, discord.User):
            user = ctx.guild.get_member(user.id) or user

        e = discord.Embed()
        roles = [role.name.replace('@', '@\u200b')
                 for role in getattr(user, 'roles', [])]
        shared = sum(g.get_member(user.id)
                     is not None for g in self.bot.guilds)
        e.set_author(name=str(user))

        def format_date(dt):
            if dt is None:
                return 'N/A'
            return f'{dt:%Y-%m-%d %H:%M} ({time.human_timedelta(dt, accuracy=3)})'

        e.add_field(name='ユーザーID', value=user.id, inline=False)
        e.add_field(name='サーバー', value=f'{shared} つの共通のサーバー', inline=False)
        e.add_field(name='参加日', value=format_date(
            getattr(user, 'joined_at', None)), inline=False)
        e.add_field(name='アカウント作成日', value=format_date(
            user.created_at), inline=False)

        voice = getattr(user, 'voice', None)
        if voice is not None:
            vc = voice.channel
            other_people = len(vc.members) - 1
            voice = f'{vc.name} : {other_people} 人' if other_people else f'{vc.name} : １人のみ'
            e.add_field(name='ボイスチャンネル', value=voice, inline=False)

        if roles:
            e.add_field(name='役職', value=', '.join(roles) if len(
                roles) < 10 else f'{len(roles)} 個', inline=False)

        colour = user.colour
        if colour.value:
            e.colour = colour

        if user.avatar:
            e.set_thumbnail(url=user.avatar_url)

        if isinstance(user, discord.User):
            e.set_footer(text='このメンバーはこのサーバーにはいません')

        await ctx.send(embed=e)

    @commands.command(aliases=['guildinfo'], usage='')
    @commands.guild_only()
    async def serverinfo(self, ctx, *, guild_id: int = None):
        """任意のサーバーの情報を表示します"""

        if guild_id is not None and await self.bot.is_owner(ctx.author):
            guild = self.bot.get_guild(guild_id)
            if guild is None:
                return await ctx.send(f'無効なサーバーIDが渡されています')
        else:
            guild = ctx.guild

        roles = [role.name.replace('@', '@\u200b') for role in guild.roles]

        # we're going to duck type our way here
        class Secret:
            pass

        secret_member = Secret()
        secret_member.id = 0
        secret_member.roles = [guild.default_role]

        # figure out what channels are 'secret'
        secret = Counter()
        totals = Counter()
        for channel in guild.channels:
            perms = channel.permissions_for(secret_member)
            channel_type = type(channel)
            totals[channel_type] += 1
            if not perms.read_messages:
                secret[channel_type] += 1
            elif isinstance(channel, discord.VoiceChannel) and (not perms.connect or not perms.speak):
                secret[channel_type] += 1

        member_by_status = Counter(str(m.status) for m in guild.members)

        e = discord.Embed()
        e.title = guild.name
        e.add_field(name='サーバーID', value=guild.id)
        e.add_field(name='所有者', value=guild.owner)
        if guild.icon:
            e.set_thumbnail(url=guild.icon_url)

        channel_info = []
        key_to_emoji = {
            discord.TextChannel: '<:text_channel:586339098172850187>',
            discord.VoiceChannel: '<:voice_channel:586339098524909604>',
        }
        for key, total in totals.items():
            secrets = secret[key]
            try:
                emoji = key_to_emoji[key]
            except KeyError:
                continue

            if secrets:
                channel_info.append(f'{emoji} {total} ({secrets} locked)')
            else:
                channel_info.append(f'{emoji} {total}')

        info = []
        features = set(guild.features)
        all_features = {
            'PARTNERED': 'Partnered',
            'VERIFIED': 'Verified',
            'DISCOVERABLE': 'Server Discovery',
            'PUBLIC': 'Server Discovery/Public',
            'INVITE_SPLASH': 'Invite Splash',
            'VIP_REGIONS': 'VIP Voice Servers',
            'VANITY_URL': 'Vanity Invite',
            'MORE_EMOJI': 'More Emoji',
            'COMMERCE': 'Commerce',
            'LURKABLE': 'Lurkable',
            'NEWS': 'News Channels',
            'ANIMATED_ICON': 'Animated Icon',
            'BANNER': 'Banner'
        }

        for feature, label in all_features.items():
            if feature in features:
                info.append(f'{ctx.tick(True)}: {label}')

        if info:
            e.add_field(name='Features', value='\n'.join(info))

        e.add_field(name='チャンネル', value='\n'.join(channel_info))

        if guild.premium_tier != 0:
            boosts = f'レベル : {guild.premium_tier}\n{guild.premium_subscription_count} ブースト'
            last_boost = max(
                guild.members, key=lambda m: m.premium_since or guild.created_at)
            if last_boost.premium_since is not None:
                boosts = f'{boosts}\n最後のブースト: {last_boost} ({time.human_timedelta(last_boost.premium_since, accuracy=2)})'
            e.add_field(name='ブースト', value=boosts, inline=False)

        fmt = f'オンライン : {member_by_status["online"]} ' \
              f'退席中 : {member_by_status["idle"]} ' \
              f'取り込み中 : {member_by_status["dnd"]} ' \
              f'オフライン : {member_by_status["offline"]}\n' \
              f'合計 : {guild.member_count}'

        e.add_field(name='メンバー', value=fmt, inline=False)

        # requires max-concurrency d.py check to work though.

        e.add_field(name='権限', value=', '.join(roles)
                    if len(roles) < 10 else f'{len(roles)} 個')
        e.set_footer(text='作成日').timestamp = guild.created_at
        await ctx.send(embed=e)

    async def say_permissions(self, ctx, member, channel):
        permissions = channel.permissions_for(member)
        e = discord.Embed(colour=member.colour)
        avatar = member.avatar_url_as(static_format='png')
        e.set_author(name=str(member), url=avatar)
        allowed, denied = [], []
        for name, value in permissions:
            name = name.replace('_', ' ').replace('guild', 'server').title()
            if value:
                allowed.append(name)
            else:
                denied.append(name)

        e.add_field(name='Allowed', value='\n'.join(allowed))
        e.add_field(name='Denied', value='\n'.join(denied))
        await ctx.send(embed=e)

    @commands.command(rest_is_raw=True, hidden=True)
    @commands.is_owner()
    async def echo(self, ctx, *, content):
        await ctx.send(content)

    @commands.cooldown(rate=1, per=60, type=commands.BucketType.guild)
    @commands.command(aliases=['countdown'], usage='')
    async def cud(self, ctx, count: int = None):
        """カウントダウンをします"""

        if count is None:
            count = 3
        elif count:
            if count >= 61:
                await ctx.send("カウントの時間が長すぎます")
                return
        for i in range(count):
            await ctx.send(count - i)
            await asyncio.sleep(1)

        await ctx.send('スタート')

    @commands.has_permissions(administrator=True)
    @commands.command(aliases=['deletechat'], usage='')
    async def dlchat(self, ctx, count: int = None):
        """メッセージを一括削除します"""

        if count is None:
            await ctx.channel.purge()
        elif count:
            count = count + 1
            await ctx.channel.purge(limit=count)


def setup(bot):
    bot.add_cog(Meta(bot))
