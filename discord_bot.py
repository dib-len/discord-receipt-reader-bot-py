import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
token = os.getenv('BOT_TOKEN')
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(name='hello')
async def say_hello(ctx):
    await ctx.send('Hello!')

@bot.command(name='receipt')
async def say_hello(ctx):
    channel = ctx.channel
    thread = await channel.create_thread(name='Receipts Thread')
    await thread.send('Welcome to the Receipts thread!')
    await thread.send('Please send your images here!')

bot.run(token)