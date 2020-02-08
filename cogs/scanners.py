import discord, shodan, os, socket

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

SHODAN_API_KEY = os.getenv('SHODAN_API_KEY')

class scanners(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('[LOGS] Cog "{}" loaded'.format(self.__class__.__name__))

    @commands.command()
    async def scanIp(self, ctx, ip=None):
        if ip is None:
            print('\n[LOGS] Must enter a host or ip!')
            await ctx.send('Must enter a host or ip!')
        else:
            # connecting api key
            api = shodan.Shodan(SHODAN_API_KEY)
            print(f'\n[LOGS] Running scan with shodan on {ip}!')
            s = socket.gethostbyname(ip)
            host = api.host(s)
            # Print general info
            print("""IP: {}\nOrganization: {}\nOperating System: {}\nReported: {}""".format(host['ip_str'],
                                                                                            host.get('org', 'n/a'),
                                                                                            host.get('os', 'n/a'),
                                                                                            host.get('reported', 'false')))
            await ctx.send("""IP: {}\nOrganization: {}\nOperating System: {}\nReported: {}""".format(host['ip_str'],
                                                                                                    host.get('org', 'n/a'),
                                                                                                    host.get('os', 'n/a'),
                                                                                                    host.get('reported',
                                                                                                            'false')))
            # Print all banners
            for item in host['data']:
                print("""Port: {}""".format(item['port'], item['data']))
                await ctx.send("""Port: {}""".format(item['port'], item['data']))

def setup(bot):
    bot.add_cog(scanners(bot))