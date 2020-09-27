import textwrap
import discord
from discord.ext import commands


class Stream(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        channel_id = 758219068007776256
        channel = member.guild.get_channel(channel_id)

        # 配信作成時の関数
        def overwrites(streamer):
            overwrite = {
                streamer.guild.default_role: discord.PermissionOverwrite(create_instant_invite=False,
                                                                         manage_channels=False,
                                                                         manage_permissions=False, manage_roles=False,
                                                                         manage_webhooks=False, read_messages=False,
                                                                         send_messages=False, send_tts_messages=False,
                                                                         manage_messages=False, embed_links=False,
                                                                         attach_files=False, read_message_history=False,
                                                                         mention_everyone=False, external_emojis=False,
                                                                         use_external_emojis=False, add_reactions=False,
                                                                         view_channel=True, connect=True, speak=True,
                                                                         stream=True, mute_members=False,
                                                                         deafen_members=False, move_members=False,
                                                                         use_voice_activation=True,
                                                                         priority_speaker=False),
                streamer: discord.PermissionOverwrite(create_instant_invite=False, manage_channels=False,
                                                      manage_permissions=False, manage_roles=False,
                                                      manage_webhooks=False, read_messages=False, send_messages=False,
                                                      send_tts_messages=False, manage_messages=False, embed_links=False,
                                                      attach_files=False, read_message_history=False,
                                                      mention_everyone=False, external_emojis=False,
                                                      use_external_emojis=False, add_reactions=False, view_channel=True,
                                                      connect=True, speak=True, stream=True, mute_members=True,
                                                      deafen_members=True, move_members=False,
                                                      use_voice_activation=True, priority_speaker=True)
            }
            return overwrite

        async def create_stream_channel(streamer):
            category_id = 733625569178157076
            category = streamer.guild.get_channel(category_id)
            stream = await category.create_voice_channel(name=f"{streamer.display_name}",
                                                         overwrites=overwrites(streamer))
            await streamer.move_to(stream)

        def get_streaming_game(streamer):
            try:
                game = streamer.activities[0]
            except IndexError:
                game = None
            return game

        async def send_stream_started(streamer):
            e = discord.Embed()
            e.title = "配信が開始されました！"
            e.description = textwrap.dedent(
                f"""
                配信者 : {streamer.mention}さん
                配信中のゲーム : {get_streaming_game(streamer).name if get_streaming_game(streamer) else '取得されませんでした'}
                """
            )
            e.colour = 0x99FFFF
            await channel.send(embed=e)

        async def send_error_message(streamer):
            e = discord.Embed()
            e.title = "エラーが発生しました！"
            e.description = textwrap.dedent(
                f"""
                配信者 : {streamer.mention}さんによる配信情報パネルの取得ができませんでした。
                既にパネルが削除されているか、存在するパネル数が多すぎる可能性があります。
                このエラーは10秒後に削除されます。
                """
            )
            e.colour = 0xFF0000
            await channel.send(embed=e, delete_after=10)

        async def delete_stream_information(streamer):

            stream_information = None

            async for message in channel.history(limit=200):
                try:
                    if message.embeds[0].title == "配信が開始されました！":
                        if f"配信者 : {streamer.mention}さん" in message.embeds[0].description:
                            stream_information = message
                            break
                except IndexError:
                    continue

            try:
                await stream_information.delete()
            except AttributeError:
                await send_error_message(streamer)

        # 配信終了時の関数
        async def close_stream(listener, stream):
            try:
                if stream.channel.overwrites_for(listener).deafen_members:
                    await stream.channel.delete()
                    await delete_stream_information(member)
            except AttributeError:
                pass

        # 処理の実行
        try:
            if after.channel.id == 733626787992567868:
                await send_stream_started(member)
                await create_stream_channel(member)
        except AttributeError:
            if not before.channel.id == 733626787992567868 and before.channel.category_id == 733625569178157076:
                await close_stream(member, before)

    @commands.command()
    async def change_stream_name(self, ctx, name: str):

        async def change_streaming_channel(listener, stream_name):
            state = listener.author.voice

            if state is None:
                await listener.channel.send("VCにいません")
            else:
                if state.channel.category_id == 733625569178157076 and not state.channel.id == 733626787992567868:
                    stream_channel_id = state.channel.id
                    stream_channel = listener.guild.get_channel(stream_channel_id)
                    await stream_channel.edit(name=stream_name)

        await change_streaming_channel(ctx, name)


def setup(bot):
    bot.add_cog(Stream(bot))
