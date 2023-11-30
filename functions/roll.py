import random

async def roll(dice: int, sides: int):
        dice_array = []
        for i in range(0, dice):
            rand_num = random.randint(1, sides)
            dice_array.append(rand_num)
        return dice_array