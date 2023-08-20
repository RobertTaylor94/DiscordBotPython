from discord.ext import commands
from discord import app_commands, Embed, Interaction
from discord import SlashCommandGroup
from typing import Literal
import json
import os
import CharacterUtilities

os.chdir('cogs/Character')

class characterMain(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    util = CharacterUtilities.characterUtils

    @app_commands.command(name='create_character', description='Create a new character')
    @app_commands.describe(name = 'name', race = 'race')
    async def create_character(self, interaction: Interaction, name: str, race: Literal['dwarf', 'elf', 'gnome', 'halfling', 'human', 'orc']):
        characters = await self.util.get_characters()
    

async def setup(bot):
    await bot.add_cog(characterMain(bot))