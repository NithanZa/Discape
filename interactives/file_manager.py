from json import load, dump
from typing import Optional


async def load_data():
    try:
        async with open("interactives_data.json", "r") as json_file:
            data = load(json_file)
    except FileNotFoundError:
        return {}
    return data


async def set_interactive_user_data(message_id: int, user_id: int, attr: Optional[str], response: Optional[str]):
    data = await load_data()
    if message_id not in data:
        data[message_id] = {}
    if user_id not in data[message_id]:
        data[message_id][user_id] = {}
    if attr is not None:
        data[message_id]["attr"] = attr
    if response is not None:
        data[message_id]["response"] = response
    async with open("interactives_data.json", "w") as json_file:
        dump(data, json_file)


async def get_interactive_user_data(message_id: int):
    data = await load_data()
    try:
        return data[message_id]
    except KeyError:
        return {}
