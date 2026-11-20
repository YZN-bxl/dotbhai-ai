
import os
import discord
from openai import AsyncOpenAI

TOKEN = os.getenv("DISCORD_TOKEN")
API_KEY = os.getenv("OPENAI_API_KEY")

ai = AsyncOpenAI(api_key=API_KEY)

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

    if bot.user not in message.mentions:
        return

    prompt = message.content
    prompt = prompt.replace(
        f"<@{bot.user.id}>", ""
    ).replace(
        f"<@!{bot.user.id}>", ""
    ).strip()

    if not prompt:
        return

    try:
        async with message.channel.typing():
            response = await ai.responses.create(
                model="gpt-5.5",
                instructions="You are Dotbhai, a helpful Discord chatbot. Reply naturally in the user's language.",
                input=prompt
            )

        answer = response.output_text or "لم أتمكن من إنشاء رد."

        await message.reply(answer[:1900])

        for i in range(1900, len(answer), 1900):
            await message.channel.send(answer[i:i+1900])

    except Exception as error:
        print(f"Error: {error}")
        await message.reply("حدث خطأ، حاول مرة ثانية.")

bot.run(TOKEN)
