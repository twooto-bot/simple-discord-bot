import discord
from discord.ext import commands

class math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="math", description="do simple math")
    async def math(self, ctx, number1: int, number2: int, function: str):

        await ctx.respond("Calculating 1 sec!", ephemeral=True)

        total = None

        if function == "+":
            total = number1 + number2

        elif function == "-":
            total = number1 - number2

        elif function == "*":
            total = number1 * number2

        elif function == "/":
            if number2 == 0:
                await ctx.send("Cannot devide by 0 learn math!")
                return
            else:
                total = number1 / number2
        
        if function != "+" or "-" or "*" or "/":
            await ctx.respond(f"Unknown operation: {function}. Please use '+', '-', '*', or '/'.", ephemeral=True)

        if total == 0:
            await ctx.send("why make me do math if you aswnser is just 0")
            return

        await ctx.send(f"Your awnser is {total}")
        

def setup(bot):
    bot.add_cog(math(bot))
