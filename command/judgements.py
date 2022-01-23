from discord.ext import commands

class Judgements(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
  

    @commands.command(name="neneagree", help="Thumbsup Nene")
    async def thumbsup_nene(self, ctx):
        url_nene="https://imgur.com/pXFFG1r"
        await ctx.send (url_nene)

  


    @commands.command(name="ogatadisagree", help="Ogata disagree about your comment")
    async def disagree_ogata(self, ctx):
        url_ogata="https://imgur.com/S4vJiLv"
        await ctx.send (url_ogata)

    

    @commands.command(name="silenceyuna", help="Make silence")
    async def silence(self, ctx):
        url_yuna="https://imgur.com/rSah1Bj"
        await ctx.send (url_yuna)


    @commands.command(name="yurinyaagree", help="Thumbsup Yurinya")
    async def Yurinya(self, ctx):
        url_yurinya="https://imgur.com/a/ml785wl"
        await ctx.send (url_yurinya)
   

    @commands.command(name="sappyagree", help="Thumbsup Sappy")
    async def sappyt(self, ctx):
        url_sappy="https://imgur.com/exZLyxM"
        await ctx.send (url_sappy)

    @commands.command(name="sappydisagree", help="Sappy disagree")
    async def sappy(self, ctx):
        url_sappyd="https://imgur.com/Ii6FiFJ"
        await ctx.send (url_sappyd)
        
    






                          


def setup(bot):
    bot.add_cog(Judgements(bot))
