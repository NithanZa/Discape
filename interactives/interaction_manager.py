from json import load, dump


async def load_data():
    async with open("interactives_data.json", "r") as json_file:
        data = load(json_file)
    return data


async def set_message_attr(message_id: int, attr: str):
    data = await load_data()
    data[message_id] = attr
    async with open("interactives_data.json", "w") as json_file:
        dump(data, json_file)


async def get_message_attr(message_id: int):
    data = await load_data()
    return data[message_id]
