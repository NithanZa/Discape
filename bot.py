from os import getenv
import discord
from yaml import safe_load
from sys import exit
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

with open('config.yml', 'r') as file:
    CONFIG = safe_load(file)
    if CONFIG is None:
        print("config.yml not found, exiting program")
        exit()

DEBUG_MODE = CONFIG['debug_mode']

if DEBUG_MODE:
    DEBUG_GUILD_IDS = CONFIG['debug_guild_ids']
    bot = discord.Bot(debug_guilds=DEBUG_GUILD_IDS)
else:
    bot = discord.Bot()


@bot.slash_command(name="ping", description="Test the latency of the bot")
async def ping(ctx):
    await ctx.respond(f"Pong! (Latency: {(bot.latency*1000):.2f} ms)")


def run():
    bot.run(TOKEN)
