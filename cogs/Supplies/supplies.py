from discord.ext import commands
from discord import app_commands, Embed
from discord.interactions import Interaction
import json
import os 

class inventory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='supplies', description='Check the food and drink supplies held on the ship')
    async def supplies(self, interaction: Interaction):
        print('supplies called...')
        supplies = await self.get_supplies()
        print('supplies loaded')

    async def set_supplies(self):
        supplies = await self.get_supplies()

        print('json loaded')

        if str('food') in supplies:
            print('returning false...')
            return False
        else:
            supplies[str('food')] = 0
            supplies[str('drink')] = 0

        with open("supplies.json", "w") as f:
            json.dump(supplies, f)
        return True
    
    async def get_supplies(self):
        print('get supplies called')
        with open("supplies.json", "r") as f:
            supplies = json.load(f)
            return supplies

async def setup(bot):
    await bot.add_cog(inventory(bot))