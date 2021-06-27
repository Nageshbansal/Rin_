import discord
from discord.ext import commands
import json
import os
from dotenv import load_dotenv
import requests

client = commands.Bot(command_prefix = ">")

command_prefix = ">"

@client.event
async def on_ready():
    activity = discord.Game(name=f"{command_prefix}help")
    print("Bot is ready!")






for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')






@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send('please pass all required arguments')
    if isinstance(error,commands.CommandNotFound):
        await ctx.send('this command doesnt exist')





load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
