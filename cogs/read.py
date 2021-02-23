import textwrap
import asyncio
import os
import subprocess
import ffmpeg
from cogs.utils.voice_generator import creat_WAV
import discord
from discord.ext import commands


class StreamStatusIsNone(Exception):
    pass


class Read(commands.Cog):
    def __init__(self, bot):
        self.voice_client = None
        self.bot = bot

    @commands.command()
    async def join(self, ctx):
        print('#voicechannelを取得')
        vc = ctx.author.voice.channel
        print('#voicechannelに接続')
        await vc.connect()

    @commands.command()
    async def bye(self, ctx):
        print('#切断')
        await ctx.voice_client.disconnect()

    @commands.command()
    async def on_message(self, message):
        msgclient = message.guild.voice_client
        if message.content.startswith('.'):
            pass

        else:
            if message.guild.voice_client:
                print(message.content)
                creat_WAV(message.content)
                source = discord.FFmpegPCMAudio("output.wav")
                message.guild.voice_client.play(source)
            else:
                pass
        await self.bot.process_commands(message)


def setup(bot):
    bot.add_cog(Read(bot))
