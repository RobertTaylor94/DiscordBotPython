from discord.ext import commands
from discord import app_commands, Embed, Interaction, ButtonStyle
from discord.ui import View, Button
from typing import Literal
import json
import os 
import random
import numpy as np

os.chdir('cogs/CustomRolls')

class custom_rolls(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name = 'add_roll', description = 'Add a custom attack roll to your character')
    @app_commands.describe(name = 'name', type = 'type of roll', atkbonus = 'your attack bonus', dmgdice = 'your damage dice (e.g. 1d10 + 1d4)', dmgbonus = 'your damage bonus', dice = 'dice to roll', bonus = 'bonus to the roll')
    async def add_role(self, interaction: Interaction, name: str, type: Literal['attack', 'other'], atkbonus: int = 0, dmgdice: str = '', dmgbonus: int = 0, atkdice: str = '1d20', dice: str = '1d20', bonus: int = 0):
        custom_rolls = await self.get_custom_rolls()
        player_rolls = custom_rolls[str(interaction.user.id)]
        roll_type = type
        em = Embed(title = "New Role")

        if roll_type == 'attack':
            new_role = {'name': name, 'atkbonus': atkbonus, 'dmgdice': dmgdice, 'dmgbonus': dmgbonus, 'atkdice': atkdice, 'type': type}
            player_rolls.append(new_role)
            em.add_field(name = name, value = f'Attack Bonus: {atkbonus}\nDamage: {dmgdice} + {dmgbonus}\nType: {type}')
        if roll_type == 'other':
            new_role = {'name': name, 'dice': dice, 'bonus': bonus, 'type': type}
            player_rolls.append(new_role)
            em.add_field(name = name, value = f'Roll: {dice} + {bonus}')

        custom_rolls[str(interaction.user.id)] = player_rolls
        await self.save_rolls(custom_rolls)
        await interaction.response.send_message(embed = em, ephemeral = True)

    @app_commands.command(name = 'check_rolls', description = 'Check your custom rolls')
    async def check_rolls(self, interaction: Interaction):
        custom_rolls = await self.get_custom_rolls()
        em = Embed(title = f"{interaction.user.name}'s Custom Rolls")
        if str(interaction.user.id) not in custom_rolls:
            custom_rolls[str(interaction.user.id)] = []
            await self.save_rolls(custom_rolls)
        else:
            user_rolls = custom_rolls[str(interaction.user.id)]
            for roll in user_rolls:
                print(roll)
                if roll['type'] == 'attack':
                    em.add_field(name = roll['name'], value = f'Attack Bonus: {roll["atkbonus"]}\nDamage: {roll["dmgdice"]} + {roll["dmgbonus"]}\nType: {roll["type"]}')
                else:
                    em.add_field(name = roll['name'], value = f'Roll: {roll["dice"]} + {roll["bonus"]}')

        await interaction.response.send_message(embed=em, ephemeral=True)

    @app_commands.command(name = 'cr', description = 'Roll one of your custom rolls')
    @app_commands.describe(roll = 'the name of your roll', extraatk = 'extra bonus to attack rolls', extradmg = 'extra bonus to damage', extra = 'extra bonus to other roll')
    async def cr(self, interaction: Interaction, roll: str, extraatk: int = 0, extradmg: int = 0, extra: int = 0):
        print("rolling custom roll")
        custom_rolls = await self.get_custom_rolls()
        player_rolls = custom_rolls[str(interaction.user.id)]
        print('got rolls...finding your roll')
        dice_to_roll = next((r for r in player_rolls if r['name'] == roll), None)
        if dice_to_roll['type'] == 'attack':
            roll_total = await self.roll(dice_to_roll['atkbonus'], extraatk)
            em = Embed(title = f"{interaction.user.name}'s {dice_to_roll['name']} Attack", description = f'{roll_total[0]} + {(dice_to_roll["atkbonus"]+extraatk)} = **{roll_total[1]}**')
            view = View()
            dmg_button = self.damageButton(dice_to_roll['dmgdice'], dice_to_roll['dmgbonus'], extradmg)
            view.add_item(dmg_button)
            await interaction.response.send_message(embed=em, view=view)
        else:
            roll_total = await self.roll(dice_to_roll['bonus'], extra)
            em = Embed(title = f"{interaction.user.name}'s {dice_to_roll['name']}", description = f'{roll_total[0]} + {[dice_to_roll["bonus"] + extra]} = **{roll_total[1]}**')
            await interaction.response.send_message(embed=em)

    @app_commands.command(name = 'delete_roll', description = 'Delete one of your custom rolls')
    @app_commands.describe(roll = 'The name of the roll to delete')
    async def delete_roll(self, interaction: Interaction, roll: str):
        print('deleting roll...')
        custom_rolls = await self.get_custom_rolls()
        player_roles = custom_rolls[str(interaction.user.id)]
        deleted_roll = roll
        for i, item in enumerate(player_roles):
            if player_roles[i]['name'] == deleted_roll:
                del player_roles[i]
            else:
                print('roll not found')
                await interaction.response.send_message("roll not found")
        custom_rolls[str(interaction.user.id)] = player_roles
        await self.save_rolls(custom_rolls)

        em = Embed(title = f"{interaction.user.name}'s Rolls")
        for roll in player_roles:
            if roll['type'] == 'attack':
                em.add_field(name = roll['name'])
            else:
                em.add_field(name = roll['name'])
        await interaction.response.send_message(embed=em, ephemeral=True)

    async def get_custom_rolls(self):
        print('getting custom rolls...')
        os.chdir('../CustomRolls')
        with open('customRolls.json', 'r') as f:
            customRolls = json.load(f)
            return customRolls
        
    async def save_rolls(self, file):
        with open('customRolls.json', 'w') as f:
            json.dump(file, f)
            print('json saved')

    async def roll(self, bonus, extra):
        print('roll_attack called')
        roll = int(random.choice(range(1, 21)))
        roll_total = str(roll+bonus+extra)
        return (roll, roll_total)

    class damageButton(Button):
        def __init__(self, dmgdice, dmgbonus, extradmg):
            super().__init__(style = ButtonStyle.secondary, label = "Damage")
            self.dmgdice = dmgdice
            self.dmgbonus = dmgbonus
            self.extradmg = extradmg

        async def callback(self, interaction: Interaction):
            print('rolling damage')
            array = self.dmgdice.split('+')
            rolls = []
            bonus = self.dmgbonus
            extradmg = self.extradmg
            for i in array:
                roll_array = i.split('d')
                dice = int(roll_array[0])
                sides = int(roll_array[1])
                outcome = await self.roll(dice, sides)
                rolls = np.concatenate((rolls, outcome)).astype(int)
            total = sum(rolls)
            total = total + bonus + extradmg
            em = Embed(title = f"{interaction.user.name}'s Damage", description = f'{rolls} + {bonus} + {extradmg}\n**Total: {total}**')
            await interaction.response.send_message(embed=em)

        async def roll(self, dice: int, sides: int):
            dice_array = []
            for i in range(0, dice):
                rand_num = random.randint(1, sides)
                dice_array.append(rand_num)
            return dice_array
                    
async def setup(bot):
    await bot.add_cog(custom_rolls(bot))