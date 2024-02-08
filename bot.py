from os import getenv
import discord
from yaml import safe_load
from sys import exit
from dotenv import load_dotenv
from asyncio import sleep
from interactives.enter_pin import PINView

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
async def ping(ctx: discord.ApplicationContext):
    interaction = await ctx.respond(f"Pong! (Latency: {(bot.latency * 1000):.2f} ms)", ephemeral=True)
    await sleep(2)
    await interaction.edit_original_response(content="hi")


@bot.slash_command(name="pintest")
async def pintest(ctx):
    view = PINView()
    await view.setup_buttons()
    await ctx.respond("Buttons!", view=view)


def run():
    bot.run(TOKEN)
