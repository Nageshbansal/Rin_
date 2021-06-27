import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv
from code_name import states_name, code_names

load_dotenv()
API_KEY = os.getenv("API_KEY")

headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("bot is online")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong!')

    @commands.command()
    async def clear(self, ctx, amount=1):
        dlt = amount + 1
        await ctx.channel.purge(limit=dlt)

    @commands.command()
    async def cs(self, ctx, *, country='india'):
        # for countries
        try:
            response = requests.get(
                f"https://covid-193.p.rapidapi.com/history?country={country}", headers=headers)
            json_response = response.json()

            cases = json_response['response'][0]['cases']
            deaths = json_response['response'][0]['deaths']
            tests = json_response['response'][0]['tests']

            #embed
            embed = discord.Embed(
                title=f"Covid19 Stats of {country}", colour=discord.Colour.green())
            embed.add_field(name="New cases", value=cases['new'], inline=False)
            embed.add_field(name="Active cases",
                            value=cases['active'], inline=True)
            embed.add_field(name="Critical cases",
                            value=cases['critical'], inline=False)
            embed.add_field(name="Recovered cases",
                            value=cases['recovered'], inline=False)
            embed.add_field(name="Total cases",
                            value=cases['total'], inline=True)
            embed.add_field(name="New deaths",
                            value=deaths['new'], inline=False)
            embed.add_field(name="Total deaths",
                            value=deaths['total'], inline=False)
            embed.add_field(name="Total tests",
                            value=tests['total'], inline=False)
            await ctx.send(embed=embed)
# for States

        except:

            country = country.lower()
            if country in states_name:
                index = states_name.index(country)
                elb = country.upper()
                country = code_names[index]
                print(country)
            response = requests.get(
                f"https://api.covid19india.org/v4/min/data.min.json")
            json_response = response.json()

            # reteriving data from api

            cases = (json_response[country]['total']['confirmed'])
            deceased = (json_response[country]['total']['deceased'])
            recovered = (json_response[country]['total']['recovered'])
            tested = (json_response[country]['total']['tested'])
            vaccinated = (json_response[country]['total']['vaccinated'])
            source = json_response[country]['meta']['tested']['source']
            last_updated = json_response[country]['meta']['tested']['last_updated']

            # embeding data in bot
            embed = discord.Embed(
                title=f"Covid19 Stats of {elb}", colour=discord.Colour.green())
            embed.add_field(name="Source", value=source, inline=False)
            embed.add_field(name="Confirmed cases", value=cases, inline=True)
            embed.add_field(name="Decreased cases",
                            value=deceased, inline=False)
            embed.add_field(name="Recovered cases",
                            value=recovered, inline=True)
            embed.add_field(name="Tested cases", value=tested, inline=False)
            embed.add_field(name="Vaccinated cases",
                            value=vaccinated, inline=True)
            embed.add_field(name="Last_Updated",
                            value=last_updated, inline=False)
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Example(client))
