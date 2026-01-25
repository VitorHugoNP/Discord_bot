import discord
import random
from discord import app_commands
from discord.ext import commands

class Diceroll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def roll(self, ctx, dice: str):
        try:
            dice = dice.lower().strip()

            if "#" in dice:
                turns_part, expr = dice.split("#", 1)
                turns = int(turns_part) if turns_part else 1
            else:
                turns = 1
                expr = dice

            expr = expr.replace(" ", "")

            rolls_list = []
            
            bonus = 0
            parts = expr.split("+")

            for part in parts:
                if not part:
                    continue

                if "d" in part:
                    rolls_str, limit_str = part.split("d", 1)
                    rolls = int(rolls_str) if rolls_str else 1
                    limit = int(limit_str)
                    rolls_list.append((rolls, limit))
                else:
                    bonus += int(part)

            if not rolls_list:
                raise ValueError

        except ValueError:
            await ctx.send(
                "Formato inválido.\n"
                "Exemplos válidos:\n"
                "`1d20`\n"
                "`2#1d20`\n"
                "`1d20+3`\n"
                "`2#1d20+3`\n"
                "`1d20+3+12d6`"
            )
            return

        await ctx.send(f"🎲 **Rolagem:** `{dice}`")

        for turno in range(1, turns + 1):
            results = []
            pure_results = []
            results_display = []
            fail = False

            for rolls, limit in rolls_list:
                for _ in range(rolls):
                    roll = random.randint(1, limit)
                    pure_results.append(roll)

                    if roll < limit * 0.25:
                        if random.randint(1, 2) == 1:
                            roll = random.randint(1, limit)
                        else:
                            fail = True

                    results.append(roll)
                
                
                if roll == limit:
                    results_display.append(f"**{roll}**")
                else:
                    results_display.append(str(roll))

            total = sum(results) + bonus
            sub = sum(pure_results) + bonus

            bonus_text = f" + {bonus}" if bonus > 0 else ""

            await ctx.send(
                f"**Turno {turno}:** `{total}`\n"
                f"Resultados: {results}{bonus_text}\n"
                f"||Impuro: {sub} → {pure_results}{bonus_text}||"
            )
        if fail == False:
            await ctx.send("*‼️ Um forte mau ágouro foi jogado sobre um ou mais dados . . . ‼️*")

async def setup(bot):
    await bot.add_cog(Diceroll(bot))