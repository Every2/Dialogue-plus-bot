from discord.ext import commands
from decouple import config
import os 

bot = commands.Bot("!")

bot.load_extension('manager')

def load_cogs(bot):
    for files in os.listdir('command'):
        if files.endswith('.py'):
            cog = files[:-3]
            bot.load_extension(f'comandos.{cog}')
                        
    
load_cogs(bot)

consumer_key=config() 
consumer_secret=config() 
access_token_key=config() 
access_token_secret=config()  
teken = config()
bot.run() 