import os
import random
import discord
import buttons
import rolls
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
   
    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(f'Server name: {guild.name}')

@bot.command(name="sync")
async def sync(ctx):
    try:
        synced = await bot.tree.sync()
        print(f'synced {len(synced)} command(s)')
        await ctx.send(f'synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

@bot.tree.command(name="test")
async def test(interaction: discord.Interaction):
    button1 = buttons.attackButton()
    button2 = buttons.aaronCharge()
    button3 = buttons.bubbleBeardHealing()

    view = discord.ui.View()

    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)

    await interaction.response.send_message("hello", view=view)

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


bot.run(TOKEN)