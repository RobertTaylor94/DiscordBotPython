import discord

class attackButton(discord.ui.Button):
    def __init__(self):
        super().__init__(style=discord.ButtonStyle.primary, label="Attack")
    
    async def callback(self, interaction: discord.Interaction):
        if interaction.user.name == 'murvoth':
            await interaction.response.send_message(f'Attack button pressed by {interaction.user.name}')
        else:
            await interaction.response.send_message(f'Attack button pressed by someone')