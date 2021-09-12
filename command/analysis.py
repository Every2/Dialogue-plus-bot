from discord.ext import commands

class Analysis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
   
    

    @commands.command(name="analisemanat", help="Manatsu Murakami thinking")
    async def manat_analise(self, ctx):
        url_manat="https://imgur.com/yJUIMLr"
        await ctx.send (url_manat)
        
    @commands.command(name="analiseyuna", help="Yuna thinking")
    async def yuna_analise(self, ctx):
        url_yuna="https://imgur.com/yJUIMLr"
        await ctx.send (url_yuna)
    


    

    @commands.command(name="sappyanalise", help="Miyamiya thinking")    
    async def miyamiya(self, ctx):
        url="https://imgur.com/a/L1di9ZJ"
        await ctx.send (url)

    

    @commands.command(name="analiseyurina", help="Yurina thinking")
    async def yurinaanalise(self, ctx):
        url="https://imgur.com/fexZjBh"
        await ctx.send (url)

    @commands.command(name="analisemayu", help="Mayu thinking")
    async def mayunalise(self, ctx):
        url="https://imgur.com/tP3S5io"
        await ctx.send (url)    





    @commands.command(name="analisenene", help="Nene thinking")
    async def analisenene(self, ctx):
        url="https://imgur.com/t9jUXCE"
        await ctx.send (url)    

    @commands.command(name="analisekyoka", help="Kyoka thinking")
    async def analisekyoka(self, ctx):
        url="https://imgur.com/qJvowON"
        await ctx.send (url)

    @commands.command(name="analiseayaka", help="Ayaka thinking")
    async def analiseayaka(self, ctx):
        url="https://imgur.com/raUQwBp"
        await ctx.send (url)

  







                          


def setup(bot):
    bot.add_cog(Analysis(bot))