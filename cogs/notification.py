import asyncio
import textwrap
import discord
from discord.ext import commands


channel_id = 701431057370710076
intro_channel_id = 717283421101096993


class Notification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):

        async def send_embed():
            channel = member.guild.get_channel(channel_id)
            intro_channel = member.guild.get_channel(intro_channel_id)
            e = discord.Embed()
            e.title = "サーバー参加へのありがとうございます！"
            e.description = textwrap.dedent(
                f"""
                サーバー新規参加者 : {member.mention}さん
                自己紹介場所 : {intro_channel.mention}
                配信・募集は遠慮なくご参加ください！募集や配信も賑やかになるので遠慮なく！
                """
            )
            e.colour = 0x00ff7f
            await channel.send(embed=e)

        await send_embed()


def setup(bot):
    bot.add_cog(Notification(bot))
