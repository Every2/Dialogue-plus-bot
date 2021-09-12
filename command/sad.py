from discord.ext import commands

class Sad(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
   

    @commands.command(name="sadyurina", help="Sad Yurina")
    async def sad_yurina(self, ctx):
        url_yurina="https://imgur.com/RD2aT24"
        await ctx.send (url_yurina)

   







                          


def setup(bot):
    bot.add_cog(Sad(bot))