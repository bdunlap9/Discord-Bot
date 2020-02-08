import discord, virustotal3.core, os, requests

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

vt_api = os.getenv('vt_api')

current_directory = os.getcwd()
output_directory = os.path.join(current_directory, r'output')

if not os.path.exists(output_directory):
   os.makedirs(output_directory)

class virustotal(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('[LOGS] Cog "{}" loaded \n'.format(self.__class__.__name__))
        
    @commands.command()
    async def vtSampleReport(self, ctx, sample_id=None):
        if sample_id is None:
            print('\n[LOGS] Must enter a sample id (SHA1, SHA256, MD5)')
            await ctx.send('Must enter a sample id (SHA1, SHA256, MD5)')
        else:
            # test sample a0dbae122905501741e03499e28bea1f
            print(f'\n[LOGS] Getting report for sample using {sample_id}')
            url = 'https://www.virustotal.com/vtapi/v2/file/report'

            params = {'apikey': vt_api, 'resource': sample_id}
            response = requests.get(url, params=params)
            json_response = response.json()

            md5 = json_response["md5"]
            sha256 = json_response["sha256"]
            sha1 = json_response["sha1"]
            permalink = json_response["permalink"]
            scanners = json_response["scans"].keys()

            markdown = """Scan Results
Link: {permalink}

MD5: {md5}
SHA256: {sha256}
SHA1: {sha1} 

            """.format(permalink=permalink , md5=md5, sha256=sha256, sha1=sha1)

            for scanner in scanners:
                detected = json_response["scans"][scanner]
                result = json_response["scans"][scanner]["result"]
                markdown += """|{scanner}|{detected}|{result}|\n""".format(scanner=scanner, detected=detected, result=result)

            full_report_path = os.path.join(output_directory, 'sample.md')

            with open(full_report_path, 'w') as file:
                file.write(markdown)

            file = discord.File(full_report_path, filename=full_report_path)
            await ctx.send("VirusTotal Sample Report", file=file)
            os.remove(full_report_path)

def setup(bot):
    bot.add_cog(virustotal(bot))
    