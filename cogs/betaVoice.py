import discord
from discord.ext import commands
from discord.utils import get
from youtube_dl import YoutubeDL

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        #all the music related stuff
        self.is_playing = False

        # 2d array containing [song, channel]
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        self.vc = ""
        

    #  #searching the item on youtube
    # def search_yt(self, item):
    #     with YoutubeDL(self.YDL_OPTIONS) as ydl:
    #         try:
    #             info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
    #         except Exception:
    #             return False

    #     return {'source': info['formats'][0]['url'], 'title': info['title']}

    # def play_next(self):
    #     if len(self.music_queue) > 0:
    #         self.is_playing = True

    #         #get the first url
    #         m_url = self.music_queue[0][0]['source']

    #         #remove the first element as you are currently playing it
    #         self.music_queue.pop(0)

    #         self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
    #     else:
    #         self.is_playing = False

    # # infinite loop checking
    # async def play_music(self):
    #     if len(self.music_queue) > 0:
    #         self.is_playing = True

    #         m_url = self.music_queue[0][0]['source']

    #         #try to connect to voice channel if you are not already connected

    #         if self.vc == "" or not self.vc.is_connected() or self.vc == None:
    #             self.vc = await self.music_queue[0][1].connect()
    #         else:
    #             await self.vc.move_to(self.music_queue[0][1])

    #         print(self.music_queue)
    #         #remove the first element as you are currently playing it
    #         self.music_queue.pop(0)

    #         self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
    #     else:
    #         self.is_playing = False

    # @commands.command(aliases=['j'])
    # async def join(self,ctx):
    #     if ctx.author.voice:            # checking author is connected to voice channel
    #             channel = ctx.message.author.voice.channel
    #             voice = get(ctx.bot.voice_clients, guild=ctx.guild)

    #             if voice and voice.is_connected():   # moving bot to the author channel
    #                 await voice.move_to(channel)       # move bot

    #             else:                               # connecting bot
    #                 await channel.connect()         # connecting bot
    #                 await ctx.send(f'Joined {channel}')
    #     else:                         # sending response
    #             await ctx.send("You must be in a voice channel to use this command!!")

    # @commands.command(aliases=['l'])
    # async def leave(self, ctx):             # leave command
    #     channel = ctx.message.author.voice.channel
    #     voice = get(ctx.bot.voice_clients, guild=ctx.guild)

    #     if voice and voice.is_connected():   # checking bot is connected
    #         await voice.disconnect()        # disconnect bot
    #         print(f"bot disconnected {channel}")
    #         await ctx.channel.send(f"left {channel}")

    #     else:
    #         print(f"bot is not in  {channel}\n")
    #         await ctx.send(f"bot is not in  {channel}\n")


    # @commands.command(aliases=['p'])
    # async def play(self, ctx, *args):
    #     query = " ".join(args)

    #     voice_channel = ctx.author.voice.channel

    #     music_cog.join(self,ctx)
    #     song = self.search_yt(query)
    #     if type(song) == type(True):
    #         await ctx.send("Could not download the song. Incorrect format try another keyword. This could be due to playlist or a livestream format.")
    #     else:
    #         await ctx.send("Song added to the queue")
    #         self.music_queue.append([song, voice_channel])

    #         if self.is_playing == False:
    #             await self.play_music()

    # @commands.command(aliases=['q'])
    # async def queue(self, ctx):
    #     retval = ""
    #     for i in range(0, len(self.music_queue)):
    #         retval += self.music_queue[i][0]['title'] + "\n"

    #     print(retval)
    #     if retval != "":
    #         await ctx.send(retval)
    #     else:
    #         await ctx.send("No music in queue")

    # @commands.command(aliases=['s'])
    # async def skip(self, ctx):
    #     if self.vc != "" and self.vc:
    #         self.vc.stop()
    #         #try to play next in the queue if it exists
    #         await self.play_music()


def setup(client):
    client.add_cog(music_cog(client))
