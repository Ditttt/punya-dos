import discord
from discord.ext import commands
import os
from discordTogether import DiscordTogether as yt

PREFIX = [
    'Dp.', 'dp.','dP.','DP.'
]


bot = commands.Bot(command_prefix=PREFIX)

together_control = yt(bot)

class MyNewHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page, color=discord.Color.purple())
            emby.set_thumbnail(url=bot.user.avatar_url)
            await destination.send(embed=emby)
    
    async def send_command_help(self, command):
        embed = discord.Embed(title=self.get_command_signature(command), color=discord.Color.purple())
        embed.add_field(name="Help", value=command.help)
        alias = command.aliases
        if alias:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)
    
    async def send_error_message(self, error):
        embed = discord.Embed(title="Error", description=error, color=discord.Color.red())
        channel = self.get_destination()
        await channel.send(embed=embed)

bot.help_command = MyNewHelp()


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

bot.run("OTQ4NDI0ODYxNjg3MTE1ODU3.Yh7new.XtlndavfSVTjui4rfPbhNI_tOGk")
