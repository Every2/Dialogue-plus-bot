from discord.ext import commands

class Motivational(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name= "surrender", help="Don't surrender! Dialogue+ Will motivate you!")
    async def surrender(self, ctx):
        url = "https://imgur.com/64CtNXT"
        answer = "GANBATTE! GANBATTE! GANBATTE! "

        await ctx.send (answer)
        await ctx.send (url)
    
                     
def setup(bot):
    bot.add_cog(Motivational(bot))