from discord.ext import commands

class Talk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name= "best", help="Avoid arguments about who is the best girl")
    async def best_girl(self, ctx):
        answer = "They're all the best " 

        await ctx.send (answer)


    @commands.command(name= "members", help="Members of group")
    async def members_group(self, ctx):
        answer = "The members are " + "Ayaka Takamura, " + "Kyoka Moriya, " + "Mayu Iizuka, " + "Manatsu Murakami, " + "Nene Hieda , "+ "Satsuki Miyahara, " + "Yuna Ogata " + "e Yurina Uchiyama."

        await ctx.send (answer)
    

    @commands.command(name= "rule", help="The rule that must always be followed")
    async def rule(self, ctx):
        answer = "Idols are for giving love, not for thinking lewd things!"
        await ctx.send (answer)



def setup(bot):
    bot.add_cog(Talk(bot))