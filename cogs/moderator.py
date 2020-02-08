import discord

from discord.ext import commands

class moderator(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('[LOGS] Cog "{}" loaded'.format(self.__class__.__name__))
    
    @commands.has_role('Admin')

    @commands.Cog.listener()
    async def on_connect(self):
        print('[LOGS] Connecting to discord!')

    @commands.Cog.listener()
    async def on_ready(self):
        print('[LOGS] Bot is ready!')
        print('[LOGS] Logged in: {}'.format(self.bot.user.name))
        print('[LOGS] Changed game presense: Kicking Ass')
        await self.bot.change_presence(activity=discord.Game(name="Kicking Ass"))


    @commands.Cog.listener()
    async def on_resumed(self):
        print("\n[LOGS] Bot has resumed session!")

    @commands.command()
    async def purge(self, ctx, amount=2):
        print('\n[LOGS] Purging chat! (Default amount = 2)')
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def kick(self, ctx, member: discord.Member = None, *, reason=None):
        if member is None:
            print('\n[LOGS] Must enter a member to kick!')
            await ctx.send('Please enter a member to kick!')
        else:
            await member.kick(reason=reason)

    @commands.command()
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):
        if member is None:
            print('\n[LOGS] Must enter a member to ban!')
            await ctx.send('Please enter a member to ban!')
        else:
            await member.ban(reason=reason)
            await ctx.send(f'Banned {self.member.mention}')

    @commands.command()
    async def unBan(self, ctx, *, member=None):
        if member is None:
            print('\n[LOGS] Please enter a member to unban!')
            await ctx.send('Please enter a member to unban!')
        else:
            # generating list of banned users
            banned_members = await ctx.guild.bans()
            member_name, member_disc = member.split('#')

            for ban_entry in banned_members:
                user = ban_entry.user

                if (user.name, user.disc) == (member_name, member_disc):
                    print(f'\n[LOGS] Unbanning {user.mention}!')
                    await ctx.guild.unban(user)
                    await ctx.send(f'Unbanned {self.user.mention}!')

def setup(bot):
    bot.add_cog(moderator(bot))
