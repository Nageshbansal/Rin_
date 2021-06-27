import os
import discord
from discord.ext import commands
import requests
import json
from dotenv import load_dotenv
import praw

import random

client = discord.Client()

load_dotenv()

reddit = praw.Reddit(
    client_id="fyc_h45Ag_gKeA",
    client_secret="tLlpV_AgBYdKgdXcm9sReKuoCg60QQ",
    user_agent="levi",
    username='HelicopterRelevant95',
    password='vb9416615528',
    check_for_async=False,
)


class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.msg_list = []
        self.ctx = "x"

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        if payload.member.bot:
            return False
        else:
            if payload.emoji.name == "▶" and payload.message_id in self.msg_list:
                print(payload.message_id)
                return self.meme

            elif payload.emoji.name == "◀" and payload.message_id in self.msg_list:
                return "backward"

            else:
                pass

    @commands.command()
    async def meme(self,ctx, subredit="memes"):
        self.ctx = ctx
        subreddit = reddit.subreddit(subredit)
        all_subs = []

        top = subreddit.top()

        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
        embed = discord.Embed(title=name, description=None, colour=discord.Colour.random())
        embed.set_image(url=url)

        message = await ctx.send(embed=embed)
        await message.add_reaction("😂")
        await message.add_reaction("▶")
        await message.add_reaction("◀")
        message_id = message.id
        self.msg_list.append(message_id)




def setup(client):
    client.add_cog(Meme(client))
