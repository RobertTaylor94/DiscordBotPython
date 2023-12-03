from discord.ext import commands
from discord import app_commands, Embed, Interaction, ButtonStyle
from discord.ui import View, Button
from typing import Literal
from functions.user_data import UserData
from functions.roll import RollFunctions
import json
import os 
import random
import numpy as np

os.chdir('cogs/CustomRolls')

class custom_rolls(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.roll_functions = RollFunctions()

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
        custom_rolls = await self.get_custom_rolls()
        player_rolls = custom_rolls[str(interaction.user.id)]
        dice_to_roll = next((r for r in player_rolls if r['name'] == roll), None)
        user = UserData(interaction).get_user()

        if dice_to_roll['type'] == 'attack':
            attack_role = await self.roll_functions.roll_attack(dice_to_roll['atkbonus'], extraatk)
            em = Embed(title = f"{dice_to_roll['atkdice']} + {dice_to_roll['atkbonus']}\nTotal: {attack_role[1]}", description = f'{attack_role[0]}')
            em.set_author(name=f"{user.nick}'s {roll}", icon_url=user.avatar_url)
            view = View()
            dmg_button = self.damageButton(dice_to_roll['dmgdice'], dice_to_roll['dmgbonus'], extradmg, user)
            view.add_item(dmg_button)
            await interaction.response.send_message(embed=em, view=view)
        else:
            expression = f"{dice_to_roll['dice']}+{dice_to_roll['bonus']}"
            print(dice_to_roll['dice'])
            roll_total = await self.roll_functions.exp_roll(expression)
            em = Embed(title = f"{dice_to_roll['dice']} + {dice_to_roll['bonus']}\nTotal: {roll_total[2]}", description=f"{roll_total[0]}")
            em.set_author(name=f"{user.nick}'s {roll}", icon_url=user.avatar_url)
            await interaction.response.send_message(embed=em)

    @app_commands.command(name = 'delete_roll', description = 'Delete one of your custom rolls')
    @app_commands.describe(roll = 'The name of the roll to delete')
    async def delete_roll(self, interaction: Interaction, roll: str):
        custom_rolls = await self.get_custom_rolls()
        player_rolls = custom_rolls[str(interaction.user.id)]
        deleted_roll = roll
        values = []

        for item in player_rolls:
            values.append(item['name'])

        if deleted_roll in values:
            for i, item in enumerate(player_rolls):
                if player_rolls[i]['name'] == deleted_roll:
                    del player_rolls[i]
            await interaction.response.send_message(f"{deleted_roll} removed.")
        else:
            await interaction.response.send_message("roll not found")

        custom_rolls[str(interaction.user.id)] = player_rolls
        await self.save_rolls(custom_rolls)

    async def get_custom_rolls(self):
        os.chdir('../CustomRolls')
        with open('customRolls.json', 'r') as f:
            customRolls = json.load(f)
            return customRolls
        
    async def save_rolls(self, file):
        with open('customRolls.json', 'w') as f:
            json.dump(file, f)

    class damageButton(Button):
        def __init__(self, dmgdice, dmgbonus, extradmg, user):
            super().__init__(style = ButtonStyle.secondary, label = "Damage")
            self.dmgdice = dmgdice
            self.dmgbonus = dmgbonus
            self.extradmg = extradmg
            self.roll_functions = RollFunctions()
            self.user = user

        async def callback(self, interaction: Interaction):
            expression = f"{self.dmgdice} + {self.dmgbonus} + {self.extradmg}"
            result = await self.roll_functions.exp_roll(expression)
            rolls = result[0]
            bonus = result[1]
            total = result[2]

            em = Embed(title = f'{expression}\n**Total: {total}**', description=rolls)
            em.set_author(name=f"{self.user.nick}'s Damage", icon_url=self.user.avatar_url)
            await interaction.response.send_message(embed=em)

        async def roll(self, dice: int, sides: int):
            dice_array = []
            for i in range(0, dice):
                rand_num = random.randint(1, sides)
                dice_array.append(rand_num)
            return dice_array
                    
async def setup(bot):
    await bot.add_cog(custom_rolls(bot))