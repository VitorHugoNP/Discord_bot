import discord
import random
from discord import app_commands
from discord.ext import commands

class Diceroll(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        
    @commands.command()
    async def roll(self, ctx, dice: str):
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

async def setup(bot):
    await bot.add_cog(Diceroll(bot))