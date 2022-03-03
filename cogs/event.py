import re
import discord
from discord import channel
from discord import user
from discord.ext import commands
import random
from discord.utils import get
from platform import *


class event(commands.Cog):
    def __init__(self, bot):
        self.bot, self.on_readys, self.on_guild_joins, self.on_commands = bot, 883563114623287298, 883560884075638814, 926041030367793182
        self.bot_version = '1.0.0'
        self.logger = 836819417325240331

    @commands.Cog.listener()
    async def on_ready(self):
        dpyVersion = discord.__version__
        pythonVersion = python_version()
        print('We have logged ' + str(self.bot.user))
        print('bot version : ' + self.bot_version)
        print('discord.py version : ' + str(dpyVersion))
        print('python version : ' + str(pythonVersion))
        channel = self.bot.get_channel(self.on_readys)
        await channel.send('We have logged ' + str(self.bot.user))
        await channel.send('bot version : ' + self.bot_version)
        await channel.send('discord.py version : ' + str(dpyVersion))
        await channel.send('python version : ' + str(pythonVersion))

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # if isinstance(error, commands.CommandNotFound):
        #     await ctx.channel.send('invalid command used')

        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(f"hi, {ctx.author.mention} you are missing the permission " + ", ".join(error.missing_perms))
            await ctx.message.delete()

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.send('please enter all the required args')

        elif isinstance(error, commands.ChannelNotFound):
            # await ctx.send(f'Channel not found!', delete_after=7)
            await ctx.send(f'hi, {ctx.author.mention} {error}')
            await ctx.message.delete()

        elif isinstance(error, commands.MemberNotFound):
            await ctx.send(f'hi, {ctx.author.mention} {error}')
            await ctx.message.delete()

        elif isinstance(error, commands.RoleNotFound):
            await ctx.send(f'hi, {ctx.author.mention} {error}')
            await ctx.message.delete()

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(error)
            await ctx.message.delete()

        elif isinstance(error, commands.errors.NotOwner):
            await ctx.send('sorry this command is only for developers')

        else:
            raise error

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.author == self.bot.user:
            return

        if f'@{self.bot.user.display_name}' in message.content:
            print(message.content)
            await message.channel.send(f'my prefix `bby `')

        if isinstance(message.channel, discord.channel.DMChannel):
            await message.channel.send(f'hello im bot music')

    @commands.Cog.listener()
    async def on_command(self, ctx):
        channel = self.bot.get_channel(self.on_commands)
        channel1 = self.bot.get_channel(self.logger)
        embed = discord.Embed(
            title=f"{ctx.author} used a command!",
            description=f'**Information :**\n```cs\nauthor : {ctx.author}\nguild : {ctx.guild.name}\nchannel : {ctx.message.channel.name}\ncontent : {ctx.message.content}```**Id :**\n```cs\nauthor : {ctx.author.id}\nguild : {ctx.guild.id}\nchannel : {ctx.message.channel.id}```',
            color=ctx.author.colour,
            timestamp=ctx.message.created_at
        )
        await channel.send("––––––––––––––––––––––––––––––––––––––––––––––––", embed=embed)
        await channel1.send("––––––––––––––––––––––––––––––––––––––––––––––––", embed=embed)

    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        channel = self.bot.get_channel(self.on_commands)
        channel1 = self.bot.get_channel(self.logger)
        embed = discord.Embed(
            title=f"Completed {ctx.author}'s command!",
            description=f'**Information :**\n```cs\nauthor : {ctx.author}\nguild : {ctx.guild.name}\nchannel : {ctx.message.channel.name}\ncontent : {ctx.message.content}```**Id :**\n```cs\nauthor : {ctx.author.id}\nguild : {ctx.guild.id}\nchannel : {ctx.message.channel.id}```',
            color=ctx.author.colour,
            timestamp=ctx.message.created_at
        )
        await channel.send(embed=embed)
        await channel1.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_join(self, ctx):
        channel_log = self.bot.get_channel(self.on_guild_joins)
        await channel_log.send('Bot has been added to a new server')
        await channel_log.send('List of servers the bot is in: ')

        for guild in self.bot.guilds:
            await channel_log.send(guild.name)


def setup(bot):
    bot.add_cog(event(bot))
