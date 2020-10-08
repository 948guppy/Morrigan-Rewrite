import discord
from discord.ext import commands
import asyncio
import textwrap
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), 'JST')


class Thread(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tmake(self, ctx):
        category = self.bot.get_channel(732925079335469118)

        async def send_first_message(message):
            e = discord.Embed()
            e.title = "スレッド作成状況"
            e.description = textwrap.dedent(
                """
                スレッドの名前を入力してください。
                """
            )
            e.set_footer(
                text=f"ステータス : 名前を入力中...",
                icon_url=message.guild.icon_url
            )
            e.colour = 0x00ff7f
            embed = await message.channel.send(embed=e)
            return embed

        async def send_second_message(message):
            e = discord.Embed()
            e.title = "スレッド作成状況"
            e.description = textwrap.dedent(
                """
                スレッドのトピックを入力してください。
                """
            )
            e.set_footer(
                text=f"ステータス : 名前を入力中...",
                icon_url=ctx.guild.icon_url
            )
            e.colour = 0x00ff7f
            embed = await message.send(embed=e)
            return embed

        async def send_description(thread, about):
            e = discord.Embed()
            e.description = about
            await thread.send(embed=e)

        async def send_complete_message(message, thread):
            e = discord.Embed()
            e.title = "📒 作成しました"
            e.description = textwrap.dedent(
                f"""
                チャンネル名 : {thread.name}
                チャンネル作成先へ：{thread.mention}
                作成時間：{str(datetime.now(JST))[:16]}
                """
            )
            e.colour = 0x00ff7f
            thread = await message.send(embed=e, delete_after=360)
            return thread

        def check(m):
            return m.author == ctx.author

        delete = []

        # 関数の実行
        try:
            delete.append(await send_first_message(ctx))
            name = await self.bot.wait_for('message', timeout=60.0, check=check)
            delete.append(name)
        except asyncio.TimeoutError:
            delete.append(await ctx.send('タイムアウトしました'))
        else:
            try:
                delete.append(await send_second_message(ctx))
                description = await self.bot.wait_for('message', timeout=60.0, check=check)
                delete.append(description)
            except asyncio.TimeoutError:
                delete.append(await ctx.send('タイムアウトしました'))
            else:
                channel = await category.create_text_channel(name=name.content, topic=description.content)
                await send_complete_message(ctx, channel)
                await send_description(channel, description.content)
        await asyncio.sleep(5)
        await ctx.message.delete()
        await ctx.channel.delete_messages(delete)


def setup(bot):
    bot.add_cog(Thread(bot))
