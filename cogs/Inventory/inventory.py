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
        print('got inventory')
        em = Embed(title=f"{interaction.user.name}'s Inventory")
        
        if str(interaction.user.id) not in inventory:
            inventory[str(interaction.user.id)] = []
            with open("inventory.json", "w") as f:
                json.dump(inventory, f)
                print('json saved')
        else:
            player_inventory = inventory[str(interaction.user.id)]
            for item in player_inventory:
                item_name = item['Name']
                desc = item['description']
                em.add_field(name=item_name, value=desc)
        
        await interaction.response.send_message(embed=em, ephemeral = True)
            
    @app_commands.command(name='add_inventory', description='Add an item to your inventory')
    @app_commands.describe(name='name', description='description')
    async def add(self, interaction: Interaction, name: str, description: str):
        inventory = await self.get_inventory()
        player_inventory = inventory[str(interaction.user.id)]
        if player_inventory == None:
            print('Player inventory not found')
        new_item = {'Name': name, 'description': description}
        print(player_inventory)
        player_inventory.append(new_item)

        inventory[str(interaction.user.id)] = player_inventory

        with open("inventory.json", "w") as f:
            json.dump(inventory, f)
            print('json saved')

        em = Embed(title=f'{interaction.user.name}')
        em.add_field(name=new_item['Name'], value=new_item['description'])

        await interaction.response.send_message(embed = em, ephemeral = True)

    @app_commands.command(name='delete', description='Remove an item from your inventory')
    @app_commands.describe(item='item')
    async def delete(self, interaction: Interaction, item: str):
        inventory = await self.get_inventory()
        player_inventory = inventory[str(interaction.user.id)]
        deleted_item = item
        for i, item in enumerate(player_inventory):
            print(f'current index: {i}')
            if player_inventory[i]['Name'] == deleted_item:
                print('deleting this item')
                del player_inventory[i]
            else:
                print('item not deleted')
        print(f'New inventory {player_inventory}')

        inventory[str(interaction.user.id)] = player_inventory
        with open("inventory.json", "w") as f:
            json.dump(inventory, f)
            print('json saved')
        
        em = Embed(title = f"{interaction.user.name}'s Inventory")
        for item in player_inventory:
                item_name = item['Name']
                desc = item['description']
                em.add_field(name=item_name, value=desc)

        await interaction.response.send_message(embed = em, ephemeral = True)

    async def get_inventory(self):
        print('get inventory called')
        os.chdir('../Inventory')
        print(os.getcwd())
        with open("inventory.json", "r") as f:
            inventory = json.load(f)
            return inventory

async def setup(bot):
    await bot.add_cog(inventory(bot))