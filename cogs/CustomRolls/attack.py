from discord.ext import commands
from discord import app_commands, Embed, Interaction
from typing import Literal
import json
import os 

os.chdir('cogs/CustomRolls')

class create_attack(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name = 'create_attack', description = 'Add a custom attack roll to your character')
    @app_commands.describe(name = 'name', atkbonus = 'atkbonus', dmgdice = 'dmgdice (e.g. 1d10 + 1d4)', dmgbonus = 'dmgbonus')
    async def create_attack(self, interaction: Interaction, name: str, atkbonus: int, dmgdice: str, dmgbonus: int, atkdice: str = '1d20', type: str = 'attack'):
        print('running create_attack')
        custom_rolls = await self.get_custom_rolls()
        player_rolls = custom_rolls[str(interaction.user.id)]

        new_role = {'name': name, 'atkbonus': atkbonus, 'dmgdice': dmgdice, 'dmgbonus': dmgbonus, 'atkdice': atkdice, 'type': type}
        player_rolls.append(new_role)

        custom_rolls[str(interaction.user.id)] = player_rolls
        await self.save_rolls(custom_rolls)

        em = Embed(title = "New Role")
        em.add_field(name = name, value = f'Attack Bonus: {atkbonus}\nDamage: {dmgdice} + {dmgbonus}\nType: {type}')
        await interaction.response.send_message(embed = em, ephemeral = True)

    @app_commands.command(name = 'check_rolls', description = 'Check your custom rolls')
    async def check_rolls(self, interaction: Interaction):
        print('checking user rolls...')
        custom_rolls = await self.get_custom_rolls()
        em = Embed(title = f"{interaction.user.name}'s Custom Rolls")
        if str(interaction.user.id) not in custom_rolls:
            custom_rolls[str(interaction.user.id)] = []
            await self.save_rolls(custom_rolls)
        else:
            user_rolls = custom_rolls[str(interaction.user.id)]
            for roll in user_rolls:
                type = roll['type']
                print(type)
                match type:
                    case 'attack':
                        print(roll['name'], roll['atkbonus'])
                    case _:
                        print('no types found')

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

async def setup(bot):
    await bot.add_cog(create_attack(bot))