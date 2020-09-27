import discord
from discord.ext import commands
import asyncio
import textwrap


class Custom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        """SWF/KYF機能のコマンド"""

        channel_id = 758219068007776256
        information_channel = member.guild.get_channel(channel_id)

        # プレイヤー環境取得用関数
        def get_player_environ(participate):
            for role in participate.roles:
                if "版" in str(role):
                    return participate.guild.get_role(role.id)
            return False

        # 最適なVCを検索する関数
        def search_optimal_channel(channel_type, participate, role):
            category = None
            if channel_type == "SWF":
                category = self.bot.get_channel(705409529763856456)
            if channel_type == "KYF":
                category = self.bot.get_channel(705292043177558066)
            for channel in category.voice_channels:
                optimal_channel = participate.guild.get_channel(channel.id)
                if optimal_channel.overwrites_for(role).view_channel:
                    return optimal_channel
            return False

        # 専用ロールの作成
        async def create_dedicated_role(participate):
            per = discord.Permissions(permissions=36700160)
            new_role = await participate.guild.create_role(name=to_name_channel("SWF")[1], permissions=per)
            await participate.add_roles(new_role)
            await new_role.edit(position=9)
            return new_role

        # 専用チャンネルの作成
        async def create_dedicated_channel(participate, custom_type):
            new_text_channel = await to_name_channel(custom_type)[0].create_text_channel(
                name=to_name_channel(custom_type)[1],
                overwrites=channel_overwrites(participate, player_environ_role, custom_role))
            new_voice_channel = await to_name_channel(custom_type)[0].create_voice_channel(
                name=to_name_channel(custom_type)[1],
                overwrites=channel_overwrites(participate, player_environ_role, custom_role))
            await new_channel_send_message(new_text_channel)
            await participate.move_to(new_voice_channel)

        def set_role(participate, channel):
            for role in participate.guild.roles:
                if not "版" in str(role):
                    if channel.overwrites_for(role).view_channel:
                        return role

        def to_name_channel(channel_type):
            category = None
            channel_name = None
            if channel_type == "SWF":
                category = self.bot.get_channel(705409529763856456)
                channel_name = f"SWF {len(category.voice_channels)}"
            if channel_type == "KYF":
                category = self.bot.get_channel(705292043177558066)
                channel_name = f"KYF {len(category.voice_channels)}"
            return category, channel_name

        def channel_overwrites(participate, player_environ, custom_role):
            overwrites = {
                participate.guild.default_role: discord.PermissionOverwrite(create_instant_invite=False,
                                                                            manage_channels=False,
                                                                            manage_permissions=False,
                                                                            manage_roles=False, manage_webhooks=False,
                                                                            read_messages=False, send_messages=False,
                                                                            send_tts_messages=False,
                                                                            manage_messages=False,
                                                                            embed_links=False, attach_files=False,
                                                                            read_message_history=False,
                                                                            mention_everyone=False,
                                                                            external_emojis=False,
                                                                            use_external_emojis=False,
                                                                            add_reactions=False,
                                                                            view_channel=False, connect=False,
                                                                            speak=False,
                                                                            stream=False, mute_members=False,
                                                                            deafen_members=False, move_members=False,
                                                                            use_voice_activation=False,
                                                                            priority_speaker=False),
                participate.guild.me: discord.PermissionOverwrite(create_instant_invite=False, manage_channels=True,
                                                                  manage_permissions=True, manage_roles=True,
                                                                  manage_webhooks=False, read_messages=True,
                                                                  send_messages=True, send_tts_messages=False,
                                                                  manage_messages=True, embed_links=True,
                                                                  attach_files=True,
                                                                  read_message_history=True, mention_everyone=True,
                                                                  external_emojis=True, use_external_emojis=True,
                                                                  add_reactions=True, view_channel=True, connect=True,
                                                                  speak=True, stream=False, mute_members=True,
                                                                  deafen_members=True, move_members=True,
                                                                  use_voice_activation=True, priority_speaker=False),
                player_environ: discord.PermissionOverwrite(create_instant_invite=False, manage_channels=False,
                                                            manage_permissions=False, manage_roles=False,
                                                            manage_webhooks=False, read_messages=True,
                                                            send_messages=False,
                                                            send_tts_messages=False, manage_messages=False,
                                                            embed_links=False, attach_files=False,
                                                            read_message_history=True,
                                                            mention_everyone=False, external_emojis=False,
                                                            use_external_emojis=False, add_reactions=False,
                                                            view_channel=True, connect=False, speak=False, stream=False,
                                                            mute_members=False, deafen_members=False,
                                                            move_members=False,
                                                            use_voice_activation=False, priority_speaker=False),
                custom_role: discord.PermissionOverwrite(create_instant_invite=False, manage_channels=False,
                                                         manage_permissions=False, manage_roles=False,
                                                         manage_webhooks=False, read_messages=True, send_messages=True,
                                                         send_tts_messages=False, manage_messages=False,
                                                         embed_links=True,
                                                         attach_files=True,
                                                         read_message_history=True, mention_everyone=False,
                                                         external_emojis=True, use_external_emojis=True,
                                                         add_reactions=True, view_channel=True, connect=True,
                                                         speak=True,
                                                         stream=True, mute_members=False, deafen_members=False,
                                                         move_members=False, use_voice_activation=True,
                                                         priority_speaker=False)
            }
            return overwrites

        # 以下VC削除用関数
        def search_role(participate, channel):
            for role in participate.guild.roles:
                if not "版" in str(role):
                    if channel.overwrites_for(role).view_channel:
                        return role

        def delete_text_channel(participate, role):
            for channel in participate.guild.text_channels:
                if channel.overwrites_for(role).view_channel:
                    return channel

        def auto_delete_channel(participate, voice_channel):
            role = participate.guild.get_role(717209621965832285)
            if voice_channel.overwrites_for(role).view_channel:
                return False
            return True

        async def new_channel_send_message(channel):
            e = discord.Embed()
            e.description = textwrap.dedent(
                f"""
                {channel.mention}を作成しました
                このチャンネルは専用VCが0人になると自動で削除されます
                この機能をOFFにするには'''m/auto_delete'''コマンドを使用してください
                """
            )
            await channel.send(embed=e)

        async def send_information(custom_type):
            e = discord.Embed()
            e.title = f"{custom_type}が作成されました！"
            e.description = textwrap.dedent(
                f"""
                コメント : 誰でもどうぞ！
                """
            )
            e.colour = 0x99FFFF
            await information_channel.send(embed=e)

        try:
            if after.channel.name == "SWFに参加":
                if get_player_environ(member) is False:
                    await member.move_to(None)
                else:
                    channel_type = "SWF"
                    player_environ_role = get_player_environ(member)
                    if search_optimal_channel("SWF", member, player_environ_role) is False:
                        custom_role = await create_dedicated_role(member)
                        await create_dedicated_channel(member, channel_type)
                        await send_information(channel_type)
                    else:
                        await member.add_roles(
                            set_role(member, search_optimal_channel("SWF", member, player_environ_role)))
                        await member.move_to(search_optimal_channel("SWF", member, player_environ_role))
            if after.channel.name == "KYFに参加":
                if get_player_environ(member) is False:
                    await member.move_to(None)
                else:
                    channel_type = "KYF"
                    player_environ_role = get_player_environ(member)
                    if search_optimal_channel("KYF", member, player_environ_role) is False:
                        custom_role = await create_dedicated_role(member)
                        await create_dedicated_channel(member, channel_type)
                        await send_information(channel_type)
                    else:
                        await member.add_roles(
                            set_role(member, search_optimal_channel("KYF", member, player_environ_role)))
                        await member.move_to(search_optimal_channel("KYF", member, player_environ_role))
        except AttributeError:
            if before.channel.category.id == 705409529763856456 or before.channel.category.id == 705292043177558066:
                if len(before.channel.members) == 0:
                    if auto_delete_channel(member, before.channel):
                        await delete_text_channel(member, search_role(member, before.channel)).delete()
                        await search_role(member, before.channel).delete()
                        await before.channel.delete()


def setup(bot):
    bot.add_cog(Custom(bot))
