import discord, dns.resolver, socket, nmap, os

from discord.ext import commands
from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
from ipwhois import IPWhois

class lookup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('[LOGS] Cog "{}" loaded'.format(self.__class__.__name__))

    # setup scanner
    scanner = nmap.PortScanner()

    def get_image(domain):
        url = 'https://dnsdumpster.com/'
        s = requests.Session()
        s.headers = {'Referer': url}
        r = s.get(url)
        soup = BS(r.content, 'html.parser')
        csrf_middleware = soup.findAll('input', attrs={'name': 'csrfmiddlewaretoken'})[0]['value']
        s.cookies.update({'csrftoken':csrf_middleware})
        d = {'csrfmiddlewaretoken': csrf_middleware, 'targetip': domain}
        s.post(url, data = d)
        pic = s.get('{}/static/map/{}.png'.format(url, domain), stream=True)
        print(pic.content[:20])
        full_result_path = os.path.join('./', 'result.png')
        with open(full_result_path, 'wb') as f: f.write(pic.content)

    @commands.command()
    async def getRefs(self, ctx, ip=None):
        if ip is None:
            print('\n[LOGS] Must enter a host or ip!')
            await ctx.send('Must enter a host or ip!')
        else:
            print(f'\n[LOGS] Getting refs for {ip}!')
            await ctx.send('https://censys.io/ipv4/' + ip)
            await ctx.send('https://www.shodan.io/host/' + ip)

    @commands.command()
    async def whois(self, ctx, ip=None):
        if ip is None:
            print('\n[LOGS] Must enter a ip!')
            await ctx.send('Must enter a ip!')
        else:
            print(f'\n[LOGS] Running whois on {ip}')
            host = socket.gethostbyname(ip)
            w = IPWhois(host)
            res = w.lookup_whois(inc_nir=True)
            final_res = """
IP: {}
IP Range: {}
Name: {}
Handle: {}
Registry: {}
Description: {}
Date: {}
Updated: {}
Country: {} 
State: {}
City: {}
Address: {}
Postal Code: {}
            """.format(res['query'], res['nets'][0]['range'], res['nets'][0]['name'], res['nets'][0]['handle'], res['asn_registry'], res['asn_description'], res['asn_date'], res['nets'][0]['updated'], res['nets'][0]['country'], res['nets'][0]['state'], res['nets'][0]['city'], res['nets'][0]['address'], res['nets'][0]['postal_code'])
            print(final_res)
            await ctx.send(final_res)
    
    @commands.command()
    async def nslookup(self, ctx, ip=None):
        if ip is None:
            print('\n[LOGS] Must enter a url or ip!')
            await ctx.send('Must enter a url or ip!')
        else:
            print(f'\n[LOGS] Running nslookup on {ip}!')
            dns_results = dns.resolver.query(ip, 'MX')
            for data in dns_results:
                print(data.exchange)
                await ctx.send(data.exchange)

    @commands.command()
    async def dnsDumpster(self, ctx, domain=None):
        if domain is None:
            print('\n[LOGS] Must enter a domain to scan')
            await ctx.send('Must enter a domain to scan')
        else:
            print(f'\n[LOGS] Using dnsDumpster on {domain}')
            res = DNSDumpsterAPI(True).search(domain)

            print("\nDNS Servers ")
            await ctx.send("DNS Servers")
            for entry in res['dns_records']['dns']:
                print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
                await ctx.send(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
            
            print("\nMX Records")
            await ctx.send("\nMX Records")
            for entry in res['dns_records']['mx']:
                print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
                await ctx.send(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))

            print("\nHost Records (A)")
            await ctx.send("\n Host Records (A)")
            for entry in res['dns_records']['host']:
                if entry['reverse_dns']:
                    print(("{domain} ({reverse_dns}) ({ip}) {as} {provider} {country}".format(**entry)))
                    await ctx.send(("{domain} ({reverse_dns}) ({ip}) {as} {provider} {country}".format(**entry)))
                else:
                    print(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))
                    await ctx.send(("{domain} ({ip}) {as} {provider} {country}".format(**entry)))

            lookup.get_image(domain)

            full_result_path = os.path.join(output_directory, 'result.png')
            file = discord.File(full_result_path, filename=full_result_path)
            await ctx.send("", file=file)
            os.remove(full_result_path)
    
    @commands.command()
    async def isUp(self, ctx, ip_addr=None):
        if ip_addr is None:
            print('\n[LOGS] Must enter a ip!')
            ctx.send('Must enter a ip!')
        else:
            print(f'\n[LOGS] Running isUp command on {ip_addr}!')
            host = socket.gethostbyname(ip_addr)
            scanner.scan(host, '1', '-v')
            print("\n[LOGS] IP Status: ", scanner[host].state())
            await ctx.send(scanner[host].state())

def setup(bot):
    bot.add_cog(lookup(bot))
