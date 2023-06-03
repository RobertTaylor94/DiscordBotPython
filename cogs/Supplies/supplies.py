from discord.ext import commands
from discord import app_commands, Embed, Interaction
import json
import os 

os.chdir('cogs/Supplies')

class supplies(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='supplies', description='Check the food and drink supplies held on the ship')
    async def supplies(self, interaction: Interaction):
        print('supplies called...')
        supplies = await self.get_supplies()
        print('supplies loaded')

        food_amt = supplies[str('food')]
        drink_amt = supplies[str('drink')]

        embed = Embed(type='rich', title='Ship Supplies')
        embed.add_field(name='Food', value=food_amt)
        embed.add_field(name='Drink', value=drink_amt)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name='update_supplies', description='Add food and drink to the rations')
    @app_commands.describe(food='food', drink='drink')
    async def update(self, interaction: Interaction, food: int, drink: int):
        supplies = await self.get_supplies()
        old_food = supplies[str('food')]
        old_drink = supplies[str('drink')]
        new_food = old_food + food
        new_drink = old_drink + drink

        supplies[str('food')] = new_food
        supplies[str('drink')] = new_drink

        with open("supplies.json", "w") as f:
            json.dump(supplies, f)
            print('json saved')

        embed = Embed(title='Updated Supplies')
        embed.add_field(name='Food', value=supplies[str('food')])
        embed.add_field(name='Drink', value=supplies[str('drink')])
        await interaction.response.send_message(embed=embed)

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
            print(supplies)
            return supplies

async def setup(bot):
    await bot.add_cog(inventory(bot))