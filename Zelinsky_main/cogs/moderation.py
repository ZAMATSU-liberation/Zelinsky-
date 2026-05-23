import discord 
from discord.ext import commands
import asyncio
from datetime import timedelta


class moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    #kick members
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.kick(reason=reason)
            await ctx.send(f"this nigga {member.mention} has been kicked.\nReason: {reason}")
        except Exception as e:
            await ctx.send("❌ I can't kick this bitch  ")
            print(e)

    # Ban
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        try:
            await member.ban(reason=reason)
            await ctx.send(f"🔨 {member.mention} has been banned.\nReason: {reason}")
        except Exception as e:
            await ctx.send(" I can't ban this user.")
            print(e)
    #mute
    @commands.command
    @commands.has_permissions(mute_members=True)
    async def timeout(self,ctx,member=discord.Member,minutes=int, reason=None ):
        us = ctx.author.mention
        try:
            duration = timedelta(minutes=minutes)
            await member.timeout(
                    duration,
                    reason=reason
            )
            await ctx.send(f'{us} gave {member.mention} a timeout of {duration} ')
        except:
            await ctx.send('i cant mute this member!')

async def setup(bot):
    await bot.add_cog(moderation(bot))


            
    