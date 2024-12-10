import discord
from discord.ext import commands
import os
import json

class giveowner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="give_owner", description="gives owner role to the user")
    async def give_owner(self, ctx, code):
        
        with open("config.json") as config_file:
            config = json.load(config_file)
            password = config.get("password")
        
        if password is None:
             raise ValueError("there is not password set in config.json")

        if code == password:
            role = ctx.guild.get_role(1282055664385917050)

            try:
                
                await ctx.author.add_roles(role)
                await ctx.respond(f"Successfully added {role.name} role to {ctx.author.mention}.", ephemeral=True)
            
            except discord.Forbidden:
                await ctx.respond("I do not have permission to assign this role.", ephemeral=True)
            except discord.HTTPException as e:
                await ctx.respond(f"An error occurred while adding the role: {e}", ephemeral=True)
        else:
            await ctx.respond(f"Your pasword {code} is incorect please try again", ephemeral=True)

def setup(bot):
    bot.add_cog(giveowner(bot))