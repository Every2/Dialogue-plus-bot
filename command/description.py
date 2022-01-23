from discord.ext import commands
import discord

class description(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name= "nene", help="description")
    async def nene(self, ctx):
        url_nene="https://cdn.discordapp.com/attachments/885246211446165526/886360338117820537/E8_825WXEAAQ3tS.png"
        
        embed_image = discord.Embed(
            title="NENE",
            description="Name: Nene Hieda \n Nickname: Nene \n Height: 1,53",
            color= 16776960,
        )

        embed_image.set_image(url=url_nene)
        
        await ctx.send (embed=embed_image) 

    
    @commands.command(name= "yakan", help="description")
    async def yakan(self, ctx):
        url_yakan="https://cdn.discordapp.com/attachments/882315038189289492/885270930983641229/E9ep75HVgAYpY16.jpeg"
        
        embed_image = discord.Embed(
            title="Yakan",
            description="Name: Ayaka Takamura \n Nickname: Yakan \n Height: 1,50",
            color= 11027200,
        )

        embed_image.set_image(url=url_yakan)
        
        await ctx.send (embed=embed_image)  
    
    @commands.command(name= "mayuyun", help="description")
    async def mayuyun(self, ctx):
        url_mayuyun="https://cdn.discordapp.com/attachments/882315038189289492/885268246364844053/E9ACsrYXoAkuAT4.jpeg"
        
        embed_image = discord.Embed(
            title="Mayuyun",
            description="Name: Mayu Iizuka \n Nickname: Mayuyun \n Height: 1,53",
            color= 2123412,
        )

        embed_image.set_image(url=url_mayuyun)
        
        await ctx.send (embed=embed_image)     

    @commands.command(name= "sappy", help="description")
    async def sappy(self, ctx):
        url_sappy="https://cdn.discordapp.com/attachments/885246211446165526/934605920057577582/EtT2gcFUUAMXlG-.png"
        
        embed_image = discord.Embed(
            title="Sappy",
            description="Name: Satsuki Miyahara \n Nickname: Sappy \n Height: 1,58",
            color= 15158332,
        )

        embed_image.set_image(url=url_sappy)
        
        await ctx.send (embed=embed_image)     


    @commands.command(name= "kyon", help="description")
    async def kyon(self, ctx):
        url_kyon="https://cdn.discordapp.com/attachments/882315038189289492/885272530225619004/E78mPquUUAcQkf8.jpeg"
        
        embed_image = discord.Embed(
            title="Kyon",
            description="Name: Kyoka Moriya \n Nickname: Kyon \n Height: 1,50",
            color= 5763719,
        )

        embed_image.set_image(url=url_kyon)
        
        await ctx.send (embed=embed_image)

    @commands.command(name= "yurinya", help="description")
    async def yurinya(self, ctx):
        url_yurinya="https://cdn.discordapp.com/attachments/882315038189289492/885263975674150932/E8_y2c9WUBU2WB0.jpeg"
        
        embed_image = discord.Embed(
            title="Yurinya",
            description="Name: Yurina Uchiyama \n Nickname: Yurinya \n Height: 1,58",
            color= 11342935,
        )

        embed_image.set_image(url=url_yurinya)
    
        await ctx.send (embed=embed_image)


    @commands.command(name= "yuna", help="description")
    async def yuna(self, ctx):
        url_yuna="https://cdn.discordapp.com/attachments/882315038189289492/885261640369590272/E81RAd4VgAAMaXA.jpeg"
        
        embed_image = discord.Embed(
            title="Yuna",
            description="Name: Yuna Ogata \n Nickname: Yuna \n Height: 1,61",
            color= 3447003,
        )

        embed_image.set_image(url=url_yuna)
        
        await ctx.send (embed=embed_image) 

    @commands.command(name= "manat", help="description")
    async def manat(self, ctx):
        url_mana="https://cdn.discordapp.com/attachments/882315038189289492/885257026773602334/E8_d1VVUUAYHcTk.jpeg"
        
        embed_image = discord.Embed(
            title="Mana-T",
            description="Name: Manatsu Murakami \n Nickname: Mana-T \n Height: 1,57",
            color= 7419530,
        )

        embed_image.set_image(url=url_mana)
        
        await ctx.send (embed=embed_image) 

   




     


                              

def setup(bot):
    bot.add_cog(description(bot))
