import discord
import random
from discord import app_commands
from discord.ext import commands

class Jokenpo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    
    @commands.command()
    async def jokenpo(self, ctx):
        choices = {
            1: "🪨 Pedra",
            2: "📄 Papel",
            3: "✂️ Tesoura"
        }

        choice = random.randint(1, 3)

        await ctx.send(
            f"{ctx.author.mention} escolheu **{choices[choice]}**"
        )
    
async def setup(bot):
    await bot.add_cog(Jokenpo(bot))