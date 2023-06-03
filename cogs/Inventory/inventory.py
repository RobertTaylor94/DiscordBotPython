from discord.ext import commands
from discord import app_commands, Embed, Interaction
import json
import os 

os.chdir('cogs/Inventory')

class inventory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='inventory', description='Get your player inventory contents')
    async def inventory(self, interaction: Interaction):
        print('get_inventory called')
        inventory = await self.get_inventory()
        print('got inventory)')
        em = Embed(title=f"{interaction.user.name}'s Inventory")
        
        if str(interaction.user.id) not in inventory:
            inventory[str(interaction.user.id)] = []
            with open("inventory.json", "w") as f:
                json.dump(inventory, f)
                print('json saved')
            em.description = 'Inventory empty'
            await interaction.response.send_message(embed=em)
        else:
            player_inventory = inventory[str(interaction.user.id)]
            for item in player_inventory:
                    name = item['name']
                    desc = item['description']
                    em.add_field(name = name, value=f'{desc}')
            await interaction.response.send_message(embed=em)
            
    @app_commands.command(name='add_inventory', description='Add an item to your inventory')
    @app_commands.describe(name='name', description='description')
    async def add(self, interaction: Interaction, name: str, description: str):
        inventory = await self.get_inventory()
        

    async def get_inventory(self):
        print('get inventory called')
        os.chdir('../Inventory')
        print(os.getcwd())
        with open("inventory.json", "r") as f:
            inventory = json.load(f)
            print(inventory)
            return inventory

async def setup(bot):
    await bot.add_cog(inventory(bot))