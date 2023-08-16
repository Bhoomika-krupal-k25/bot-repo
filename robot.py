from discord.ext import commands
import discord
intents=discord.Intents.all()
bot=commands.Bot(command_prefix="!",intents=intents)

def run():
    @bot.event
    async def on_message(message:discord.message)