import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = '?', intents = intents)

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')

'''@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
''' # method for allowing pings to pass as a command

token = os.getenv('DISCORD_TOKEN')    
bot.run(token)