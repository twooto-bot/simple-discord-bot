import discord
import os
import json

try:
    path = os.getcwd()
    config_path = os.path.join(path, "config.json")

    with open(config_path) as main_config:
        config = json.load(main_config)
        TOKEN = config.get("TOKEN")
   
    if TOKEN == None:
        raise ValueError("there is no token set in config.js")

except FileNotFoundError:
    print("config was not found")

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)

@bot.event
async def on_ready():
    print(f"Loged in as {bot.user}")

bot.load_extension("cogs.hello")
bot.load_extension("cogs.math")
bot.load_extension("cogs.embeds")
bot.load_extension("cogs.raid")
bot.load_extension("cogs.purge")

bot.run(TOKEN)
