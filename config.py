import os


class DiscordBot:
    token = os.environ["TOKEN"]
    cogs = [
        "cogs.admin",
        "cogs.custom",
        "cogs.meta",
        "cogs.stream"
    ]
