import discord, os, subprocess, ctypes, sys, platform

from discord.ext import commands
from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def weeke_system(cmd):
    subprocess.call(cmd, shell=True)

weeke_system('cls')
ctypes.windll.kernel32.SetConsoleTitleW("[Weeke's]->Discord Bot")

print(f"Loading bot using discord.py version: {discord.__version__} and Python version {platform.python_version()}\n")

load_dotenv()

discord_token = os.getenv('discord_token')

bot = commands.Bot(command_prefix='.')

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.[extension]')
    
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.[extension]')
    
@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cogs.[extension]')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(discord_token)
