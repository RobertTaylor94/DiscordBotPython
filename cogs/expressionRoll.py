import random
from discord.ext import commands
from discord import app_commands, Interaction, Embed, File
import numpy as np
from functions.roll import RollFunctions
from functions.user_data import UserData
from functions.get_dice_img import stitch_dice_images

class expressionRoll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.roll_functions = RollFunctions()

    @app_commands.command(name='q', description='Roll a dice from an expression')
    @app_commands.describe(expression="expression", roll_type="rolling for")
    async def q(self, interaction: Interaction, expression: str, roll_type:str = ""):
        user = UserData(interaction).get_user()

        if roll_type != "":
            rolling = f"For {roll_type}"
        else:
            rolling = ""

        roll_total = await self.roll_functions.exp_roll(expression)
        total = roll_total[2]
        bonus = roll_total[1]
        rolls = roll_total[0]
        img_array = roll_total[3]

        stitch_dice_images(img_array, user.id)
        em1 = Embed(title=f'{expression}\n**Total: {total}**', color=user.color)
        em1.set_author(name=f"{user.nick} {rolling}", icon_url=user.avatar_url)

        file = File(f"/Users/robert/Desktop/DiscordBot/assets/{user.id}/stitched_image.png", filename="image.png")
        em1.set_image(url="attachment://image.png")
        await interaction.response.send_message(file=file, embed=em1, silent=True)
    
async def setup(bot):
    await bot.add_cog(expressionRoll(bot))


