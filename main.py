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
        turns, dice_part = dice.lower().split("#")
        turns = int(turns)
        
        rolls_str, limit_str = dice_part.lower().split("d")
        rolls = int(rolls_str)
        limit = int(limit_str)

    except ValueError:
        await ctx.send(f"Use o formato correto: `{bot.intents}roll 2d6`")
        return

    
    await ctx.send(f"🎲 Rolagem: {dice}\n")
    for turno in range(1, turns + 1):
        results = []
        pure_results = []
        
        for _ in range(rolls):
            roll = random.randint(1, limit)
            ctx.send(f"Rolagem pura: {roll}\n")
            pure_results.append(roll)
            if roll < limit * 0.25:
                chance = random.randint(1, 2)
                if chance == 1:
                    roll = random.randint(1, limit)
                else:
                    await ctx.send("‼️ Uma mágica Maligna foi jogada sobre este dado... Não foi possivel abençoa-la 😭")
            results.append(roll)
    
        total = sum(results)
        sub = sum(pure_results)

        await ctx.send(
                f" `{total}` <— Resultados: {results} \n" 
                f"|| {sub} <— Resultados Impuros: {pure_results} ||"
            )

bot.run("MTQ1OTIxNjk3OTI3MjUzNjMxOQ.GyUi3X._UcpNWd_LNCBa77f4s4VMxwmoRTGTMJ44CHDM4")