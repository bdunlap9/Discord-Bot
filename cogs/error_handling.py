import discord, logging

from discord.ext import commands

class error_handling(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        print('[LOGS] Cog "{}" loaded'.format(self.__class__.__name__))

    # System Logging
    logger = logging.getLogger("discord")
    logger.setLevel(logging.INFO) # for Debug: logging.DEBUG or for INFO: logging.INFO
    handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
    handler.setFormatter(
        logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
    )
    logger.addHandler(handler)

    @commands.Cog.listener()
    async def on_command_error(ctx, error):
        if isinstance(error, commands.errors.CheckFailure):
            await ctx.send('You do not have permission to use that command!')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found! Try again!')
        else:
            await ctx.send('Unknown error has occurred! Please message Weeke!')

def setup(bot):
    bot.add_cog(error_handling(bot))