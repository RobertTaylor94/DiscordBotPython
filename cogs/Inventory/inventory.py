from discord.ext import commands
from discord import app_commands, Embed, Interaction
import json
import os 

os.chdir('cogs/Supplies')

class inventory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def get_inventory(self):
        print('get inventory called')
        with open("inventory.json", "r") as f:
            inventory = json.load(f)
            print(inventory)
            return inventory


async def setup(bot):
    await bot.add_cog(inventory(bot))