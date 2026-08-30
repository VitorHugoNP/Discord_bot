from discord.ext import commands


class ErrorHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.CommandNotFound):
            await ctx.send(
                "❌ Comando inexistente. Verifique se você digitou corretamente."
            )

        elif isinstance(error, commands.BadArgument):
            await ctx.send(
                "❌ Argumento inválido. Verifique o que você digitou."
            )

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                "❌ Está faltando algum argumento."
            )


async def setup(bot):
    await bot.add_cog(ErrorHandler(bot))