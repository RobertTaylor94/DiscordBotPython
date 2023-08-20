import os
import discord
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
    for filename in os.listdir('./cogs/Supplies'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.Supplies.{filename[:-3]}')
    os.chdir('../../')
    for filename in os.listdir('./cogs/Inventory'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.Inventory.{filename[:-3]}')
    os.chdir('../../')
    for filename in os.listdir('./cogs/CustomRolls'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.CustomRolls.{filename[:-3]}')
    os.chdir('../../')
    for filename in os.listdir('./cogs/Character'):
        if filename.endswith('n.py'):
            await bot.load_extension(f'cogs.Character.{filename[:-3]}')

async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())