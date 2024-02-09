import discord
from discord import Interaction
from interactives.file_manager import get_interactive_info, set_interactive_info
from asyncio import sleep


class NumberButton(discord.ui.Button):
    def __init__(self, label, row):
        super().__init__(style=discord.ButtonStyle.primary, label=label, row=row)

    async def callback(self, interaction: Interaction):
        message_id = interaction.message.id
        number = self.label
        attr = await get_interactive_info(message_id)
        response_interaction = await interaction.response.send_message("hello!", ephemeral=True)
        await sleep(2)
        response_message: discord.InteractionMessage = await response_interaction.original_response()
        await response_message.edit(content=f"Msg id is {response_message.id}")
        await sleep(2)
        await response_message.delete()


class PINView(discord.ui.View):
    async def setup_buttons(self):
        self.add_item(NumberButton(label="1", row=0))

        # # the loop, and the row argument arranges it into the standard PIN order thing
        # for i in range(1, 10):
        #     button = discord.ui.Button(style=discord.ButtonStyle.primary, label=str(i), row=(i - 1) // 3)
        #     button.callback = self.button_callback
        #     self.add_item(button)
