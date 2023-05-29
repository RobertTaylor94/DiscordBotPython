import os
import random
import discord
import buttons
# from discord import ActionRow
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

    

@bot.command(name='roll', help='Rolls a dice')
async def roll(ctx, numberOfDice: int, numberOfSides: int):
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

@bot.command(name='test')
async def test(ctx):
    button1 = buttons.attackButton()
    button2 = discord.ui.Button(style=discord.ButtonStyle.primary, label='Initiative', row=0, custom_id="init")

    view = discord.ui.View()

    view.add_item(button1)
    view.add_item(button2)

    await ctx.send("hello", view=view)

@bot.event
async def on_button_click(interaction):
    await interaction.respond(content="Button Clicked")

bot.run(TOKEN)