import random
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    print("Bot inicializado com sucesso")
    
@bot.command()
async def benzer(ctx):
    await ctx.send("✝️ O CHAT TA BENZIDO! ✝️")
    
        
@bot.command()
async def roll(ctx, dice: str, turns = 1):
    try:
        rolls, limit = dice.lower().split("d")
        rolls = int(rolls)
        limit = int(limit)

        if rolls > 100:
            await ctx.send("Máximo de 100 dados por vez.")
            return

    except ValueError:
        await ctx.send(f"Use o formato correto: `{bot.intents}roll 2d6`")
        return

    results = []
    
    for _ in range(rolls):
        roll = random.randint(1, limit)
        
        if roll < 10:
            await ctx.send("o resultado foi algourado, benzendo... ")
            chance = random.randint(1, 2)
            if chance == 1:
                roll = random.randint(1, limit)
                await ctx.send("A benção foi dada 🛐")
            else:
                await ctx.send("Uma mágia maligna foi jogada sobre este dado... não foi possivel benzer 😭")
        
        results.append(roll)
    
        
        
    
    total = sum(results)

    await ctx.send(
        f"🎲 **Rolagem:** `{dice}`\n"
        f"Resultados: {results}\n"
        f"**Total:** {total}"
    )

bot.run("MTQ1OTIxNjk3OTI3MjUzNjMxOQ.GyUi3X._UcpNWd_LNCBa77f4s4VMxwmoRTGTMJ44CHDM4")