from discord.ext import commands
from discord import app_commands, Interaction, Embed

class inventory(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='')

    @app_commands.command(name='food', description='Manage food and water supplies')
    @app_commands.describe(food='food', drink='drink')
    async def food(self, interaction: Interaction, food: int, drink: int):
        prev_food = 0
        prev_drink = 0
        new_food = prev_food + food
        new_drink = prev_drink + drink

        embed = Embed(type='rich', title='Rations', description=f'{prev_food} + {food} = {new_food}\n{prev_drink} + {drink} = {new_drink}')
        interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(inventory(bot))