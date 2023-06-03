from discord.ext import commands
from discord import app_commands, Embed, Interaction
import json
import os 

os.chdir('cogs/Supplies')

class inventory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='get_inventory', description='Get your player inventory contents')
    async def get_inventory(self, interaction: Interaction):
        inventory = self.get_inventory()

    
    @app_commands.command(name='add_inventory', description='Add an item to your inventory')
    @app_commands.describe(name='name', description='description')
    async def add(self, interaction: Interaction, name: str, description: str):
        inventory = self.get_inventory()

    async def get_inventory(self):
        print('get inventory called')
        with open("inventory.json", "r") as f:
            inventory = json.load(f)
            print(inventory)
            return inventory

async def setup(bot):
    await bot.add_cog(inventory(bot))