import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

# guild = client.guilds

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
   
    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(guild.name)

@bot.command(name='roll', help='Rolls a dice')
async def roll(ctx, numberOfDice: int, numberOfSides: int):
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

    await ctx.send(', '.join(dice))
    await ctx.send(sum)

bot.run(TOKEN)