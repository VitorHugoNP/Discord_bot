
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

@bot.event
async def on_ready():
    print("Bot inicializado com sucesso")
    
@bot.event
async def on_message(msg:discord.Message):
    if msg.author.bot:
        return
    elif msg.author.id == 485253736457961484:
        await msg.reply(f"Ken")
    
@bot.event
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel(1125942464545575036)
    await canal.send(f"Bem vindo ao nosso servidor {membro}")
    
@bot.command()
async def somar(ctx:commands.Context, num1:int, num2:int):
    resultado = num1 + num2
    await ctx.send(f"a soma entre {num1} e {num2} é: {resultado}")

bot.run("MTQ1OTIxNjk3OTI3MjUzNjMxOQ.GyUi3X._UcpNWd_LNCBa77f4s4VMxwmoRTGTMJ44CHDM4")