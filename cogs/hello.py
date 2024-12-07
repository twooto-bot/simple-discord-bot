import discord
from discord.ext import commands

class hello(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="greed", description="says hello")
    async def greed(self, ctx):
        await ctx.respond("sending message", ephemeral=True)
        await ctx.send(f"Hello <@{ctx.author.id}>!")

def setup(bot):
    bot.add_cog(hello(bot))
