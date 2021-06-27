import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import asyncio
import pafy
import os
from dotenv import load_dotenv

class Voice2(commands.Cog):


    def __init__(self,client):
        self.client = client
        self.song_queue = {}

    async def search_song(self , amount , song , get_url =False):
        








    @commands.Cog.listener()
    async def on_ready(self):
        print("Betavoice is online")

    @commands.command(aliases=['bj'])
    async def bjoin(self,ctx):

        if ctx.author.voice is None:
            await ctx.send("You must be connected to a voice channel")


        if ctx.voice_client is not None:
            await ctx.voice_client.disconnect()

        await ctx.author.voice.channel.connect()
        await ctx.send(f"bot connected from {ctx.author.voice.channel} ")

    @commands.command(aliases=['bl'])
    async def betaleave(self,ctx):
        channel = ctx.message.author.voice.channel
        voice = get(ctx.bot.voice_clients, guild=ctx.guild)

        if voice.is_connected():    # checking bot is connected
            await voice.disconnect()        # disconnect bot
            print(f"bot disconnected {channel}")
            await ctx.channel.send(f"left {channel}")

        else:
            print(f"bot is not in  {channel}\n")
            await ctx.send(f"bot is not in  {channel}\n")























def setup(client):
    client.add_cog(Voice2(client))
