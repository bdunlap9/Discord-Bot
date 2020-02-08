import discord
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('[LOGS] Cog "{}" loaded'.format(self.__class__.__name__))

    @commands.command()
    async def h(self, ctx):
        print(
            '\n[LOGS] Commands: \n .kick\n .ban\n .isUp\n .ping\n .purge\n .unBan\n .genShellPy\n .genShellPerl\n '
            '.getRefs\n .scanIp\n .whois\n '
            '.traceroute\n .nslookup\n .b64encode\n .b64decode\n .urlDecode\n .githubSearch\n .exploits\n '
            '.terminal\n .sqliTest\n .vtSampleReport\n .dnsDumpster\n .scrapeFiledropper\n .google\n hexEncode\n .hexDecode')
        embed = discord.Embed(
            title="List of all commands that can be used",
            description="Command list",
            colour=discord.Colour.blue()
        )
        embed.set_footer(text="Help function")
        embed.set_author(name="Weeke")
        embed.add_field(name='.kick', value='Kick a member', inline=True)
        embed.add_field(name='.ban', value='Ban a member', inline=True)
        embed.add_field(name='.unBan', value='Unban a member', inline=True)
        embed.add_field(name='.isUp', value='Check if a host or ip is Up or Down', inline=False)
        embed.add_field(name='.ping', value='Get client latency', inline=True)
        embed.add_field(name='.purge', value='Purge chat (default is 2 lines)', inline=True)
        embed.add_field(name='.genShellPy', value='Generates a reverse shell in python', inline=True)
        embed.add_field(name='.genShellPerl', value='Generates a reverse shell in perl', inline=False)
        embed.add_field(name='.getRefs', value='Generates urls for censys.io and shodan.io', inline=True)
        embed.add_field(name='.scanIp', value='Scan ip or host using shodan.io API', inline=True)
        embed.add_field(name='.whois', value='Whois lookup on a host', inline=True)
        embed.add_field(name='.scrapeFiledropper', value='Scrapes filedropper.com for all links', inline=False)
        embed.add_field(name='.sqliTest', value='Test for basic SQL Injection vulnerabilities', inline=True)
        embed.add_field(name='.nslookup', value='Runs a nslookup on host', inline=True)
        embed.add_field(name='.dnsDumpster', value='Use dnsDumpster unoficiall api', inline=True)
        embed.add_field(name='.b64encode', value='Base64 encodes a string', inline=False)
        embed.add_field(name='.b64decode', value='Base64 decodes a string', inline=True)
        embed.add_field(name='.urlDecode', value='Does a url decode on string', inline=True)
        embed.add_field(name='.githubSearch', value='Searches github using a query', inline=True)
        embed.add_field(name='.exploits', value='Does a vulnDB exploit search with query', inline=False)
        embed.add_field(name='.terminal', value='Runs terminal commands(Clear, Restart, Stop)', inline=True)
        embed.add_field(name='.google', value='Search google', inline=True)
        embed.add_field(name='.vtSampleReport', value='Creates a virustotal report for a given sample', inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        print('\n[LOGS] Running ping command!')
        await ctx.send(f'Client Latency: {round(self.bot.latency * 1000)}')

def setup(bot):
    bot.add_cog(help(bot))
