import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import pytesseract
import cv2
import numpy as np
import re

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

@bot.command(name='scan')
async def scan_receipt(ctx):
    message = ctx.message

    try:
        attachment = message.attachments[0]
    except:
        await ctx.send("Please attach a valid image file. EXCEPT")
        return

    if attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg')) == False:
        await ctx.send("Please attach a valid image file. ")
        return
    
    response = await attachment.read()
    nparr = np.frombuffer(response, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Perform OCR on the image to extract the receipt total
    text = pytesseract.image_to_string(img)
    total = extract_total(text)

    print(total)
    
    await ctx.send("Image scanned!")


def extract_total(text):
    # Search for a decimal number preceded by the word "total"
    match = re.search(r'total\s*\$?(\d+\.\d+)', text, re.IGNORECASE)
    if match:
        return match.group(1)
    else:
        return None


bot.run(token)