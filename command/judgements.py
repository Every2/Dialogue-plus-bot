from discord.ext import commands

class Judgements(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
  

    @commands.command(name="neneagree", help="Thumbsup Nene")
    async def joinha_nene(self, ctx):
        url_nene="https://imgur.com/pXFFG1r"
        await ctx.send (url_nene)

  


    @commands.command(name="ogatadisagree", help="Ogata disagree about your comment")
    async def discordo_ogata(self, ctx):
        url_ogata="https://imgur.com/S4vJiLv"
        await ctx.send (url_ogata)

    

    @commands.command(name="silenceyuna", help="Make silence")
    async def silence(self, ctx):
        url_yuna="https://imgur.com/rSah1Bj"
        await ctx.send (url_yuna)


    @commands.command(name="yurinyaagree", help="Thumbsup Yurinya")
    async def silence(self, ctx):
        url_yurinya="https://imgur.com/a/ml785wl"
        await ctx.send (url_yurinya)






                          


def setup(bot):
    bot.add_cog(Judgements(bot))
