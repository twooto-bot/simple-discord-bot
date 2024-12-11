import requests
import discord
from discord.ext import commands
import json
import base64

# api function
def getinfo(API, username):

    mojang = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}", timeout=10).json()
    skin = requests.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{mojang["id"]}").json()
    request = requests.get(f"https://api.hypixel.net/v2/skyblock/profiles?key={API}&uuid={mojang["id"]}", timeout=10).json()

    return request, skin

# getting skin texture
def getting_player_skin(player_skin_bytes):

    player_skin_str = player_skin_bytes.decode('utf-8')
    player_skin = json.loads(player_skin_str)

    return player_skin

# create cog
class networth(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #creating command
    @commands.slash_command(name="networth", description="shows you your skyblock networth")
    async def networth(self, ctx, name):

        API = "38990b60-31e7-41ac-80ec-30224f77b524"

        data, skin_dict = getinfo(API, name)

        # getting skin bytes and converting to dict
        skin_dict = getting_player_skin(base64.b64decode(skin_dict["properties"][0]["value"]))

        # discord side stuff
        try:

            await ctx.respond(f"getting player info ...", ephemeral=True)

            if data["success"] == False:
                await ctx.send(f"there was a problem fetching the player info from {username} please try again", ephemeral=True)
                return
            
            # creating embed
            embed = discord.Embed(
                title=f"Skyblock Stats for {name}",
                description="Here are the detailed stats for your Skyblock profile!",
                color=discord.Color.blue()
            )

            embed.set_thumbnail(url = skin_dict["textures"]["SKIN"]["url"])

            embed.add_field(name="Health", value="1200", inline=True)
            embed.add_field(name="Defense", value="850", inline=True)
            embed.add_field(name="Strength", value="230", inline=True)
            embed.add_field(name="Critical Damage", value="250%", inline=True)
            embed.add_field(name="Mana", value="350", inline=True)
            embed.add_field(name="Speed", value="125%", inline=True)

            embed.set_footer(text="made by twooto")
            embed.timestamp = discord.utils.utcnow()

            embed.set_author(
                name="Skyblock Bot",
                icon_url=self.bot.user.avatar,
            )

            await ctx.send(embed=embed)

        except UnicodeEncodeError as e:
            await ctx.send(f"Encoding error: {e}", ephemeral=True)

def setup(bot):
    bot.add_cog(networth(bot))
