from json import load, dump
from typing import Optional


async def load_data():
    try:
        async with open("interactives_data.json", "r") as json_file:
            data = load(json_file)
    except FileNotFoundError:
        return {}
    return data


async def set_message_attr(message_id: int, attr: Optional[str], response: Optional[str]):
    data = await load_data()
    interactive_info = data[message_id]
    if interactive_info is None:
        interactive_info = {}
    if attr is not None:
        interactive_info["attr"] = attr
    if response is not None:
        interactive_info["response"] = response
    async with open("interactives_data.json", "w") as json_file:
        dump(data, json_file)


async def get_message_attr(message_id: int):
    data = await load_data()
    try:
        return data[message_id]
    except KeyError:
        return {}
