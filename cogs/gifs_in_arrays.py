import discord
import random
from discord import app_commands
from discord.ext import commands


# setup
class Gifs_in_arrays(commands.Cog):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

        self.patpatgif = [
            "https://i.pinimg.com/originals/08/de/7a/08de7ad3dcac4e10d27b2c203841a99f.gif",
            "https://tenor.com/view/good-boy-pat-on-head-stitch-gif-6929366788372516752",
            "https://tenor.com/view/cat-black-cute-pat-pat-gif-15490955286723955595",
            "https://tenor.com/view/pat-garrys-mod-garrys-mod-physics-fast-intense-gif-26322619",
            "https://tenor.com/view/apothecary-diaries-maomao-xiaolan-pat-pat-good-girl-gif-13334045917351786597"
        ]

        self.pragagif = [
            "https://cdn.discordapp.com/attachments/883839698970243072/1293715322083479632/togif-9-1.gif",
            "https://tenor.com/view/skeleton-mad-skeleton-gif-10886506202898815019",
            "https://tenor.com/view/goku-prowler-goku-goku-mad-goku-dbs-dbs-gif-11120329515669448575",
            "https://tenor.com/view/pibble-pibble-dog-pibble-gmail-gmail-dog-gmail-gif-1592494038181494840",
            "https://tenor.com/view/davy-jones-gameplayrj-dark-souls-gif-7318785129441002853",
            "https://tenor.com/view/ishowspeed-try-not-to-laugh-gif-7682731162751353849",
            "https://tenor.com/view/sybau-ts-pmo-gif-2102579015947246168",
            "https://tenor.com/view/strawberry-cat-domgcat-donkeycat-free-robux-vbucks-gif-9547401608137840178"
        ]

        self.botsadreact = [
            "https://tenor.com/view/bocchi-the-rock-anime-sad-gif-27615865",
            "https://tenor.com/view/hd-triste-sad-umaru-chan-gif-12703663354090997997",
            "https://tenor.com/view/anime-cry-crying-crying-girl-marin-kitagawa-my-dress-up-darling-gif-1018184038746649636"
        ]
        
        self.punchgif = [
            "https://tenor.com/view/weliton-amogos-arzkeir-jujutsu-kaisen-panda-gif-20161414",
            "https://tenor.com/view/jujutsu-kaisen-nanami-kento-kento-friday-gif-27058744",
            "https://tenor.com/view/makima-maki-chs-chainsaw-man-reze-gif-2127323234004152026",
            "https://tenor.com/view/naoya-zenin-choso-fight-aura-farm-not-in-the-manga-gif-15215466617984430840",
            "https://tenor.com/view/naoya-zenin-punching-combo-fast-assault-gif-10811434377792099967",
            "https://tenor.com/view/jujutsu-kaisen-jjk-maki-maki-jjk-maki-zenin-gif-8736688734787472408"
        ]

    @commands.command()
    async def patpat(self, ctx, member: discord.Member):
        nickname = member.display_name

        if nickname != "Benzoe":
            await ctx.send(f"{nickname} recebeu carinho ❤️")
            await ctx.send(random.choice(self.patpatgif))
        else:
            await ctx.send("owwwn brigado :3")
            await ctx.send(random.choice(self.patpatgif))
    
    @commands.command()
    async def praga(self, ctx, member: discord.Member):
        nickname = member.display_name
        if nickname != "Benzoe":
            await ctx.send(f"{nickname} caiu em uma terrivel maldição 💀")
            await ctx.send(random.choice(self.pragagif))
        else:
            await ctx.send("perdão mestre 🥺")
            await ctx.send(random.choice(self.botsadreact))
        
    @commands.command()
    async def punch(self, ctx, member: discord.Member):
        nickname = member.display_name
        
        if nickname != "Benzoe":
            await ctx.send(f"{nickname} foi esmurrado sem dó")
            await ctx.send(random.choice(self.punchgif))
        else:
            await ctx.send("perdão mestre 🥺")
            await ctx.send(random.choice(self.botsadreact))
        
async def setup(bot):
    await bot.add_cog(Gifs_in_arrays(bot))