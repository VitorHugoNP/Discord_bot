import discord
from discord.ext import commands
import random
import os
intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

async def load_cogs():
    for arquivo in os.listdir('cogs'):
        if arquivo.endswith('.py'):
            await bot.load_extension(f"cogs.{arquivo[:-3]}")
            
@bot.event
async def on_ready():
    await load_cogs()
    await bot.tree.sync()
    print(f"Bot inicializado como {bot.user}")

@bot.command()
async def benzer(ctx):
    await ctx.send("✝️ O CHAT TA BENZIDO! ✝️")

bot.run("MTQ1OTIxNjk3OTI3MjUzNjMxOQ.GJIy73.pBGZOUN5NU_bkJXPnoFKe4YyclCSwWTH4Nb-lE")

# if __name__ == "__main__":
#     run()