import discord, base64, binascii

from discord.ext import commands
from urllib.parse import unquote

class encoding_decoding(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('[LOGS] Cog "{}" loaded'.format(self.__class__.__name__))

    @commands.command()
    async def b64encode(self, ctx, string=None):
        if string is None:
            print('\n[LOGS] Must enter a string!')
            await ctx.send('Must enter a string!')
        else:
            print(f'\n[LOGS] Running b64decode on {string}!')
            b = string.encode("ascii")
            c = base64.b64encode(b)
            d = c.decode("ascii")
            await ctx.send(d)

    @commands.command()
    async def b64decode(self, ctx, string=None):
        if string is None:
            print('\n[LOGS] Must enter a string!')
            await ctx.send('Must enter a string!')
        else:
            print(f'\n[LOGS] Running b64decode on {string}!')
            string_bytes = base64.b64decode(string)
            string = string_bytes.decode('ascii')
            await ctx.send(string)

    @commands.command()
    async def urlDecode(self, ctx, string=None):
        if string is None:
            print('\n[LOGS] Must enter a string!')
            await ctx.send('Must enter a string!')
        else:
            print(f'\n[LOGS] Running URldecode on {string}!')
            unquote(unquote(string))
            await ctx.send(unquote(unquote(string)))

    @commands.command()
    async def hexEncode(self, ctx, string=None):
        if string is None:
            print('\n[LOGS] Must enter a string')
            await ctx.send('Must enter a string')
        else:
            print(f'HEX Encoding {string}')
            await ctx.send(binascii.b2a_hex(string))

    @commands.command()
    async def hexDecode(self, ctx, string=None):
        if string is None:
            print('\n[LOGS] Must enter a string')
            await ctx.send('Must enter a string')
        else:
            print(f'HEX Encoding {string}')
            await ctx.send(binascii.b2a_hex(string))

def setup(bot):
    bot.add_cog(encoding_decoding(bot))