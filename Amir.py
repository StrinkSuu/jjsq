import discord
from discord.ext import commands

# Initialize the bot
bot = commands.Bot(command_prefix=';')

# Event to print a message in the console when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

# Command to ban a member
@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} has been banned.')

# Command to kick a member
@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} has been kicked.')

# Run the bot with your token
bot.run('YOUR_BOT_TOKEN')
