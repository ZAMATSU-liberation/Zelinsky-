import discord
import random
from discord.ext import commands
from datetime import timedelta,time 

class Roleplay(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    # Hug
    @commands.command()
    async def hug(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send(f"{ctx.author.mention}, who do you want to hug? 🤔")
        else:
            gifs = [
                "https://media.tenor.com/ZQ-gLvxHdL8AAAAC/hug-anime.gif",
                "https://media.tenor.com/2gP9nHZJzAEAAAAC/anime-hug.gif"
            ]
            await ctx.send(f"{ctx.author.mention} gives {member.mention} a warm hug! 🤗\n{random.choice(gifs)}")

    # Kiss
    @commands.command()
    async def kiss(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send(f"{ctx.author.mention}, you need someone to kiss!:kiss:")
        else:
            gifs = [
                "https://media.tenor.com/0AVbKGY_MxMAAAAC/anime-kiss.gif",
                "https://media.tenor.com/ErAPuiWY46gAAAAC/anime-kiss-love.gif"
            ]
            await ctx.send(f"{ctx.author.mention} kisses {member.mention}! 💋\n{random.choice(gifs)}")

    # Pat
    @commands.command()
    async def pat(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send(f"{ctx.author.mention}, pat who? 👀")
        else:
            gifs = [
                "https://media.tenor.com/L2z1a0Jb6XQAAAAC/anime-pat.gif",
                "https://media.tenor.com/4Cq5q1R9WlYAAAAC/anime-headpat.gif"
            ]
            await ctx.send(f"{ctx.author.mention} pats {member.mention} gently. 🐾\n{random.choice(gifs)}")

      #fuck
    @commands.command()
    async def fuck(self,ctx,member:discord.Member = None):
        if member is None:
            await ctx.send(f"jackass {ctx.author.mention}fucked emself kink ")
        else:
            gifs = [

            ]
            await ctx.send(f"{ctx.author.mention} fucks {member.mention} gently \n{random.choice(gifs)}")
    #bonk
    @commands.command()
    async def bonk(self,ctx,member:discord.Member=None):
        if member is None:
            await ctx.send(f"kink you cant bonk yourself {ctx.author.mention}")
        elif member is ctx.author:
            await ctx.send(f"yeah bonk yourself boi you deserve {ctx.author.mention}")
        else:
            gifs = [

            ]
            await ctx.send(f"{ctx.author.mention} bonks {member.mention} cutely \n{random.choice(gifs)}")

    @commands.command()
    async def slap(self,ctx,member:discord.Member=None):
        if member is None:
            await ctx.send(f"who you need to slap boi")
        elif member is ctx.author:
            await ctx.send(f"yeah mate slap {ctx.author.mention} yourself")
        else:
            gifs = [ # add your gifs here

            ]
            await ctx.send(f"{ctx.author.mention} slaps {member.mention} hardly \n{random.choice(gifs)}")

    @commands.command()
    async def nutkick(self,ctx,member:discord.Member=None):
        if member is None:
            await ctx.send(f"yeah boi end someone's generation")
        elif member is ctx.author:
            await ctx.send(f"buddy you gonna smash yo nuts {ctx.author.mention}")
        else:
            gifs = [ # add gifs here

            ]
            await ctx.send(f"{ctx.author.mention}  nutkicked {member.mention} \n{random.choice(gifs}")
    @commands.command()
    async def spank(self,ctx,member:discord.Member=None):
        if member is None:
            await ctx.send(f"someone gonna get thier ass whipped tightly")
        elif member is ctx.author:
            await ctx.send(f"{ctx.author.mention} spanked {ctx.author.mention}")
        else:
            gifs = [

            ]
            await ctx.send(f"{ctx.author.mention} spanks {member.mention} lovely..UWU >_<" , {random.choice(gifs)}")
    
# Setup this is the main task
async def setup(bot):
    await bot.add_cog(Roleplay(bot))

                  
