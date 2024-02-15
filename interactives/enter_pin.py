from typing import Optional

import discord
from discord import Interaction

import bot_manager
from interactives.user_data_manager import get_interactive_user_data, set_interactive_user_data, clear_interactive_data
from asyncio import sleep


class NumberButton(discord.ui.Button):
    def __init__(self, label, row):
        super().__init__(style=discord.ButtonStyle.primary, label=label, row=row)

    async def callback(self, interaction: Interaction):
        user_id = interaction.user.id
        message_id = str(interaction.message.id)
        number = self.label
        # fetch previously entered pin
        interactive_data = await get_interactive_user_data(message_id, str(user_id))
        try:
            current_pin = interactive_data["attr"] + number
        except KeyError:
            print(interactive_data)
            current_pin = number
        
        await set_interactive_user_data(message_id, str(user_id), current_pin)
        await interaction.response.send_message(f"Entered PIN: {current_pin}", ephemeral=True, delete_after=1.5)


class BackspaceButton(discord.ui.Button):
    def __init__(self, row):
        super().__init__(style=discord.ButtonStyle.danger, label="⌫", row=row)

    async def callback(self, interaction: Interaction):
        user_id = interaction.user.id
        message_id = str(interaction.message.id)
        interactive_data = await get_interactive_user_data(message_id, str(user_id))
        try:
            # deletes a number
            current_pin = interactive_data["attr"][:-1]
            if current_pin:
                await interaction.response.send_message(f"Entered PIN: {current_pin}", ephemeral=True, delete_after=1.5)
            else:
                await interaction.response.send_message(f"Entered PIN is now empty", ephemeral=True, delete_after=1.5)

            await set_interactive_user_data(message_id, str(user_id), current_pin)
        except KeyError:
            pass


class SubmitButton(discord.ui.Button):
    def __init__(self, row):
        super().__init__(style=discord.ButtonStyle.success, emoji="✅", row=row)

    async def callback(self, interaction: Interaction):
        user_id = interaction.user.id
        message_id = str(interaction.message.id)
        interactive_data = await get_interactive_user_data(message_id, str(user_id))
        try:
            current_pin = interactive_data["attr"]
        except KeyError:
            current_pin = ""
        if current_pin == self.view.answer:
            await interaction.response.send_message(f"PIN is correct! (PIN: {current_pin})", delete_after=2)
            self.view.disable_all_items()
            await interaction.message.edit(view=self.view)
            await clear_interactive_data(message_id)
        else:
            await interaction.response.send_message(f"PIN is wrong! (Entered PIN: {current_pin})", delete_after=2)
            await set_interactive_user_data(message_id, str(user_id), "")


class PINView(discord.ui.View):
    def __init__(self, answer: str):
        super().__init__()
        self.answer = answer

        # the loop, and the row argument arranges it into the standard PIN order thing
        for i in range(1, 10):
            self.add_item(NumberButton(str(i), (i - 1) // 3))

        self.add_item(BackspaceButton(4))
        self.add_item(NumberButton('0', 4))
        self.add_item(SubmitButton(4))
