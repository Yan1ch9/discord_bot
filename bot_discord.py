import discord
from discord.ext import commands
from bot_logic import generate_password
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command(name="password")
async def password1(ctx, length):
    password = generate_password(length)
    await ctx.send(password)
    await ctx.send(length)
bot.run("")
