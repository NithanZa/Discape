from yaml import safe_load
import discord
import aiofiles


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
    if data is None:
        await ctx.respond("puzzle.yml not found!", ephemeral=True)
    elif type(data) == list:
        if data == []:
            await ctx.respond("puzzle.yml has an empty list")
        else:
            interactive_amount = 0
            for channel in data[puzzle_state]:

