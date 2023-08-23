import discord
from discord.ext import commands
import youtube_dl

intents = discord.Intents.default()
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {Bot.user.name}")

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@bot.command()
async def play(ctx, *, search_query):
    voice_channel = ctx.author.voice.channel

    if not ctx.voice_client:
        await voice_channel.connect()

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_query, download=False)
        url = info['formats'][0]['url']

    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
        'options': '-vn',
    }
    ctx.voice_client.play(discord.FFmpegPCMAudio(url, **FFMPEG_OPTIONS))

bot.run('MTEzMzM1NjQ4NDMzMjM1OTY5MA.Gsyt5f.-Sh4EBmZjbyUv1ySIci3HyVZA-wA404eHlN-c0')
