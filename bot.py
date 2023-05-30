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
        synced = await bot.tree.sync(guild=discord.Object(id=1108491843873804418))
        print(f'synced {len(synced)} command(s)')
        await ctx.send(f'synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

@bot.tree.command(name='roll', description="rolls a dice")
@app_commands.describe(number_of_sides="The number of sides of the dice", d="The number of dice to roll")
async def roll(interaction: discord.Interaction, number_of_sides: int, d: int):
    user = interaction.user
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(d)
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

    view = discord.ui.View()

    view.add_item(button1)

    await interaction.response.send_message("hello", view=view, ephemeral= True)




bot.run(TOKEN)