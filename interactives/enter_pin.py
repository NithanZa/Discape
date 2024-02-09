import discord
from discord import Interaction
from interactives.file_manager import get_message_attr, set_message_attr
from asyncio import sleep


class NumberButton(discord.ui.Button):
    async def callback(self, interaction: Interaction):
        message_id = interaction.message.id
        attr = await get_message_attr(message_id)
        response_interaction = await interaction.response.send_message("hello!", ephemeral=True)
        await sleep(2)
        response_message: discord.InteractionMessage = await response_interaction.original_response()
        await response_message.edit(content="hir")



class PINView(discord.ui.View):
    async def setup_buttons(self):
        self.add_item(NumberButton(style=discord.ButtonStyle.primary, label="1", row=0))

        # # the loop, and the row argument arranges it into the standard PIN order thing
        # for i in range(1, 10):
        #     button = discord.ui.Button(style=discord.ButtonStyle.primary, label=str(i), row=(i - 1) // 3)
        #     button.callback = self.button_callback
        #     self.add_item(button)
