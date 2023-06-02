import random
from discord.ext import commands
from discord import app_commands, Interaction, Embed

class expressionRoll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='r', description='Roll a dice from an expression')
    @app_commands.describe(expression="expression")
    async def r(self, interaction: Interaction, expression: str):
        array = expression.split("d")
        num_of_dice = array[0]
        num_of_sides = array[1]

        print(num_of_dice, num_of_sides)

        if '+' in num_of_sides:
            split = num_of_sides.split("+")
            sides = int(split[0])
            bonus = int(split[1])
            dice = int(num_of_dice)
            embed = roll(sides=sides, dice=dice, bonus=bonus, user=interaction.user.name)
            await interaction.response.send_message(embed=embed)
        else:
            dice = int(num_of_dice)
            sides = int(num_of_sides)
            embed = roll(sides=sides, dice=dice, user=interaction.user.name)
            await interaction.response.send_message(embed=embed)

class diceRoll(object):
    global roll
    def roll(sides: int, dice: int, user, bonus = 0):
        dice_array = []
        sum = 0

        for i in range(0, dice):
            rand_num = random.randint(1, sides)
            dice_array.append(rand_num)
        for i in dice_array:
            sum += i
        sum += bonus

        embed = Embed(type='rich', title=f'{user}', description=f'{dice_array} + {bonus}\nTotal: {sum + bonus}')
        return embed
    
async def setup(bot):
    await bot.add_cog(expressionRoll(bot))