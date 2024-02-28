from yaml import safe_load, safe_dump
from json.decoder import JSONDecodeError
from typing import Optional
import aiofiles


async def load_data():
    try:
        async with aiofiles.open("../config/interactives_data.yml", "r") as json_file:
            contents = await json_file.read()
        data = safe_load(contents)
    except (FileNotFoundError, JSONDecodeError):
        print('hi')
        return {}
    return data


async def set_interactive_user_data(interactive: str, user_id: str, attr: Optional[str]):
    data = await load_data()
    print('b1' + str(data))
    if interactive not in data:
        data[interactive] = {}
        print('b2' + str(data))
    if user_id not in data[interactive]:
        data[interactive][user_id] = {}
        print('b3' + str(data))
    if attr is not None:
        data[interactive][user_id]["attr"] = attr
        print('b4' + str(data))
    async with aiofiles.open("../config/interactives_data.yml", "w") as json_file:
        await json_file.write(safe_dump(data))


async def get_interactive_user_data(interactive: str, user_id: str):
    data = await load_data()
    try:
        return data[interactive][user_id]
    except KeyError:
        return {}


async def clear_interactive_data(interactive: str):
    data = await load_data()
    data.pop(interactive, None)
    async with aiofiles.open("interactives_data.json", "w") as json_file:
        await json_file.write(dumps(data))


async def clear_all_data():
    async with aiofiles.open("interactives_data.json", "w") as json_file:
        await json_file.write(dumps({}))

