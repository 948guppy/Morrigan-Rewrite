import asyncio

import discord
from discord.ext import commands
import random
import textwrap
from cogs.utils.perks import Survivor, Killer , Killers


class RandomPerk(commands.Cog):
    """ランダムパーク関連コマンド"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = self.bot.get_channel(payload.channel_id)
        guild = self.bot.get_guild(payload.guild_id)
        message = await channel.fetch_message(payload.message_id)
        member = guild.get_member(payload.user_id)
        delete = []

        async def send_survivor_embed(PERK):
            e = discord.Embed()
            e.title = "今回の生存者のパークはこちら！"
            e.description = textwrap.dedent(
                f"""
                1⃣{PERK[0]}
                2⃣{PERK[1]}
                3⃣{PERK[2]}
                4⃣{PERK[3]}
                """
            )
            e.colour = 0x99FFFF
            if guild.icon:
                e.set_thumbnail(url=guild.icon_url)
            delete.append(await channel.send(embed=e))

        async def send_killer_embed(PERK):
            e = discord.Embed()
            e.title = "今回の殺人鬼のパークはこちら！"
            e.description = textwrap.dedent(
                f"""
                1⃣{PERK[0]}
                2⃣{PERK[1]}
                3⃣{PERK[2]}
                4⃣{PERK[3]}
                """
            )
            e.colour = 0x99FFFF
            if guild.icon:
                e.set_thumbnail(url=guild.icon_url)
            delete.append(await channel.send(embed=e))

        async def send_killers_embed(KILLER):
            e = discord.Embed()
            e.title = "今回の殺人鬼はこちら！"
            e.add_field(
                name="殺人鬼",
                value=f"{KILLER[0]}"
            )
            e.colour = 0x99FFFF
            if guild.icon:
                e.set_thumbnail(url=guild.icon_url)
            delete.append(await channel.send(embed=e))

        if message.embeds[0].title == "ランダムDBD":
            if str(payload.emoji) == "1⃣":
                perks = random.sample(list(Survivor.survivor_perks), 4)
                await send_survivor_embed(perks)
            if str(payload.emoji) == "2⃣":
                perks = random.sample(list(Killer.killer_perks), 4)
                await send_killer_embed(perks)
            if str(payload.emoji) == "3⃣":
                killer = random.sample(list(Killers.Killers), 1)
                await send_killers_embed(killer)
        await (await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)).remove_reaction(
            payload.emoji, self.bot.get_guild(payload.guild_id).get_member(payload.user_id))
        await asyncio.sleep(60)
        await channel.delete_messages(delete)


def setup(bot):
    bot.add_cog(RandomPerk(bot))
