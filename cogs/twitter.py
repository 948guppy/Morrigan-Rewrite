import re
import sys

import discord
import tweepy
from discord.ext import commands, tasks

sys.path.append('../')
from config import Twitter

CONSUMER_KEY = Twitter.CONSUMER_KEY
CONSUMER_SECRET = Twitter.CONSUMER_SECRET
ACCESS_TOKEN = Twitter.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = Twitter.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"


class TwitterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.get_tweet.start()

    @tasks.loop(seconds=480)
    async def get_tweet(self):

        def search_optimal_channel(tweet_data):
            tweet_context = tweet_data.full_text
            announce_channel = 702513437535895553
            channels = {
                "毎週水曜日はシュライン・オブ・シークレットの更新日！": 702513375917113475,
                "アップデート": 702513333483339856,
                "#新スキン": 702517983813173368,
                "セール情報": 703107555295100980,
                "#DbDアート": 702518338336849940,
            }
            for key in channels.keys():
                if key in tweet_context:
                    announce_channel = channels[key]
            return announce_channel

        async def check_tweet_already_send(optimal_channel, tweet_data):
            url_list = re.findall(pattern, tweet_data.full_text)
            full_text = tweet_data.full_text
            try:
                if not tweet_data.full_text.replace(url_list[-1], '') == "":
                    full_text = tweet_data.full_text.replace(url_list[-1], '')
            except IndexError:
                pass
            async for message in optimal_channel.history(limit=500):
                try:
                    if message.embeds[0].description in full_text:
                        print('> 送信しませんでした')
                        return False
                except AttributeError and IndexError:
                    continue
            print('> 送信しました')
            return True

        async def send_tweet_embed(optimal_channel, tweet_data):
            url_list = re.findall(pattern, tweet_data.full_text)
            e = discord.Embed()
            e.description = tweet_data.full_text
            try:
                if not tweet_data.full_text.replace(url_list[-1], '') == "":
                    e.description = tweet_data.full_text.replace(url_list[-1], '')
            except IndexError:
                pass
            e.colour = 0x7fffd4
            e.set_author(
                name=tweet_data.user.name,
                url=f"https://twitter.com/{tweet_data.user.screen_name}?s=20",
                icon_url=api.get_user(tweet_data.user.id).profile_image_url_https
            )
            try:
                e.set_image(url=tweet_data.extended_entities['media'][0]['media_url'])
            except:
                pass
            await optimal_channel.send(embed=e)

        for tweet in reversed(api.user_timeline(id='DeadbyBHVR_JP', tweet_mode='extended')[0:5]):
            print(tweet.full_text)
            channel = self.bot.get_channel(search_optimal_channel(tweet))
            if await check_tweet_already_send(channel, tweet):
                await send_tweet_embed(channel, tweet)
            print('---------------------')


def setup(bot):
    bot.add_cog(TwitterCog(bot))
