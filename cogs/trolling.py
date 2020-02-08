import discord

from discord.ext import commands

class trolling(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('[LOGS] Cog "{}" loaded'.format(self.__class__.__name__))

    @commands.command()
    async def spamMessage(self, ctx, message=None, lines=1, amount=10):
        if message is None:
            print('\n[LOGS] Must enter a message')
            await ctx.send('Must enter a message')
        else:
            print(f'\n[LOGS] Spamming {message} -> lines {lines} -> times {amount}')
            for times in range(amount):
                await ctx.send(message * lines)
                print(f'\n[LOGS] Done spamming {message} -> lines {lines} -> times {amount}')

def setup(bot):
    bot.add_cog(trolling(bot))
