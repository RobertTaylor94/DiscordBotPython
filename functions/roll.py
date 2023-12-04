import random
import numpy as np

class RollFunctions:
    def __init__(self):
        pass
    
    async def roll(self, dice: int, sides: int):
        dice_array = []
        for i in range(0, dice):
            rand_num = random.randint(1, sides)
            dice_array.append(rand_num)
        return dice_array

    async def roll_attack(self, bonus, extra):
        roll = int(random.choice(range(1, 21)))
        roll_total = str(roll+bonus+extra)
        return [roll, roll_total]

    async def exp_roll(self, expression):
        array = expression.split("+")
        bonus = 0
        rolls = []
        img_array = []
        for i in array:
            if "d" in i:
                roll_array = i.split("d")
                dice = int(roll_array[0])
                sides = int(roll_array[1])
                outcome = await self.roll(dice, sides)
                for i in outcome:
                    img_array.append([i, sides])
                rolls = np.concatenate((rolls, outcome)).astype(int)
            else:
                bonus += int(i)
        total = sum(rolls)
        total += bonus
        return [rolls, bonus, total, img_array]