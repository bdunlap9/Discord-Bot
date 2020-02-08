import discord, requests, os.path

from discord.ext import commands
from bs4 import BeautifulSoup as BS

current_directory = os.getcwd()
output_directory = os.path.join(current_directory, r'output')

if not os.path.exists(output_directory):
   os.makedirs(output_directory)

class scrapers(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('[LOGS] Cog "{}" loaded'.format(self.__class__.__name__))

    @commands.command()
    async def scrapeFiledropper(self, ctx):
        full_result_path = os.path.join(output_directory, 'filedropper_com.txt')

        print('\n[LOGS] Scraping filedropper.com')
        await ctx.send('```\nPlease wait for scrape to finish, once its done it will upload file to chat.\n```')
        urls = ['http://www.filedropper.com/lister.php?id=0', 'http://www.filedropper.com/lister.php?id=1', 'http://www.filedropper.com/lister.php?id=2', 'http://www.filedropper.com/lister.php?id=3', 'http://www.filedropper.com/lister.php?id=4', 'http://www.filedropper.com/lister.php?id=5', 'http://www.filedropper.com/lister.php?id=6', 'http://www.filedropper.com/lister.php?id=7', 'http://www.filedropper.com/lister.php?id=8', 'http://www.filedropper.com/lister.php?id=9', 'http://www.filedropper.com/lister.php?id=a', 'http://www.filedropper.com/lister.php?id=b', 'http://www.filedropper.com/lister.php?id=c', 'http://www.filedropper.com/lister.php?id=d', 'http://www.filedropper.com/lister.php?id=e', 'http://www.filedropper.com/lister.php?id=f', 'http://www.filedropper.com/lister.php?id=g', 'http://www.filedropper.com/lister.php?id=h', 'http://www.filedropper.com/lister.php?id=i', 'http://www.filedropper.com/lister.php?id=j', 'http://www.filedropper.com/lister.php?id=k', 'http://www.filedropper.com/lister.php?id=l', 'http://www.filedropper.com/lister.php?id=m', 'http://www.filedropper.com/lister.php?id=n', 'http://www.filedropper.com/lister.php?id=o', 'http://www.filedropper.com/lister.php?id=p', 'http://www.filedropper.com/lister.php?id=q', 'http://www.filedropper.com/lister.php?id=r', 'http://www.filedropper.com/lister.php?id=s', 'http://www.filedropper.com/lister.php?id=t', 'http://www.filedropper.com/lister.php?id=u', 'http://www.filedropper.com/lister.php?id=v', 'http://www.filedropper.com/lister.php?id=w', 'http://www.filedropper.com/lister.php?id=x', 'http://www.filedropper.com/lister.php?id=y', 'http://www.filedropper.com/lister.php?id=z']
        for url in urls:
            req = requests.get(url)
            soup = BS(req.text)
            for all_links in soup.find_all('a', href=True):
                print("URL:", all_links['href'])
                with open(full_result_path, 'a') as f:
                    f.write(all_links['href'] + '\n')
        file = discord.File(full_result_path, filename=full_result_path)
        await ctx.send("", file=file)
        os.remove(full_result_path)

def setup(bot):
    bot.add_cog(scrapers(bot))
