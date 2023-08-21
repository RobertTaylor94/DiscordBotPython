from discord.ext import commands
from discord import app_commands, Embed, Interaction
from typing import Literal
import json
import os
from cogs.Character.CharacterUtilities import characterUtils

os.chdir('cogs/Character')

class characterMain(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    util = characterUtils()

    @app_commands.command(name='init', description='initialise player in character database')
    async def init(self, interaction: Interaction):
        print('init called')
        characters = await self.util.get_characters()
        if str(interaction.user.id) not in characters:
            print('user not found in characters')
            characters[str(interaction.user.id)] = []
            print(characters)
            await self.util.save_characters(characters)
        await interaction.response.send_message("user initialized in character database", ephemeral = True)

    # @app_commands.command(name='create_character', description='Create a new character')
    # @app_commands.describe(name = 'name', race = 'race')
    # async def create_character(self, interaction: Interaction, name: str, race: Literal['dwarf', 'elf', 'gnome', 'halfling', 'human', 'orc']):
    #     characters = await self.util.get_characters()

async def setup(bot):
    await bot.add_cog(characterMain(bot))