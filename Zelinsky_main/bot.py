import os 
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from datetime import timedelta
from groq import Groq

load_dotenv()
TOKEN = os.getenv("TOKEN")
Api_key = os.getenv("groq_api_key")

print("TOKEN loaded:", TOKEN is not None)
print("Groq loaded:", Api_key is not None)
print('initializing bot..')

client = Groq(api_key = Api_key)


# Intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('!', '?','zam'),
    intents=intents
)


@bot.event
async def on_ready():
    print(f'Bot is online as {bot.user}')

# Message handler
@bot.event
async def on_message(message):
    if message.author == bot.user:
        
        return

    
    

    
    if "zam" in message.content:
        prompt = message.content[len("zam"):]
        
        try:

            chat = client.chat.completion.create(
                model="llama-3.1-8b-instant",
                
                message= [
                    {
                        "role": "system",
                        "content": (
                            'you are a real human chatting on discord you speak naturally like a delhi boy'
                            'use short sentences and occassional slangs  or gen z slangs sometimes'
                            'you have senses and emotions like humans'
                            'dont sound too robotic or overly formal'
                            'dont mention that you are ai you are zammy"s pet '
                        ) #bakchodi ki adat 
                    },
                        {"role": "user", "content": prompt
                        }
                ]
             )

            reply = chat.choices[0].message.content
            await message.channel.send(reply)
            return
        except Exception as e:
            await message.channel.send("❌error gettin genai key")
            print(e)

        

    await bot.process_commands(message)

# Startup
async def main():
    async with bot:
        await bot.load_extension("cogs.roleplay")
        await bot.load_extension("cogs.role_changing")
        await bot.load_extension("cogs.moderation")
        await bot.start(TOKEN)

if TOKEN:
    asyncio.run(main())
else:
    print("❌ TOKEN missing")