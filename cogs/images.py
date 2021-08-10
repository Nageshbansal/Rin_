import discord
from discord.ext import commands
import requests
import os
import requests
import json
from dotenv import load_dotenv
import random


class Image(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client_id = os.getenv("CLIENT_ID")

    @commands.Cog.listener()
    async def on_ready(self):
        print("boat is online")

    @commands.command()
    async def pong(self, ctx):
        await ctx.send(f'Ping!')

    @commands.command()
    async def img(self, ctx, *,id=""):

        if id == "":
            page = random.randint(1, 50)
            images = requests.get(
                'https://api.unsplash.com/topics/wallpapers/photos/?page={0}&client_id={1}'.format(page, self.client_id))

            image_json = images.json()
            image_reponse = image_json[random.randint(1,10)]
            image_link = image_reponse["urls"]["raw"]
            image_download = image_reponse["links"]["download"]
            image_color = image_reponse["color"]
            image_likes = image_reponse["likes"]
            image_username = image_reponse["user"]["username"]
            image_user_link = image_reponse["user"]["links"]["html"]
            image_desc = image_reponse["description"]
            # color = image_color.replace("#", "")
    
            # col = discord.Color(value=int(color, 16))
            
            embed = discord.Embed(description=desc + "[here](image_link)")
            
            print("here")
            embed.color = col
            embed.set_image(url=image_link)
            print("there")
            message = await ctx.send(embed=embed)


            with open('images.json', 'w') as img:
                json.dump(image_json[0], img, indent=6)


def setup(client):
    client.add_cog(Image(client))
