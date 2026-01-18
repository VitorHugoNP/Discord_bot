import discord
from discord.ext import commands
from run import bot, run
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot inicializado como {bot.user}")
    
@bot.command()
async def benzer(ctx):
    await ctx.send("✝️ O CHAT TA BENZIDO! ✝️")
    
@bot.command()
async def patpat(ctx, member: discord.Member):
    nickname = member.display_name
    await ctx.send(f"{nickname} recebeu carinho")
    await ctx.send("https://i.pinimg.com/originals/08/de/7a/08de7ad3dcac4e10d27b2c203841a99f.gif")
    
@bot.command()
async def roll(ctx, dice: str):
    try:
        if "#" in dice:
            turns, dice_part = dice.lower().split("#")
            turns = int(turns)
            rolls_str, limit_str = dice_part.lower().split("d")
        else:
            rolls_str,limit_str = dice.lower().split("d")
            turns = int(1)
        rolls = int(rolls_str)
        limit = int(limit_str)

    except ValueError:
        await ctx.send(f"Use o formato correto (EXEMPLO: `.roll 2d6` ou `.roll 2#2d6`)")
        return

    
    await ctx.send(f"🎲 Rolagem: {dice}\n")
    for turno in range(1, turns + 1):
        results = []
        pure_results = []
        
        for _ in range(rolls):
            roll = random.randint(1, limit)
            await ctx.send(f"Rolagem pura: {roll}\n")
            pure_results.append(roll)
            if roll < limit * 0.25:
                chance = random.randint(1, 2)
                if chance == 1:
                    roll = random.randint(1, limit)
                else:
                    await ctx.send("* ‼️ Uma mágica Maligna foi jogada sobre este dado... Não foi possivel abençoa-la 😭 *")
            results.append(roll)
    
        total = sum(results)
        sub = sum(pure_results)

        await ctx.send(
                f" `{total}` <— Resultados: {results} \n" 
                f"|| {sub} <— Resultados Impuros: {pure_results} ||"
            )

bot.run("MTQ1OTIxNjk3OTI3MjUzNjMxOQ.GJIy73.pBGZOUN5NU_bkJXPnoFKe4YyclCSwWTH4Nb-lE")

# if __name__ == "__main__":
#     run()