import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
from dotenv import load_dotenv

players = {}

class Music(commands.Cog):

    def __init__(self, client):
        self.client = client


    """Intializing commands """
    @commands.Cog.listener()
    async def on_ready(self):
        print("voice is online")

    @commands.command()
    async def print(self, ctx):
        pass
    """ JOin command"""
    @commands.command(aliases=['j'])
    async def join(self,ctx):
        if ctx.author.voice:            # checking author is connected to voice channel
            channel = ctx.message.author.voice.channel
            voice = get(ctx.bot.voice_clients, guild=ctx.guild)

            if voice and voice.is_connected():   # moving bot to the author channel
                await voice.move_to(channel)       # move bot

            else:                               # connecting bot
                await channel.connect()         # connecting bot
                await ctx.send(f'Joined {channel}')
        else:                         # sending response
            await ctx.send("You must be in a voice channel to use this command!!")


    @commands.command(aliases=['l'])
    async def leave(self, ctx):             # leave command
        channel = ctx.message.author.voice.channel
        voice = get(ctx.bot.voice_clients, guild=ctx.guild)

        if voice and voice.is_connected():   # checking bot is connected
            await voice.disconnect()        # disconnect bot
            print(f"bot disconnected {channel}")
            await ctx.channel.send(f"left {channel}")

        else:
            print(f"bot is not in  {channel}\n")
            await ctx.send(f"bot is not in  {channel}\n")

    @commands.command(aliases=['p'])
    async def play(self, ctx, url:str):   # play command
        song_there = os.path.isfile("song.mp3")  # checking is there file song.mp3
        try:
            if song_there:
                os.remove("song.mp3")
        except PermissionError:
            await ctx.send("wait for the music to be completed ")

        await Music.join(self,ctx)  # calling the join method
        channel = (ctx.message.author.voice.channel)  # defining  the author
        voice = get(ctx.bot.voice_clients, guild=ctx.guild)
        ydl_opts = {                                   # ydl_options
            'format' : 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],

        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:   # searching the song by youtube_dl
            ydl.download([url])

        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file,"song.mp3")
        await ctx.send(f"Playing..{url}")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))

    @commands.command(aliases=['pau'])
    async def pause(self, ctx):
        voice = get(ctx.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
            await ctx.send("Paused")
        else:
            await ctx.send("Currently no audio is not playing")


    @commands.command(aliases=['r'])
    async def resume(self, ctx):
        voice = get(ctx.bot.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
            await ctx.send("Resumed")
        else:
            await ctx.send("  audio is not paused")

    @commands.command(aliases=['s'])
    async def stop(self, ctx):
        voice = get(ctx.bot.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.stop()
            await Music.leave(self,ctx)
        else:
            await ctx.send("Currently no audio is not playing")









def setup(client):
    client.add_cog(Music(client))
