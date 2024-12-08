import discord
from discord.ext import commands


class purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="purge", description="remove a set amount of messages")
    async def purge(self, ctx, amount: int):    

        await ctx.respond("deleting messages ...", ephemeral=True)

        channel = ctx.channel
        messages = await channel.history(limit=amount).flatten()

        for message in messages:
            await message.delete()
    
    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user:
            return
        print(message.content)
        if message.content.startswith("purge"):

            if message.author.guild_permissions.administrator:

                if message.guild.me.guild_permissions.administrator:

                    try:

                        amount = int(message.content.split()[1])
                        await message.channel.send("deleting messages ...")

                        messages = await message.channel.history(limit=amount).flatten()

                        for message in messages:
                            await message.delete()

                    except (IndexError, ValueError):
                            await message.channel.send("Please provide a valid number of messages to delete.", delete_after=5)
                            return

                else:
                    await message.channel.send("I don't have permission to delete messages.", delete_after=5)
                    return

            else:
                await message.channel.send("You need administrator permissions to use this command.", delete_after=5)
                return

def setup(bot):
    bot.add_cog(purge(bot))