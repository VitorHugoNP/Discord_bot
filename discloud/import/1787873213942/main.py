import discord
from discord.ext import commands
import random
import os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).parent
COGS_DIR = BASE_DIR / "cogs"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

async def load_cogs():
    for arquivo in COGS_DIR.rglob("*.py"):
        if arquivo.name == "__init__.py":
            continue

        caminho_relativo = arquivo.relative_to(BASE_DIR).with_suffix("")
        extensao = ".".join(caminho_relativo.parts)

        await bot.load_extension(extensao)
            
@bot.event
async def on_ready():
    await load_cogs()
    await bot.tree.sync()
    print(f"Bot inicializado como {bot.user}")


@bot.command()
async def benzer(ctx):
    await ctx.send("✝️ O CHAT TA BENZIDO! ✝️")

TOKEN = config("TOKEN")
bot.run(TOKEN)