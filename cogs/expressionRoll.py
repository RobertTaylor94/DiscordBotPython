import random
from discord.ext import commands
from discord import app_commands, Interaction, Embed, File
import numpy as np
from functions.roll import RollFunctions
from functions.user_data import UserData
from functions.get_dice_img import GetDice

class expressionRoll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.roll_functions = RollFunctions()

    @app_commands.command(name='q', description='Roll a dice from an expression')
    @app_commands.describe(expression="expression", roll_type="rolling for")
    async def q(self, interaction: Interaction, expression: str, roll_type:str = ""):
        array = expression.split("+")
        # rolls = []
        # bonus = 0
        user = UserData(interaction).get_user()
        get_dice = GetDice()
        files = []
        embeds = []

        if roll_type != "":
            rolling = f"For {roll_type}"
        else:
            rolling = ""

        roll_total = await self.roll_functions.exp_roll(expression)

        total = roll_total[2]
        bonus = roll_total[1]
        rolls = roll_total[0]

        em1 = Embed(title=f'{expression}\n**Total: {total}**', description=f'{rolls}')
        em1.set_author(name=f"{user.nick} {rolling}", icon_url=user.avatar_url)
        # em1.set_image(url="https://i.imgur.com/0lU6puv.png")
        await interaction.response.send_message(embed=em1)
    
async def setup(bot):
    await bot.add_cog(expressionRoll(bot))
