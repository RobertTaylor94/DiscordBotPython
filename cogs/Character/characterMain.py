from discord.ext import commands
from discord import app_commands, Embed, Interaction
from discord import SlashCommandGroup
import json
import os
import CharacterUtilities

os.chdir('cogs/Character')

class characterMain(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    utils = CharacterUtilities.characterUtils

    
    

async def setup(bot):
    await bot.add_cog(characterMain(bot))