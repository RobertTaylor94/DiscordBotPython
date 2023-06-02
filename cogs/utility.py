import discord
from discord.ext import commands

class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(ctx):
        print(f'We have logged in as {ctx.bot.user}')

    @commands.command()
    async def sync(self, ctx):
        print('syncing...')
        synced = await ctx.bot.tree.sync()
        print(f'Synced {len(synced)} commands')
        await ctx.send(f'Synced {len(synced)} commands')

async def setup(bot):
    await bot.add_cog(utility(bot))