import discord, time, sys, subprocess, os

from discord.ext import commands

class terminal(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('[LOGS] Cog "{}" loaded'.format(self.__class__.__name__))

    def weeke_system(cmd):
        subprocess.call(cmd, shell=True)

    def restart_program():
        python = sys.executable
        os.execl(python, python, "\"{}\"".format(sys.argv[0]))

    @commands.command()
    async def terminal(self, ctx, option=None, Clear=None, Restart=None, Stop=None):
        if option is None:
            print('\n[LOGS] Must enter an option (Clear, Restart, Stop)')
            await ctx.send('Must enter an option (Clear, Restart, Stop)')
        elif option == 'clear':
            print('\n[LOGS] Running clear terminal')
            await ctx.send('Running clear terminal')
            weeke_system('cls')
            time.sleep(4)
            await ctx.send('Terminal Cleared!')
        elif option == 'restart':
            print('\n[LOGS] Running restart bot')
            await ctx.send("Restarting Bot!")
            terminal.restart_program()
        elif option == 'stop':
            print('\n[LOGS] Running stop bot')
            await ctx.send('Shutting Down Bot!')
            sys.exit()
        else:
            print('\n[LOGS] Invalid option!')
            await ctx.send('Invalid option!')

def setup(bot):
    bot.add_cog(terminal(bot))
