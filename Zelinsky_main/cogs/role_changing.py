import asyncio
import discord
from discord.ext import commands
class change_roles(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def role_change(self,ctx,member : discord.Member,role : discord.Role):
        if role>= ctx.guild.me.top_role:
            await ctx.send(f'sorry i cant assign this role{role.name} to this member{member.name}')
            return

        try:
            await member.add_roles()
            await ctx.send(f"successfully added {role.name} to {member.name}")
        except discord.Forbidden:
            await ctx.send('nigga i dont have permissions')

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def remove_role(self,ctx,member:discord.Member,role:discord.Role):
        if role>= ctx.guild.me_top_role:
            await ctx.send('sorry i cant remove the role of that member')
            return
        try:
            await member.remove_roles()
            await ctx.send(f"successfully removed {role.name} from {member.name}")
        except:
            await ctx.send("cant remove the role unexpected error")
        @commands.command()
        @commands.has_permissions(manage_nicknames=True)
        async def change_nickname(ctx,mwmber:discord.Member,*,nickname):
            if role >= ctx.guild.me_top_role:
                await ctx.send('sorry i cant change this user nickname')
                return
            try:
                await ctx.edit(nick=nickname)
                await ctx.send(f"successfully changed {member.name}'s nickname")
            except discord.Forbidden:
                await ctx.send(f"unexpected error {ctx.author.mention}")
        
async def setup(bot):
    await bot.add_cog(change_roles(bot))