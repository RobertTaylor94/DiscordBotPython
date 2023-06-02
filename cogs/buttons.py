import discord
import random
from discord.ext import commands
from discord import app_commands

class buttons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='button', description='Display commonly used rolls as buttons')
    async def button(self, interaction: discord.Interaction):
        print("button command issued")
        view = buttonsView()
        await interaction.response.send_message("hello", view=view, ephemeral = True)

class buttonsView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(attackButton())
        self.add_item(aaronCharge())
        self.add_item(bubbleBeardHealing())

class attackButton(discord.ui.Button):
    def __init__(self):
        super().__init__(style=discord.ButtonStyle.primary, label="Attack")
    
    async def callback(self, interaction: discord.Interaction):
        if interaction.user.name == 'murvoth':
            roll = int(random.choice(range(1, 21)))
            total= str(roll+15)
            view = discord.ui.View()
            view.add_item(rollDamage())
            embed = discord.Embed(color=1, title=f'Attack by {interaction.user.name}', description=f'{roll} + 15 = {total}', type='rich')
            await interaction.response.send_message(view=view, embed=embed)
        else:
            await interaction.response.send_message(f'Attack button pressed by someone')

class rollDamage(discord.ui.Button):
    def __init__(self):
        super().__init__(style=discord.ButtonStyle.secondary, label="Roll Damage")

    async def callback(self, interaction: discord.Interaction):
        if interaction.user.name == 'murvoth':
            roll1 = int(random.choice(range(1, 11)))
            roll2 = int(random.choice(range(1, 5)))
            total = str(roll1 + roll2 + 5)
            embed = discord.Embed(color=2, title=f'Damage by {interaction.user.name}', description=f'{roll1} + {roll2} + 5 = {total}', type='rich')
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message('Damage be damaging')

class aaronCharge(discord.ui.Button):
    def __init__(self):
        super().__init__(style=discord.ButtonStyle.primary, label="Aaron Charge")

    async def callback(self, interaction: discord.Interaction):
        roll1 = int(random.choice(range(1, 21)))
        total = str(roll1 + 18)
        embed = discord.Embed(type='rich', title="Aaron's Charge", description=f'{roll1} + 18\n{total}')
        await interaction.response.send_message(embed=embed)

class bubbleBeardHealing(discord.ui.Button):
    def __init__(self):
        super().__init__(style=discord.ButtonStyle.success, label="Bubble Beard Healing")

    async def callback(self, interaction: discord.Interaction):
        array = []
        total = 0
        for i in range(0, 6):
            roll = int(random.choice(range(1,7)))
            array.append(roll)
        
        for i in array:
            total += i

        embed = discord.Embed(type='rich', title="Bubble Beard Healing", description=f'{array}\nTotal: {total}')
        
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(buttons(bot))