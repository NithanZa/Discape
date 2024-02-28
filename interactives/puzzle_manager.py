from yaml import safe_load
from discord import Embed
import discord
import aiofiles

INTERACTIVE_TYPES = (
    "enterpin"
)

puzzle_state = []
puzzle_index = 0


async def load_data(filename: str):
    try:
        async with aiofiles.open(f"../config/{filename}", "r") as json_file:
            contents = await json_file.read()
        data = safe_load(contents)
    except FileNotFoundError:
        return None
    return data


async def load_puzzle(ctx: discord.ApplicationContext, filename: str):
    data = await load_data(filename)
    if not data:
        await ctx.respond(f"{filename} not found/empty! Make sure to put it in the config folder", ephemeral=True)
    elif type(data) == list:
        interactive_amount = 0
        for channel in data[puzzle_state]:
            for content in channel.items():
                if content[0].lower() in INTERACTIVE_TYPES:
                    interactive_amount += 1


async def load_embed(body: dict) -> Embed:
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
    url: str = body["url"] if "url" in body else Embed.Empty
    thumbnail: str = body["thumbnail"] if "thumbnail" in body else Embed.Empty  # url
    author: str = body["author"] if "author" in body else Embed.Empty
    author_icon: str = body["author_icon"] if "author_icon" in body else Embed.Empty  # url
    author_url: str = body["author_url"] if "author_url" in body else Embed.Empty
    footer: str = body["footer"] if "footer" in body else Embed.Empty
    footer_icon: str = body["footer_icon"] if "footer_icon" in body else Embed.Empty  # url

    # Makes a list of `discord.EmbedField`
    if "fields" in body:
        fields_dict = body["fields"]
        fields = [None] * len(fields_dict)

        for i, (field_name, field_value) in enumerate(fields_dict.items()):
            fields[i] = discord.EmbedField(field_name, field_value)
    else:
        fields = None

    embed = Embed(colour=colour,
                  title=title,
                  url=url,
                  description=content,
                  fields=fields
                  )

    embed.set_thumbnail(thumbnail)
    embed.set_author(author, author_url, author_icon)
    embed.set_footer(footer, footer_icon)
    return embed
