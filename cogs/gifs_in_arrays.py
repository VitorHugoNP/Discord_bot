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
            "https://tenor.com/view/apothecary-diaries-maomao-xiaolan-pat-pat-good-girl-gif-13334045917351786597",
            "https://tenor.com/view/pat-dinosaurs-plushies-gif-24417567",
            "https://tenor.com/view/pat-cat-pat-pat-gif-25250101",
            "https://tenor.com/view/pikachu-sadness-pet-head-caterpie-sad-gif-16792400",
            "https://tenor.com/view/%D8%AD%D8%B6%D9%86-%D8%A8%D9%88-gif-873756486592965272",
            "https://tenor.com/view/big-hero-six-big-hero6-cheer-up-comfort-baymax-gif-4215410",
            "https://tenor.com/view/head-pat-cat-cat-head-pat-cat-pat-kiki-gif-12035753500620958402",
            "https://tenor.com/view/hu-tao-lover-gif-10788586197618788122",
            "https://tenor.com/view/fern-cat-frieren-cat-frieren-anime-frieren-cat-petting-fern-cat-petting-gif-15066021529503890927",
            "https://tenor.com/view/hug-love-hi-bye-cat-gif-5711781834381685182",
            "https://tenor.com/view/frieren-pats-heither%27s-head-sousou-no-frieren-headpat-frieren-heither-gif-9445174606794519653",
            "https://tenor.com/view/the-apothecary-diaries-jinshi-maomao-gif-16911923218805411444"
        ]

        self.pragagif = [
            "https://cdn.discordapp.com/attachments/883839698970243072/1293715322083479632/togif-9-1.gif",
            "https://tenor.com/view/skeleton-mad-skeleton-gif-10886506202898815019",
            "https://tenor.com/view/goku-prowler-goku-goku-mad-goku-dbs-dbs-gif-11120329515669448575",
            "https://tenor.com/view/pibble-pibble-dog-pibble-gmail-gmail-dog-gmail-gif-1592494038181494840",
            "https://tenor.com/view/davy-jones-gameplayrj-dark-souls-gif-7318785129441002853",
            "https://tenor.com/view/ishowspeed-try-not-to-laugh-gif-7682731162751353849",
            "https://tenor.com/view/sybau-ts-pmo-gif-2102579015947246168",
            "https://tenor.com/view/strawberry-cat-domgcat-donkeycat-free-robux-vbucks-gif-9547401608137840178",
            "https://tenor.com/view/sunflower-pvz-singing-gif-17681690944762513733",
            "https://tenor.com/view/hollow-knight-zote-the-knight-gif-14177395",
            "https://tenor.com/view/shinji-ikari-gif-26168958",
            "https://tenor.com/view/cursed-random-mickey-mouse-gif-3326933426856018167",
            "https://tenor.com/view/spongebob-3bob-extra-eye-snail-eating-gif-13711041841154725027",
            "https://tenor.com/view/sad-kermit-kermit-the-frog-jump-off-gif-17801028",
            "https://tenor.com/view/eagle-gif-12032200364783936872",
            "https://tenor.com/view/cursed-goat-gif-6856262736279591755",
            "https://tenor.com/view/daicon-iii-bunny-girl-lightsaber-star-wars-darth-vader-gif-20742427",
            "https://tenor.com/view/gojo-jujutsu-kaisen-feet-gif-2332714932412147859",
            "https://tenor.com/view/ptojak-meme-bird-ptak-funnybird-gif-14816073084696890992",
            "https://tenor.com/view/speech-speech-bubble-bubble-fish-meme-gif-25115905",
            "https://tenor.com/view/xdzuiro-gif-21872932",
            "https://tenor.com/view/22-%D1%8B%D1%8B-gif-26660367",
            "https://tenor.com/view/sigmer-gif-1030637700133480791",
            "https://tenor.com/view/goku-piccolo-goku-kiss-dragon-ball-gif-13524722178893516531",
            "https://tenor.com/view/davy-jones-mago-dos-games-gameplayrj-provando-monster-de-cafe-contem-leite-entao-tem-leite-e-tem-oq-o-que-e-no-finalzinho-tem-um-negocinho-monster-com-cafe-gif-13402252620181522103",
            "https://tenor.com/view/davyjones-gameplayrj-dava-davadance-davy-jones-dan%C3%A7ando-gif-5732316184697138212",
            "https://tenor.com/view/frango-de-macumba-frango-macumba-jonatan-jonatan-santos-gif-8572306241937352801",
            "https://tenor.com/view/perro-macumba-perro-gif-11033550165526711587",
            "https://tenor.com/view/gyats-gif-13226811450218957859",
            "https://tenor.com/eANBklKLzNv.gif",
            "https://tenor.com/f576zV9tZd.gif",
            "https://tenor.com/view/yuimetal-gif-2236335851178412850",
            "https://tenor.com/view/burak-gif-4153398623157332309",
            "https://tenor.com/view/joker-joker-laugh-joker-laughing-joker-meme-gif-70796100678697647"
        ]

        self.botsadreact = [
            "https://tenor.com/view/bocchi-the-rock-anime-sad-gif-27615865",
            "https://tenor.com/view/hd-triste-sad-umaru-chan-gif-12703663354090997997",
            "https://tenor.com/view/anime-cry-crying-crying-girl-marin-kitagawa-my-dress-up-darling-gif-1018184038746649636",
            "https://tenor.com/view/crying-girl-anime-gif-1148332258033326155",
            "https://tenor.com/view/pokemon-pikachu-upset-sad-anime-gif-22961752",
            "https://tenor.com/view/anime-gif-1029519612558471852"
        ]
        
        self.punchgif = [
            "https://tenor.com/view/weliton-amogos-arzkeir-jujutsu-kaisen-panda-gif-20161414",
            "https://tenor.com/view/jujutsu-kaisen-nanami-kento-kento-friday-gif-27058744",
            "https://tenor.com/view/makima-maki-chs-chainsaw-man-reze-gif-2127323234004152026",
            "https://tenor.com/view/naoya-zenin-choso-fight-aura-farm-not-in-the-manga-gif-15215466617984430840",
            "https://tenor.com/view/naoya-zenin-punching-combo-fast-assault-gif-10811434377792099967",
            "https://tenor.com/view/jujutsu-kaisen-jjk-maki-maki-jjk-maki-zenin-gif-8736688734787472408",
            "https://tenor.com/view/espancando-o-boneco-batendo-no-pinto-puppet-chicken-beaten-gif-18376681",
            "https://tenor.com/view/triple-kick-itadori-itadori-vs-hanami-itadori-kicking-itadori-kicks-yuji-itadori-gif-26345536",
            "https://tenor.com/view/jujutsu-kaisen-yuji-itadori-hanami-black-flash-punch-gif-23773648",
            "https://tenor.com/view/maki-zenin-naoya-zenin-maki-naoya-maki-jjk-gif-6357792504434790394",
            "https://tenor.com/view/toji-jjk-jujutsu-kaisen-rabbit-kick-gif-8242498221806767486",
            "https://tenor.com/view/jujutsu-beatdown-jujutsu-kaisen-2v1-gif-19722418",
            "https://tenor.com/view/jjk-jujutsu-kaisen-jjk-fight-jujutsu-kaisen-fight-yuji-itadori-gif-13410355612590763521",
            "https://tenor.com/view/megumi-fushiguro-fushiguro-megumi-megumi-fushiguro-toji-fushiguro-gif-14764636942047131755",
            "https://tenor.com/view/jujutsu-kaisen-jjk-beatdown-anime-fight-jujutsu-gif-20535874"
            "https://tenor.com/view/gojo-satoru-fight-jujutsu-kaisen-gif-18532851"
        ]

    @commands.command()
    async def patpat(self, ctx, member: discord.Member):
        nickname = member.display_name

        if nickname != "Benzoe":
            await ctx.send(f"{nickname} recebeu carinho ❤️")
            await ctx.send(random.choice(self.patpatgif))
        else:
            await ctx.send("owwwn brigado ☆*: .｡. o(≧▽≦)o .｡.:*☆")
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
            await ctx.send(f"{nickname} tomou uma coça pesada")
            await ctx.send(random.choice(self.punchgif))
        else:
            await ctx.send("perdão mestre 🥺")
            await ctx.send(random.choice(self.botsadreact))
            
    @commands.command()
    async def poder(self, ctx):
        pode_ = random.randint(1,2)
        if pode_ == 1:
            await ctx.send("Pode")
        else:
            await ctx.send("Não Pode")
        
async def setup(bot):
    await bot.add_cog(Gifs_in_arrays(bot))