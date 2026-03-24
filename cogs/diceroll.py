import discord
import random
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
import asyncio

MAX_WORKERS = 10  # 🔥 limite de threads
MAX_TURNS = 100   # 🔥 proteção contra flood

class Diceroll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

    @commands.command()
    async def roll(self, ctx, *, dice: str):

        try:
            dice = dice.lower().strip()

            if "#" in dice:
                turns_part, expr = dice.split("#", 1)
                turns = int(turns_part) if turns_part else 1
            else:
                turns = 1
                expr = dice

            # 🔥 proteção contra flood
            if turns > MAX_TURNS:
                await ctx.send(f"⚠️ Máximo de turnos permitido: {MAX_TURNS}")
                return

            expr = expr.replace(" ", "")
            expr = expr.replace("-", "+-")
            parts = expr.split("+")

            rolls_list = []
            bonus = 0

            for part in parts:

                if not part:
                    continue

                if "d" in part:
                    rolls_str, limit_str = part.split("d", 1)

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

                else:
                    bonus += int(part)

            if not rolls_list:
                raise ValueError

        except:
            await ctx.send("Formato inválido.")
            return

        await ctx.send(f"🎲 **Rolagem:** `{dice}`")

        global_fail = False

        # 🔧 função que roda na thread
        def roll_turn(turno):
            nonlocal global_fail

            results = []
            pure_results = []
            display = []
            local_fail = False

            for rolls, limit in rolls_list:
                for _ in range(rolls):
                    roll = random.randint(1, limit)
                    pure = roll

                    if roll <= limit * 0.25:
                        if random.randint(1, 2) == 1:
                            roll = random.randint(1, limit)
                        else:
                            local_fail = True

                    pure_results.append(pure)
                    results.append(roll)

                    if roll == limit:
                        display.append(f"**{roll}**")
                    else:
                        display.append(str(roll))

            total = sum(results) + bonus
            sub = sum(pure_results) + bonus

            return {
                "turno": turno,
                "text": (
                    f"**Turno {turno}:** `{total}`\n"
                    f"Resultados: [{', '.join(display)}]\n"
                    f"||Impuro: {sub} → {pure_results}||"
                ),
                "fail": local_fail
            }

        loop = asyncio.get_running_loop()

        # 🔥 executa no pool de threads (controlado)
        tasks = [
            loop.run_in_executor(self.executor, roll_turn, turno)
            for turno in range(1, turns + 1)
        ]

        results = await asyncio.gather(*tasks)

        # 📤 envio ordenado
        results.sort(key=lambda x: x["turno"])

        for r in results:
            if r["fail"]:
                global_fail = True
            await ctx.send(r["text"])

        if global_fail:
            await ctx.send("*‼️ Mau ágouro ocorreu... ‼️*")


async def setup(bot):
    await bot.add_cog(Diceroll(bot))