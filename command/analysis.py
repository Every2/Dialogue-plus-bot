from discord.ext import commands

class Analysis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
   
    

    @commands.command(name="analysisemanat", help="Manatsu Murakami thinking")
    async def manat_analise(self, ctx):
        url_manat="https://imgur.com/yS1dVaO"
        await ctx.send (url_manat)
        
    @commands.command(name="analysisyuna", help="Yuna thinking")
    async def yuna_analise(self, ctx):
        url_yuna="https://imgur.com/mdcxJhK"
        await ctx.send (url_yuna)
    


    

    @commands.command(name="sappyanalysis", help="Miyamiya thinking")    
    async def miyamiya(self, ctx):
        url="https://imgur.com/a/L1di9ZJ"
        await ctx.send (url)

    

    @commands.command(name="analysisyurina", help="Yurina thinking")
    async def yurinaanalise(self, ctx):
        url="https://imgur.com/fexZjBh"
        await ctx.send (url)

    @commands.command(name="analysismayu", help="Mayu thinking")
    async def mayunalise(self, ctx):
        url="https://imgur.com/tP3S5io"
        await ctx.send (url)    





    @commands.command(name="analysisnene", help="Nene thinking")
    async def analisenene(self, ctx):
        url="https://imgur.com/t9jUXCE"
        await ctx.send (url)    

    @commands.command(name="analysiskyoka", help="Kyoka thinking")
    async def analisekyoka(self, ctx):
        url="https://imgur.com/qJvowON"
        await ctx.send (url)

    @commands.command(name="analysisayaka", help="Ayaka thinking")
    async def analiseayaka(self, ctx):
        url="https://imgur.com/raUQwBp"
        await ctx.send (url)

  







                          


def setup(bot):
    bot.add_cog(Analysis(bot))
