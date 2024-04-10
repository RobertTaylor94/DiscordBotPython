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
    # for filename in os.listdir('./cogs'):
    #     if filename.endswith('.py'):
    #         await bot.load_extension(f'cogs.{filename[:-3]}')
    # for filename in os.listdir('./cogs/Supplies'):
    #     if filename.endswith('.py'):
    #         await bot.load_extension(f'cogs.Supplies.{filename[:-3]}')
    # os.chdir('../../')
    # for filename in os.listdir('./cogs/Inventory'):
    #     if filename.endswith('.py'):
    #         await bot.load_extension(f'cogs.Inventory.{filename[:-3]}')
    # os.chdir('../../')
    # for filename in os.listdir('./cogs/CustomRolls'):
    #     if filename.endswith('.py'):
    #         await bot.load_extension(f'cogs.CustomRolls.{filename[:-3]}')
    project_root = os.path.abspath(os.path.dirname(__file__))
    cogs_path = os.path.join(project_root, "cogs")

    for filename in os.listdir(cogs_path):
        if filename.endswith('.py'):
            extension_path = f'cogs.{filename[:-3]}'
            print(f'added {filename}')

    for subdir in os.listdir(cogs_path):
        subdir_path = os.path.join(cogs_path, subdir)
        if os.path.isdir(subdir_path):
            for filename in os.listdir(subdir_path):
                if filename.endswith('.py'):
                    extension_path = f'cogs.{subdir}.{filename[:-3]}'
                    await bot.load_extension(extension_path)
                    print(filename)

async def main():
    await load()
    print("loaded all extensions")
    await bot.start(TOKEN)

asyncio.run(main())