import os
import random
import discord
import buttons
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

@bot.tree.command(name='roll', description="rolls a dice")
@app_commands.describe(number_of_sides="The number of sides of the dice", number_of_dice="The number of dice to roll")
async def roll(interaction: discord.Interaction, number_of_sides: int, number_of_dice: int):
    user = interaction.user
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for number_of_sides in range(number_of_dice)
    ]
    diceInt = []
    for i in dice:
        diceInt.append(int(i))
    sum = 0
    for i in diceInt:
        sum += i

    rolls = ', '.join(dice)

    if user.id == 427116626446516224:
        await interaction.response.send_message(f'{rolls}\nTotal: {sum}')

    else:
        print(user.id)
        await interaction.response.send_message('who are you?')

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

    if num_of_dice.isdigit() and num_of_sides.isdigit():
        dice = int(num_of_dice)
        sides = int(num_of_sides)

        dice_array = []

        for i in range(dice):
            random_number = random.randint(1, sides)
            dice_array.append(random_number)
        
        print(dice_array)

        sum = 0

        for i in dice_array:
            sum += i

        embed = discord.Embed(title=f'Roll', type='rich', description=f'{dice_array}\nTotal: {sum}')

        await interaction.response.send_message(f'Murvoth', embed=embed)


bot.run(TOKEN)