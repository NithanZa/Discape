from typing import List

from yaml import safe_load
import discord
from discord import Embed
import aiofiles

INTERACTIVE_TYPES = (
    "enterpin"
)

puzzle_state = []
puzzle_index = 0


async def load_data():
    try:
        async with aiofiles.open("../config/puzzle.yml", "r") as json_file:
            contents = await json_file.read()
        data = safe_load(contents)
    except FileNotFoundError:
        return None
    return data


async def load_puzzle(ctx: discord.ApplicationContext):
    data = await load_data()
    if not data:
        await ctx.respond("puzzle.yml not found/empty!", ephemeral=True)
    elif isinstance(data, list):
        interactive_amount = 0
        for channel in data[puzzle_state]:
            for content in channel.items():
                if content[0].lower() in INTERACTIVE_TYPES:
                    interactive_amount += 1


async def load_embed(body: dict):
    # Optional params
    title: str = body["title"] if "title" in body else Embed.Empty
    colour_inp: str | int | list = body["colour"] if "colour" in body else Embed.Empty
    if isinstance(colour_inp, str):  # parses hex code
        if colour_inp.startswith("#"):
            colour_inp = colour_inp[1:]

        r = int(colour_inp[:2], 16)
        g = int(colour_inp[2:4], 16)
        b = int(colour_inp[4:6], 16)
        colour = discord.Colour.from_rgb(r, g, b)
    elif isinstance(colour_inp, int):  # discord's colour value thing???
        colour = colour_inp
    else:  # list of rgb
        colour = discord.Colour.from_rgb(colour_inp[0], colour_inp[1], colour_inp[2])

    content: str = body["content"] if "content" in body else Embed.Empty
    thumbnail: str = body["thumbnail"] if "thumbnail" in body else Embed.Empty  # url
    author: str = body["author"] if "author" in body else Embed.Empty
    author_icon: str = body["author_icon"] if "author_icon" in body else Embed.Empty  # url
    footer: str = body["footer"] if "footer" in body else Embed.Empty
    footer_icon: str = body["footer_icon"] if "footer_icon" in body else Embed.Empty  # url
    fields_inp: list = []  # NOT DONE!!
    embed = Embed(colour=colour,
                  title=title,
                  description=content
                  )
