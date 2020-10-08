import os


class DiscordBot:
    token = os.environ["TOKEN"]
    cogs = [
        "cogs.admin",
        "cogs.custom",
        "cogs.meta",
        "cogs.stream",
        "cogs.thread",
        "cogs.twitter"
    ]


class Twitter:
    CONSUMER_KEY = os.environ['CONSUMER_KEY']
    CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
