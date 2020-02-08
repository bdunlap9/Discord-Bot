import discord, requests

from discord.ext import commands
from bs4 import BeautifulSoup as BS

class sqli_injection(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('[LOGS] Cog "{}" loaded'.format(self.__class__.__name__))

    @commands.command()
    async def sqliTest(self, ctx, url=None):
        global string
    
        if url is None:
            print('\n[LOGS] Must input url to test')
            await ctx.send('Must input url to test')
        else:
            print(f'\n[LOGS] Testing {url} for basic SQLI vulnerabilities')
            await ctx.send(f'Testing {url} for basic SQLI vulnerabilities')
            #####################################################################
            # EXAMPLES OF VULNERABLE SITES FOR TESTING                          #
            # https://www.architecturalpapers.ch/index.php?ID=4%27              #
            # http://www.wurm.info/index.php?id=8%27                            #
            # https://www.cityimmo.ch/reservations.php?lang=FR&todo=res&;id=22  #
            #####################################################################  
            urls = [url + "'", url + ';' ] 
            vulnerable_text = ['MySQL Query fail:', '/www/htdocs/', 'Query failed', 'mysqli_fetch_array()', 'mysqli_result', 'Warning: ', 'MySQL server', 'SQL syntax', 'You have an error in your SQL syntax;', 'mssql_query()', "Incorrect syntax near '='", 'mssql_num_rows()', 'Notice: ']
            for url in urls:
                results = requests.get(url)
                data = results.text
                soup = BS(data, features="html.parser")
                for vuln in vulnerable_text:
                    if vuln in data:
                        string = vuln
                        print('\n[LOGS] Vulnerable: ' + vuln)
                        await ctx.send('Vulnerable: ' + vuln)

def setup(bot):
    bot.add_cog(sqli_injection(bot))
