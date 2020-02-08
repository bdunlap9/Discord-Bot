import discord, vulners, os, requests

from discord.ext import commands
from dotenv import load_dotenv
from github import Github
from bs4 import BeautifulSoup as BS

load_dotenv()

vulners_api_key = os.getenv('vulners_api_key')
GITHUB_ACCESS_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')

class searching(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('[LOGS] Cog "{}" loaded'.format(self.__class__.__name__))

    @commands.command()
    async def exploits(self, ctx, string=None):
        if string is None:
            print('\n[LOGS] Must enter a string')
            await ctx.send('Must enter a string')
        else:
            print(f'\n[LOGS] Searching using vulners api for {string}')
            vulners_api = vulners.Vulners(vulners_api_key)
            exploit_search = vulners_api.searchExploit(string, limit=10)
            hrefs = [item['href'] for item in exploit_search]
            titles = [item['title'] for item in exploit_search]
            await ctx.send('```\n'  + '\n['.join(hrefs) + '\n' + '```')

    @commands.command()
    async def githubSearch(self, ctx, string=None):
        if string is None:
            print('\n[LOGS] Must enter a string')
            await ctx.send('Must enter a string')
        else:
            print(f'\n[LOGS] Searching github for {string}')
            # connecting github token for public_repo search
            git = Github(GITHUB_ACCESS_TOKEN)
            rate_limit = git.get_rate_limit()
            rate = rate_limit.search
            if rate.remaining == 0:
                print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
                return
            else:
                print(f'You have {rate.remaining}/{rate.limit} API calls remaining')
            query = f'"{string} english" in:readme+in:description'
            result = git.search_code(query, order='desc')
            max_size = 10
            print(f'Found {result.totalCount} file(s)')
            if result.totalCount > max_size:
                result = result[:max_size]
            for file in result:
                print(f'{file.download_url}')
                await ctx.send(f'{file.download_url}')

    @commands.command()
    async def google(self, ctx, string=None):
        if string is None:
            print('\n[LOGS] Must enter a string')
            await ctx.send('Must enter a string')
        else:
            print(f'\n[LOGS] Running google search on {string}')
            s = string.replace(' ', '+')
            url = f'https://www.google.com/search?q={s}'
            agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
            headers = {'user-agent': agent}
            req = requests.get(url, headers=headers)
            if req.status_code == 200:
                soup = BS(req.content, "html.parser")
                results = []
                for a in soup.find_all('div', class_='r'):
                    links = a.find_all('a')
                    if links:
                        link = links[0]['href']
                        title = a.find('h3').text
                        item = {
                            'Title: ': title,
                            'Link: ': link
                        }
                        results.append(item)
                        final_res = """Title: {}
Link: {}
                        """.format(title, link)
                        print(final_res)
                        await ctx.send('```'+final_res+'```')

def setup(bot):
    bot.add_cog(searching(bot))
    