import discord
from discord.ext import commands
from run import bot, run
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

patpatgif = [
    "https://i.pinimg.com/originals/08/de/7a/08de7ad3dcac4e10d27b2c203841a99f.gif", "https://tenor.com/view/good-boy-pat-on-head-stitch-gif-6929366788372516752", "https://tenor.com/view/cat-black-cute-pat-pat-gif-15490955286723955595", "https://tenor.com/view/pat-garrys-mod-garrys-mod-physics-fast-intense-gif-26322619", "https://tenor.com/view/apothecary-diaries-maomao-xiaolan-pat-pat-good-girl-gif-13334045917351786597"
]

pragagif = [
    "https://cdn.discordapp.com/attachments/883839698970243072/1293715322083479632/togif-9-1.gif?ex=6972b148&is=69715fc8&hm=a4860d4abe3175e3dac028f0ae40567923d94b3b77d030f1582094b966af594a&", "https://tenor.com/view/skeleton-mad-skeleton-gif-10886506202898815019", "https://tenor.com/view/goku-prowler-goku-goku-mad-goku-dbs-dbs-gif-11120329515669448575", "https://tenor.com/view/pibble-pibble-dog-pibble-gmail-gmail-dog-gmail-gif-1592494038181494840", "https://tenor.com/view/davy-jones-gameplayrj-dark-souls-gif-7318785129441002853", "https://tenor.com/view/ishowspeed-try-not-to-laugh-gif-7682731162751353849", "https://tenor.com/view/sybau-ts-pmo-gif-2102579015947246168", "https://tenor.com/view/strawberry-cat-domgcat-donkeycat-free-robux-vbucks-gif-9547401608137840178"
]

botsadreact = [
    "https://tenor.com/view/bocchi-the-rock-anime-sad-gif-27615865", "https://tenor.com/view/hd-triste-sad-umaru-chan-gif-12703663354090997997", "https://tenor.com/view/anime-cry-crying-crying-girl-marin-kitagawa-my-dress-up-darling-gif-1018184038746649636"
]

@bot.event
async def on_ready():
    print(f"Bot inicializado como {bot.user}")

@bot.command()
async def benzer(ctx):
    await ctx.send("✝️ O CHAT TA BENZIDO! ✝️")

@bot.command()
async def patpat(ctx, member: discord.Member):
    nickname = member.display_name
    if nickname != "Benzoe":
        await ctx.send(f"{nickname} recebeu carinho❤️")
        await ctx.send(patpatgif[random.randint(0, 4)])
    else:
        await ctx.send("owwwn brigado :3")
        await ctx.send(patpatgif[random.randint(0, 4)])

@bot.command()
async def praga(ctx, member: discord.Member):
    nickname = member.display_name
    if nickname != "Benzoe":
        await ctx.send(f"{nickname} caiu em uma terrivel maldição 💀")
        await ctx.send(pragagif[random.randint(0, 7)])
    else:
        await ctx.send("perdão mestre 🥺")
        await ctx.send(botsadreact[random.randint(0,2)])
@bot.command()
async def roll(ctx, dice: str):
    try:
        dice = dice.lower()

        # Turnos
        if "#" in dice:
            turns_part, dice_part = dice.split("#")
            turns = int(turns_part)
        else:
            dice_part = dice
            turns = 1

        # Bônus
        if "+" in dice_part:
            dice_core, bonus_part = dice_part.split("+")
            bonus = int(bonus_part)
        else:
            dice_core = dice_part
            bonus = 0

        # Dados
        rolls_str, limit_str = dice_core.split("d")
        rolls = int(rolls_str)
        limit = int(limit_str)

    except ValueError:
        await ctx.send(
            "Use o formato correto:\n"
            "`.roll 2d6`\n"
            "`.roll 2d6+3`\n"
            "`.roll 2#2d6`\n"
            "`.roll 2#2d6+5`"
        )
        return

    await ctx.send(f"🎲 **Rolagem:** `{dice}`")

    for turno in range(1, turns + 1):
        results = []
        pure_results = []

        for _ in range(rolls):
            roll = random.randint(1, limit)
            pure_results.append(roll)

            # Mecânica dos 25%
            if roll < limit * 0.25:
                chance = random.randint(1, 2)
                if chance == 1:
                    roll = random.randint(1, limit)
                else:
                    await ctx.send(
                        "*‼️ Uma mágica Maligna foi jogada sobre este dado... "
                        "Não foi possivel abençoá-la 😭*"
                    )

            results.append(roll)

        total = sum(results) + bonus
        sub = sum(pure_results) + bonus

        bonus_text = f" + {bonus}" if bonus > 0 else ""
        await ctx.send(
            f" `{total}` <— Resultados: {results} {bonus_text}\n" 
            f"|| {sub} <— Resultados Impuros: {pure_results} {bonus_text}||"
        )

bot.run("MTQ1OTIxNjk3OTI3MjUzNjMxOQ.GJIy73.pBGZOUN5NU_bkJXPnoFKe4YyclCSwWTH4Nb-lE")

# if __name__ == "__main__":
#     run()