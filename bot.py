import os
import discord

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Dotbhai online: {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if bot.user in message.mentions:
        await message.reply("هلا! أنا Dotbhai AI 🚀")

bot.run(TOKEN)
