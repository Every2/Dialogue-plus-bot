from discord.ext import commands
import tweepy
import asyncio
from decouple import config
class Manager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
            print (f"I'm Ready! {self.bot.user}")
           
            

            
            
            users_id = ['DIALOGUE_staff','uchiyama_yurina', 'miyamiya_Satsu', 'kyoka_moriya', 'takamura_ayaka', 'iizuka_mayu', 'nene_hieda']

            last_ids = {

                }
        

            
                
                    
            for i in users_id:
                    last_ids[i] = 0


            auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
            auth.set_access_token(access_token_key,access_token_secret)
            api = tweepy.API(auth)
            
            
            
            
            


            while True:
                
                

                    for user in users_id:
                        print('Waiting')
                        await asyncio.sleep(15)
                

                        cursor=tweepy.Cursor(api.user_timeline,id=user, tweet_mode="extended",).items(1)
                        channel = self.bot.get_channel()
                    
                    
                        for i in cursor:
                        
                            if i.id != last_ids[user]:
                            
                            
            
                                a = i.id
                                last_ids[user] = a

            
                                await channel.send(f'New Tweets!!! https://twitter.com/user/status/{a}')
    
    
consumer_key=config('') 
consumer_secret=config('') 
access_token_key=config('') 
access_token_secret=config('') 


def setup(bot):
    bot.add_cog(Manager(bot))
