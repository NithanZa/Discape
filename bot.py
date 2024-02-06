from os import getenv
import discord

bot = discord.Bot()


@bot.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")


def run():
    bot.run(getenv("DISCAPE_TOKEN"))
