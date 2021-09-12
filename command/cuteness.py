from discord.ext import commands

class Cuteness(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
   

    @commands.command(name="cutesappy", help="Sappy being cute")
    async def cute_sappy(self, ctx):
        url_sappy="https://imgur.com/muUJZVM"
        await ctx.send (url_sappy)
    

    @commands.command(name="cutemayu", help="Mayu being cute")
    async def cute_mayu(self, ctx):
        url_mayu="https://imgur.com/0OfsD5a"
        await ctx.send (url_mayu)
    
    @commands.command(name="cutemanat", help="Manatsu Murakami being cute")
    async def cute_manat(self, ctx):
        url_manat="https://imgur.com/mWSVyrm"
        await ctx.send (url_manat)
    

   
    


    @commands.command(name="cutenene", help="Nene being cute")
    async def nene_cute(self, ctx):
        url_nene="https://imgur.com/a/iFed2IE"
        await ctx.send (url_nene)

   



    
  
 

    @commands.command(name="cutekyoka", help="Kyoka being cute")
    async def kyoka_cute(self, ctx):
        url_kyoka="https://imgur.com/csNSpfQ"
        await ctx.send (url_kyoka)

  

    

    @commands.command(name="cuteyuna", help="Yuna being cute")
    async def yuna_cute(self, ctx):
        url_nene="https://imgur.com/DGniApB"
        await ctx.send (url_nene)

    
    

    @commands.command(name="cuteyurina", help="Yurina being cute")
    async def cute_yurina(self, ctx):
        url_yurina="https://imgur.com/mhr6bXr"
        await ctx.send (url_yurina)

   

    @commands.command(name="cuteayaka", help="Ayaka being cute")
    async def cute_ayaka(self, ctx):
        url_ayaka="https://imgur.com/hy5Fxh1"
        await ctx.send (url_ayaka)

                    

def setup(bot):
    bot.add_cog(Cuteness(bot))