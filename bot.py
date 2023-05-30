import os
import random
import discord
import buttons
# from discord import ActionRow
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
    except Exception as e:
        print(e)

@bot.tree.command(name='roll', description="rolls a dice")
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    user = ctx.author
    dice = [
        str(random.choice(range(1, numberOfSides + 1)))
        for _ in range(numberOfDice)
    ]
    diceInt = []
    for i in dice:
        diceInt.append(int(i))
    sum = 0
    for i in diceInt:
        sum += i

    if user.id == 427116626446516224:
        await ctx.send(', '.join(dice))
        await ctx.send(sum)
    else:
        print(user.id)
        await ctx.send('who are you?')

@bot.tree.command(name='test')
async def test(ctx):
    button1 = buttons.attackButton()
    button2 = discord.ui.Button(style=discord.ButtonStyle.primary, label='Initiative', row=0, custom_id="init")

    view = discord.ui.View()

    view.add_item(button1)
    view.add_item(button2)

    await ctx.send("hello", view=view)

bot.run(TOKEN)