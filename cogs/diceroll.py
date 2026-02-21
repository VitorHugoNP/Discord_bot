import discord
import random
from discord import app_commands
from discord.ext import commands

class Diceroll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.command()
    async def roll(self, ctx, *, dice: str):

        try:
            dice = dice.lower().strip()

            # -------- turnos --------
            if "#" in dice:
                turns_part, expr = dice.split("#", 1)
                turns = int(turns_part) if turns_part else 1
            else:
                turns = 1
                expr = dice

            expr = expr.replace(" ", "")

            # 🔥 TRUQUE PRA SUPORTAR "-"
            expr = expr.replace("-", "+-")

            parts = expr.split("+")

            rolls_list = []
            bonus = 0

            # -------- parsing --------
            for part in parts:

                if not part:
                    continue

                # dado
                if "d" in part:

                    rolls_str, limit_str = part.split("d", 1)

                    # suporta d20 == 1d20
                    if rolls_str in ("", "+"):
                        rolls = 1
                    elif rolls_str == "-":
                        rolls = -1
                    else:
                        rolls = int(rolls_str)

                    limit = int(limit_str)

                    if rolls < 0:
                        raise ValueError

                    rolls_list.append((rolls, limit))

                # bonus numerico
                else:
                    bonus += int(part)

            if not rolls_list:
                raise ValueError

        except:
            await ctx.send(
                "Formato inválido.\n"
                "Exemplos válidos:\n"
                "`1d20`\n"
                "`2#1d20`\n"
                "`1d20+3`\n"
                "`1d20-2`\n"
                "`2#1d20+3-1+2d6`"
            )
            return

        # -------- execução --------

        await ctx.send(f"🎲 **Rolagem:** `{dice}`")

        global_fail = False

        for turno in range(1, turns + 1):

            results = []
            pure_results = []
            display = []

            for rolls, limit in rolls_list:

                for _ in range(rolls):

                    roll = random.randint(1, limit)
                    pure = roll

                    # sua regra de mau ágouro
                    if roll <= limit * 0.25:
                        if random.randint(1, 2) == 1:
                            roll = random.randint(1, limit)
                        else:
                            global_fail = True

                    pure_results.append(pure)
                    results.append(roll)

                    # destaque crítico
                    if roll == limit:
                        display.append(f"**{roll}**")
                    else:
                        display.append(str(roll))

            total = sum(results) + bonus
            sub = sum(pure_results) + bonus

            bonus_text = ""

            if bonus > 0:
                bonus_text = f" + {bonus}"
            elif bonus < 0:
                bonus_text = f" - {abs(bonus)}"

            await ctx.send(
                f"**Turno {turno}:** `{total}`\n"
                f"Resultados: [{', '.join(display)}]{bonus_text}\n"
                f"||Impuro: {sub} → {pure_results}{bonus_text}||"
            )

        if global_fail:
            await ctx.send("*‼️ Um forte mau ágouro foi jogado sobre um ou mais dados . . . ‼️*")

async def setup(bot):
    await bot.add_cog(Diceroll(bot))