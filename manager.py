from discord.ext import commands
import tweepy
import asyncio
from decouple import config
import psycopg2
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

load_dotenv()
class Manager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    


    @commands.Cog.listener()
    async def on_ready(self):
            print (f"I'm ready {self.bot.user}")
            
            
            result = urlparse(os.getenv("DATABASE_URL"))

            DB_USER = result.username
            DB_PASSWORD = result.password
            DB_NAME = result.path[1:]
            DB_HOST = result.hostname
            DB_PORT = result.port
            
            




            con = psycopg2.connect(dbname=DB_NAME, user=DB_USER, host=DB_HOST, password=DB_PASSWORD, port=DB_PORT)
            cur = con.cursor() 
                     
            cur.execute("SELECT id_idol FROM idols;")
            tuples_array = cur.fetchall()
            con.commit()
            users_id = [ID for ID, in tuples_array]         
               
            
            
            last_ids = {

                }

            for idol_id in users_id:
                last_ids [idol_id] = []

            cur.execute("SELECT * FROM twitter;")
            con.commit()
            all_posts = cur.fetchall()    
            for idol_id, post_id in all_posts:
                idol_posts = last_ids.get(idol_id)
                if idol_posts:
                    last_ids[idol_id].append(post_id)
                else:
                    last_ids [idol_id] = [post_id]
                
                    
           


            auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
            auth.set_access_token(access_token_key,access_token_secret)
            api = tweepy.API(auth)
            
            
            
            
            


            while True:
                
                

                    for user in users_id:
                        print('Waiting')
                        await asyncio.sleep(3)
                

                        cursor=tweepy.Cursor(api.user_timeline,id=user, tweet_mode="extended",).items(1)
                        channel = self.bot.get_channel()
                    
                    
                        for i in cursor:
                        
                            if not str (i.id) in last_ids[user]:
                            
                            
                                
                                a = str (i.id)
                                
                                
                                
                                cur.execute("INSERT INTO twitter VALUES (%s, %s);", (user,a))         
                                con.commit()   
                                
                                last_ids[user].append(a)
                                

            
                                await channel.send(f'New post! https://twitter.com/{user}/status/{a}')
   
            con.close()
  
consumer_key=config('') 
consumer_secret=config('') 
access_token_key=config('') 
access_token_secret=config('') 


def setup(bot):
    bot.add_cog(Manager(bot))
