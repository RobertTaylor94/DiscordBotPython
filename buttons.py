import discord
import random

class attackButton(discord.ui.Button):
    def __init__(self):
        super().__init__(style=discord.ButtonStyle.primary, label="Attack")
    
    async def callback(self, interaction: discord.Interaction):
        if interaction.user.name == 'murvoth':
            roll = int(random.choice(range(1, 20)))
            total= str(roll+15)
            view = discord.ui.View()
            view.add_item(rollDamage())
            embed = discord.Embed(color=1, title="Attack by Murvoth", description=f'{roll} + 15 = {total}', type='rich')
            await interaction.response.send_message(view=view, embed=embed)
        else:
            await interaction.response.send_message(f'Attack button pressed by someone')

