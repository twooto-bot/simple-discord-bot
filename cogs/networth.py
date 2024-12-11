import requests
import discord
from discord.ext import commands
import json

def getinfo(API, username):
    mojang = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}", timeout=10).json()
    request = requests.get(f"https://api.hypixel.net/player?key={API}&uuid={mojang["id"]}", timeout=10)
    return request.json()

class networth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="networth", description="shows you your skyblock networth")
    async def networth(self, ctx, name):

        API = "38990b60-31e7-41ac-80ec-30224f77b524"
        data = getinfo(API, name)

        try:

            await ctx.respond(f"getting player info ...", ephemeral=True)

            if data["success"] == False:
                return
            
            
            username = data["player"]["displayname"]
            uuid = data["player"]["uuid"]
            await ctx.send(f"player username {username} and player uuid {uuid}")

        except UnicodeEncodeError as e:
            await ctx.send(f"Encoding error: {e}", ephemeral=True)

def setup(bot):
    bot.add_cog(networth(bot))
