from discord.ext import commands


class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
   

    @commands.command(name="demonayaka", help="Ayaka dressed as a devil")
    async def demonayaka(self, ctx):
        url_ayakademon="https://imgur.com/Uxx2mcx"
        await ctx.send (url_ayakademon)

    

    @commands.command(name="ogatarun", help="Yuna running")
    async def ogata_run(self, ctx):
        url_ogata="https://imgur.com/lS02rN9"
        await ctx.send (url_ogata)

    

    @commands.command(name="demonsappy", help="Sappy dressed as a devil")
    async def demon_sappy(self, ctx):
        url_sappy="https://imgur.com/Cm87OK5"
        await ctx.send (url_sappy)
    
    @commands.command(name="angrysappy", help="Angry sappy")
    async def angry_sappy(self, ctx):
        url_sappy="https://imgur.com/AfnFFoc"
        await ctx.send (url_sappy)
    
    @commands.command(name="kyokapunch", help="Kyoka hit you")
    async def kyoka_punch(self, ctx):
        url_sappy="https://imgur.com/mmOBSq9"
        await ctx.send (url_sappy)

                      
def setup(bot):
    bot.add_cog(Meme(bot))
