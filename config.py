import os


class DiscordBot:
    token = os.environ["DISCORD_BOT_MORRIGAN_TOKEN"]
    cogs = [
        "cogs.admin",
        "cogs.meta"
    ]
