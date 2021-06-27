import discord
from discord.ext import  commands
import requests
import os
from dotenv import load_dotenv

class Image(commands.Cog):

    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("boat is online")

    @commands.command()
    async def pong(self, ctx):
        await ctx.send(f'Ping!')



def setup(client):
    client.add_cog(Image(client))





