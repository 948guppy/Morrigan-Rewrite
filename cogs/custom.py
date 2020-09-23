import discord
from discord.ext import commands
import textwrap


class Custom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        channel_id = 758219068007776256
        channel = member.guild.get_channel(channel_id)

        # プレイヤー環境チェック用関数
        def check_player_role(participant):
            player_environ = None
            for role in participant.roles:
                if "版" in str(role):
                    player_environ = role
            for role in participant.roles:
                if "クロスプレイON" in str(role):
                    return player_environ, True
            return player_environ, False

        # VC用チャンネル名指定用関数
        def to_name_channel(channel_type: str):
            if channel_type == "SWF":
                category = self.bot.get_channel(705409529763856456)
                channel_name = f"SWF {len(category.voice_channels)}"
            else:
                category = self.bot.get_channel(705292043177558066)
                channel_name = f"KYF {len(category.voice_channels)}"
            return channel_name

        # VC用役職作成関数
        async def create_custom_role(participates, custom_type: str):
            per = discord.Permissions(permissions=36700160)
            new_role = await participates.guild.create_role(name=to_name_channel(custom_type), permissions=per)
            await participates.add_roles(new_role)
            return new_role

        # VC用権限作成関数
        def channel_overwrites(participates, play_role, new_role, cross_play: bool):
            overwrites = {
                participates.guild.default_role: discord.PermissionOverwrite(create_instant_invite=False,
                                                                             manage_channels=False,
                                                                             manage_permissions=False,
                                                                             manage_roles=False, manage_webhooks=False,
                                                                             read_messages=False, send_messages=False,
                                                                             send_tts_messages=False,
                                                                             manage_messages=False, embed_links=False,
                                                                             attach_files=False,
                                                                             read_message_history=False,
                                                                             mention_everyone=False,
                                                                             external_emojis=False,
                                                                             use_external_emojis=False,
                                                                             add_reactions=False, view_channel=False,
                                                                             connect=False, speak=False, stream=False,
                                                                             mute_members=False, deafen_members=False,
                                                                             move_members=False,
                                                                             use_voice_activation=False,
                                                                             priority_speaker=False),
                participates.guild.me: discord.PermissionOverwrite(create_instant_invite=False, manage_channels=True,
                                                                   manage_permissions=True, manage_roles=True,
                                                                   manage_webhooks=False, read_messages=True,
                                                                   send_messages=True, send_tts_messages=False,
                                                                   manage_messages=True, embed_links=True,
                                                                   attach_files=True, read_message_history=True,
                                                                   mention_everyone=True, external_emojis=True,
                                                                   use_external_emojis=True, add_reactions=True,
                                                                   view_channel=True, connect=True, speak=True,
                                                                   stream=False, mute_members=True, deafen_members=True,
                                                                   move_members=True, use_voice_activation=True,
                                                                   priority_speaker=False),
                play_role: discord.PermissionOverwrite(create_instant_invite=False, manage_channels=False,
                                                       manage_permissions=False, manage_roles=False,
                                                       manage_webhooks=False, read_messages=True, send_messages=False,
                                                       send_tts_messages=False, manage_messages=False,
                                                       embed_links=False, attach_files=False, read_message_history=True,
                                                       mention_everyone=False, external_emojis=False,
                                                       use_external_emojis=False, add_reactions=False,
                                                       view_channel=True, connect=False, speak=False, stream=False,
                                                       mute_members=False, deafen_members=False, move_members=False,
                                                       use_voice_activation=False, priority_speaker=False),
                new_role: discord.PermissionOverwrite(create_instant_invite=False, manage_channels=False,
                                                      manage_permissions=False, manage_roles=False,
                                                      manage_webhooks=False, read_messages=True, send_messages=True,
                                                      send_tts_messages=False, manage_messages=False, embed_links=True,
                                                      attach_files=True,
                                                      read_message_history=True, mention_everyone=False,
                                                      external_emojis=True, use_external_emojis=True,
                                                      add_reactions=True, view_channel=True, connect=True, speak=True,
                                                      stream=True, mute_members=False, deafen_members=False,
                                                      move_members=False, use_voice_activation=True,
                                                      priority_speaker=False)
            }
            if cross_play:
                cross_play_role = participates.guild.get_role(758261798792462346)
                overwrites[cross_play_role] = discord.PermissionOverwrite(create_instant_invite=False,
                                                                          manage_channels=False,
                                                                          manage_permissions=False, manage_roles=False,
                                                                          manage_webhooks=False, read_messages=True,
                                                                          send_messages=False, send_tts_messages=False,
                                                                          manage_messages=False, embed_links=False,
                                                                          attach_files=False, read_message_history=True,
                                                                          mention_everyone=False, external_emojis=False,
                                                                          use_external_emojis=False,
                                                                          add_reactions=False, view_channel=True,
                                                                          connect=False, speak=False, stream=False,
                                                                          mute_members=False, deafen_members=False,
                                                                          move_members=False, use_voice_activation=True,
                                                                          priority_speaker=False)
            return overwrites

        # VC作成用関数
        async def create_custom_channel(custom_category, custom_type: str, participate, environ_role, custom_role,
                                        cross_play: bool):
            limit = None
            if custom_type == "SWF":
                limit = 4
            new_text_channel = await custom_category.create_text_channel(name=to_name_channel(custom_type),
                                                                         overwrites=channel_overwrites(participate,
                                                                                                       environ_role,
                                                                                                       custom_role,
                                                                                                       cross_play))
            new_voice_channel = await custom_category.create_voice_channel(name=to_name_channel(custom_type),
                                                                           overwrites=channel_overwrites(participate,
                                                                                                         environ_role,
                                                                                                         custom_role,
                                                                                                         cross_play),
                                                                           user_limit=limit)
            fmt = textwrap.dedent(
                f"""
                {new_text_channel.mention}を作成しました。
                このチャンネルは専用VCが0人になると自動で削除されます。

                この機能をOFFにするには'''m/auto_delete'''コマンドを使用してください。
                """
            )
            e = discord.Embed(
                description=fmt
            )
            await participate.move_to(new_voice_channel)
            await new_text_channel.send(embed=e)
            await send_custom_started(custom_type, participate)

        # アナウンス用関数
        async def send_custom_started(custom_type, participate):
            e = discord.Embed()
            e.title = f"{custom_type}が作成されました！"
            e.description = textwrap.dedent(
                """
                誰でも歓迎！
                """
            )
            e.add_field(name="募集者", value=f"{participate.mention}さん")
            e.colour = 0x99FFFF
            await channel.send(embed=e)

        async def send_error_message(streamer):
            e = discord.Embed()
            e.title = "エラーが発生しました！"
            e.description = textwrap.dedent(
                f"""
                募集者 : {streamer.mention}さんによる募集情報パネルの取得ができませんでした。
                既にパネルが削除されているか、存在するパネル数が多すぎる可能性があります。
                このエラーは10秒後に削除されます。
                """
            )
            e.colour = 0xFF0000
            await channel.send(embed=e, delete_after=10)

        async def delete_custom_information(participate):

            information = None

            async for message in channel.history(limit=200):
                try:
                    if "が作成されました！" in message.embeds[0].title:
                        information = message
                except IndexError:
                    continue

            try:
                await information.delete()
            except AttributeError:
                await send_error_message(participate)

        # 最適VC検索用関数
        def check_channel(channel_type, participate, role):
            if channel_type == "SWF":
                custom_category = self.bot.get_channel(705409529763856456)
            else:
                custom_category = self.bot.get_channel(705292043177558066)
            for custom_channel in custom_category.voice_channels:
                voice_channel = participate.guild.get_channel(custom_channel.id)
                if voice_channel.overwrites_for(role).view_channel:
                    return voice_channel
            return False

        # VC削除用関数
        async def delete_text_channel(participate, role):
            for custom_channel in participate.guild.text_channels:
                if custom_channel.overwrites_for(role).view_channel:
                    await custom_channel.delete()

        def search_role(participate, custom_channel):
            for role in participate.guild.roles:
                if not "版" in str(role):
                    if custom_channel.overwrites_for(role).view_channel:
                        return role

        # 関数の実行
        try:
            play_role = check_player_role(member)[0]
            if after.channel.name == "SWFに参加":
                category = member.guild.get_channel(705409529763856456)
                if not check_channel("SWF", member, play_role):
                    if check_player_role(member)[0]:
                        await create_custom_channel(category, "SWF", member, check_player_role(member)[0],
                                                    await create_custom_role(member, "SWF"),
                                                    check_player_role(member)[1])
            if after.channel.name == "KYFに参加":
                category = member.guild.get_channel(705292043177558066)
                if not check_channel("SWF", member, play_role):
                    if check_player_role(member)[0]:
                        await create_custom_channel(category, "KYF", member, check_player_role(member)[0],
                                                    await create_custom_role(member, "KYF"),
                                                    check_player_role(member)[1])
        except AttributeError:
            if before.channel.category.id == 705409529763856456 or before.channel.category.id == 705292043177558066:
                if len(before.channel.members) == 0:
                    await delete_custom_information(member)
                    await delete_text_channel(member, search_role(member, before.channel))
                    await search_role(member, before.channel).delete()
                    await before.channel.delete()


def setup(bot):
    bot.add_cog(Custom(bot))
