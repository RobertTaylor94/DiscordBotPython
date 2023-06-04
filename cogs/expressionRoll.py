import random
from discord.ext import commands
from discord import app_commands, Interaction, Embed
import numpy as np

class expressionRoll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='r', description='Roll a dice from an expression')
    @app_commands.describe(expression="expression")
    async def r(self, interaction: Interaction, expression: str):
        array = expression.split("+")
        rolls = []
        bonus = 0

        for i in array:
            if "d" in i:
                roll_array = i.split("d")
                dice = int(roll_array[0])
                sides = int(roll_array[1])
                outcome = await self.roll(dice, sides)
                rolls = np.concatenate((rolls, outcome)).astype(int)
            else:
                bonus += int(i)
        total = sum(rolls)
        total += bonus
        em = Embed(title=interaction.user.name, description = f'{rolls} + {bonus}\n**Total: {total}**')
        await interaction.response.send_message(embed=em)
    
    async def roll(self, dice: int, sides: int):
        dice_array = []
        for i in range(0, dice):
            rand_num = random.randint(1, sides)
            dice_array.append(rand_num)
        return dice_array
    
async def setup(bot):
    await bot.add_cog(expressionRoll(bot))