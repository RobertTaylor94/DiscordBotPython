import random
from discord.ext import commands
from discord import app_commands, Interaction, Embed
import numpy as np
from functions.roll import roll
class expressionRoll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='q', description='Roll a dice from an expression')
    @app_commands.describe(expression="expression", roll_type="rolling for")
    async def q(self, interaction: Interaction, expression: str, roll_type:str = ""):
        array = expression.split("+")
        rolls = []
        bonus = 0

        if roll_type != "":
            rolling = f"For {roll_type}"
        else:
            rolling = ""

        for i in array:
            if "d" in i:
                roll_array = i.split("d")
                dice = int(roll_array[0])
                sides = int(roll_array[1])
                print('about to call roll...')
                outcome = await roll(dice, sides)
                rolls = np.concatenate((rolls, outcome)).astype(int)
            else:
                bonus += int(i)
        total = sum(rolls)
        total += bonus
        em = Embed(title=f'{interaction.user.nick} {rolling}', description = f'{rolls} + {bonus}\n**Total: {total}**')
        await interaction.response.send_message(embed=em)
    
async def setup(bot):
    await bot.add_cog(expressionRoll(bot))