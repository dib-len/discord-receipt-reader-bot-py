import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
token = os.getenv('BOT_TOKEN')

print(token)
