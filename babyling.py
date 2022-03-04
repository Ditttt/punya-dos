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

@bot.command(aliases=["rep"])
async def report(ctx, *, args):
    await ctx.send(
        content=
        f'oke {ctx.author.mention} kita selidiki ya,Sorry banget :SS_cat_blush:'
    )
    channel = bot.get_channel(946630512162791434)
    em = discord.utils.get(bot.emojis, name='SS_cat_blush')
    await channel.send(f'''
Hey <@851997270597828618> ada report baru nih
Report : {args}
Reporter : {ctx.author.mention}
Id Reporter: {ctx.author.id}
Id channel : {ctx.channel.id}
Channel : {ctx.channel.mention}''')

@bot.command()
async def say(ctx, *, args):
  admin = [763433861634850816,851997270597828618]
  if ctx.author.id in admin:
    await ctx.send(args)
    await ctx.message.delete()
  else:
    pass

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Delpi"))
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))
    channel = bot.get_channel(946630512162791434)
    await channel.send(f'''Delpi is online''')


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
