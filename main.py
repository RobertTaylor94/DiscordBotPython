import os
import random
import discord
import buttons
import rolls
import asyncio
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start(TOKEN)

@bot.tree.command(name="r", description="roll dice")
@app_commands.describe(expression="expression")
async def r(interaction: discord.Interaction, expression: str):
    array = expression.split("d")
    num_of_dice = array[0]
    num_of_sides = array[1]

    print(num_of_dice, num_of_sides)

    if '+' in num_of_sides:
        split = num_of_sides.split("+")
        sides = int(split[0])
        bonus = int(split[1])
        dice = int(num_of_dice)
        embed = rolls.roll(sides=sides, dice=dice, bonus=bonus, user=interaction.user.name)
        await interaction.response.send_message(embed=embed)
    else:
        dice = int(num_of_dice)
        sides = int(num_of_sides)
        embed = rolls.roll(sides=sides, dice=dice, user=interaction.user.name)
        await interaction.response.send_message(embed=embed)


asyncio.run(main())