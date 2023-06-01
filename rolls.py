import random
from discord import Embed

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