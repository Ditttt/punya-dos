import discord
from discord.ext import commands
import os
from discordTogether import DiscordTogether as yt

PREFIX = [
    'SS1 ',
    'SS1',
    'sS1 ',
    'sS1',
    'Ss1 ',
    'Ss1',
    'ss1 ',
    'ss1',
]


bot = commands.Bot(command_prefix=PREFIX)

together_control = yt(bot)


@bot.command()
async def startYT(ctx):
    link = await together_control.create_link(ctx.author.voice.channel.id, 'youtube')
    await ctx.send(f"Click the blue link!\n{link}")


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run("ODg3NTE3MjgzNjg4MjgwMDg4.YUFS4Q.ntVj34qLnlZICag_m5N2w9R4WiM")
