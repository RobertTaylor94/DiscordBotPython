import random
from discord.ext import commands
from discord import app_commands, Interaction, Embed, ButtonStyle
from discord.ui import View, Button

class buttons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='b', description='Display commonly used rolls as buttons')
    async def b(self, interaction: Interaction):
        view = buttonsView()
        await interaction.response.send_message(view=view, ephemeral = True)

class buttonsView(View):
    def __init__(self):
        super().__init__()
        # self.add_item(attackButton())
        # self.add_item(aaronCharge())
        # self.add_item(bubbleBeardHealing())
        self.add_item(d12Button())
        self.add_item(d100Button())

class d12Button(Button):
    def __init__(self):
        super().__init__(style=ButtonStyle.secondary, label="d12")

    async def callback(self, interaction: Interaction):
        roll = int(random.choice(range(1, 13)))
        embed = Embed(title=f'{interaction.user.nick}', description=f'{roll}', type='rich')
        await interaction.response.send_message(embed=embed)

class d100Button(Button):
    def __init__(self):
        super().__init__(style= ButtonStyle.secondary, label="Percentile")

    async def callback(self, interaction: Interaction):
        roll = int(random.choice(range(1, 101)))
        embed = Embed(title=f'{interaction.user.nick}', description=f'{roll}', type='rich')
        await interaction.response.send_message(embed=embed)

class attackButton(Button):
    def __init__(self):
        super().__init__(style= ButtonStyle.primary, label="Attack")
    
    async def callback(self, interaction: Interaction):
        if interaction.user.name == 'murvoth':
            roll = int(random.choice(range(1, 21)))
            total= str(roll+15)
            view = View()
            view.add_item(rollDamage())
            embed = Embed(color=1, title=f'Attack by {interaction.user.nick}', description=f'{roll} + 15 = {total}', type='rich')
            await interaction.response.send_message(view=view, embed=embed)
        else:
            await interaction.response.send_message(f'Attack button pressed by someone')

class rollDamage(Button):
    def __init__(self):
        super().__init__(style = ButtonStyle.secondary, label="Roll Damage")

    async def callback(self, interaction: Interaction):
        if interaction.user.name == 'murvoth':
            roll1 = int(random.choice(range(1, 11)))
            roll2 = int(random.choice(range(1, 5)))
            total = str(roll1 + roll2 + 5)
            embed = Embed(color=2, title=f'Damage by {interaction.user.nick}', description=f'{roll1} + {roll2} + 5 = {total}', type='rich')
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message('Damage be damaging')

class aaronCharge(Button):
    def __init__(self):
        super().__init__(style=ButtonStyle.primary, label="Aaron Charge")

    async def callback(self, interaction: Interaction):
        roll1 = int(random.choice(range(1, 21)))
        total = str(roll1 + 18)
        embed = Embed(type='rich', title="Aaron's Charge", description=f'{roll1} + 18\n{total}')
        view = buttonsView()
        await interaction.response.send_message(embed=embed)

class bubbleBeardHealing(Button):
    def __init__(self):
        super().__init__(style=ButtonStyle.success, label="Bubble Beard Healing")

    async def callback(self, interaction: Interaction):
        array = []
        total = 0
        for i in range(0, 6):
            roll = int(random.choice(range(1,7)))
            array.append(roll)
        
        for i in array:
            total += i

        embed = Embed(type='rich', title="Bubble Beard Healing", description=f'{array}\nTotal: {total}')
        view = buttonsView()
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(buttons(bot))