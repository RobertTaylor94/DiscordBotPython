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
            if "d100" in i:
                roll_array = i.split("d")
                if roll_array[0] == "":
                    roll_array.insert(0, "1")
                dice = int(roll_array[0])
                sides = int(roll_array[1])
                outcome = await self.roll(dice, sides)
                for i in outcome:
                    num_str = str(i)
                    big_num = num_str[0]+'0'
                    small_num = num_str[1]
                    img_array.append([int(big_num), 100])
                    img_array.append([int(small_num), 10])
                rolls = np.concatenate((rolls, outcome)).astype(int)
                print(rolls)
            elif "d" in i:
                roll_array = i.split("d")
                if roll_array[0] == "":
                    roll_array[0] = "1"
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