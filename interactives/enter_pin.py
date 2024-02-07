import discord
from discord import Interaction


class NumberButton(discord.ui.Button):
    async def callback(self, interaction: Interaction):
        pass

class PINView(discord.ui.View):
    async def button_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(f"Clicked {button.label}")

    async def setup_buttons(self):
        # the loop, and the row argument arranges it into the standard PIN order thing
        for i in range(1, 10):
            button = discord.ui.Button(style=discord.ButtonStyle.primary, label=str(i), row=(i - 1) // 3)
            button.callback = self.button_callback
            self.add_item(button)
