from discord.ext import commands
from discord import app_commands, Embed, Interaction
import json
import os 

os.chdir('cogs/CustomRolls')

class create_attack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name = 'create_attack', description = 'Add a custom attack roll to your character')
    @app_commands.describe(name = 'name', atbonus = 'atkbonus', dmgdice = 'dmgdice (e.g. 1d10 + 1d4)', dmgbonus = 'dmgbonus')
    async def create_attack(self, interaction: Interaction, name: str, atkbonus: int, dmgdice: str, dmgbonus: int, atkdice = '1d20'):
        print('running create_attack')
    

    async def get_custom_rolls(self):
        print('getting custom rolls...')
        os.chdir('../CustomRolls')
        with open('customRolls.json', 'r') as f:
            customRolls = json.load(f)
            return customRolls

async def setup(bot):
    await bot.add_cog(create_attack(bot))