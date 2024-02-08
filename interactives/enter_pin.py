import discord
from discord import Interaction
from interaction_manager import get_message_attr, set_message_attr


class NumberButton(discord.ui.Button):
    async def callback(self, interaction: Interaction):
        message_id = interaction.message.id

        pass


class PINView(discord.ui.View):
    async def setup_buttons(self):

        # the loop, and the row argument arranges it into the standard PIN order thing
        for i in range(1, 10):
            button = discord.ui.Button(style=discord.ButtonStyle.primary, label=str(i), row=(i - 1) // 3)
            button.callback = self.button_callback
            self.add_item(button)
