import discord
from discord.ext import commands

class embeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name ="embed", description ="send a embed")
    async def embed(slef, ctx):

        embed = discord.Embed(
            title="this is a embed",
            description="this is the description of the embed",
            color=discord.Color.green()
        )
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(embeds(bot))