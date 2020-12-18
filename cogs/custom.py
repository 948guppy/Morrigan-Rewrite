import textwrap
import asyncio
import discord
from discord.ext import commands

create_channel = [701432232090271794, 717249484161155102]


class StreamStatusIsNone(Exception):
    pass


class Custom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        channel_id = 758219068007776256
        channel = member.guild.get_channel(channel_id)

        async def create_custom_voice_channel(custom_type):
            category = self.bot.get_channel(705292043177558066)  # KYF用のカテゴリーチャンネル
            if custom_type == "SWF":
                category = self.bot.get_channel(705409529763856456)  # SWF用のカテゴリーチャンネル
            created_channel = await category.create_voice_channel(name=f'{custom_type}-{len(category.voice_channels)+1}')
            await member.move_to(created_channel)
            return created_channel

        async def send_custom_panel(custom_type):
            created_channel = await create_custom_voice_channel(custom_type)
            e = discord.Embed()
            e.title = f"{custom_type}が作成されました！"
            e.description = textwrap.dedent(
                f"""
                募集者 : {member.mention}さん
                """
            )
            e.set_footer(text=f'チャンネルID:{created_channel.id}')
            e.colour = 0x00ff7f
            await channel.send(embed=e)

        async def send_error_message(voice_channel_id):
            e = discord.Embed()
            e.title = "エラーが発生しました！"
            e.description = textwrap.dedent(
                f"""
                チャンネルID : {voice_channel_id}用のパネルが取得されませんでした。
                既にパネルが削除されているか、存在するパネル数が多すぎる可能性があります。
                このエラーは10秒後に削除されます。
                """
            )
            e.colour = 0xFF0000
            await channel.send(embed=e, delete_after=10)

        async def delete_custom_panel(voice_channel_id):

            custom_information = None

            async for message in channel.history(limit=200):
                try:
                    if message.embeds[0].title in ["SWFが作成されました！", "KYFが作成されました！"]:
                        if f"チャンネルID:{voice_channel_id}" in message.embeds[0].footer.text:
                            custom_information = message
                            break
                except IndexError:
                    continue

            try:
                await custom_information.delete()
            except AttributeError:
                await send_error_message(voice_channel_id)

        try:
            if after.channel.name in ["SWFを作成", "KYFを作成"]:
                channel_type = after.channel.name[0:3]
                await send_custom_panel(channel_type)
        except AttributeError:
            if before.channel.category.id == 705409529763856456 or before.channel.category.id == 705292043177558066:
                if len(before.channel.members) == 0:
                    await delete_custom_panel(before.channel.id)
                    await before.channel.delete()


def setup(bot):
    bot.add_cog(Custom(bot))
