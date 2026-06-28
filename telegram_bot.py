import os
import asyncio
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

async def send_to_telegram(message):
    bot = Bot(token=BOT_TOKEN)

    MAX_LENGTH = 4000

    for i in range(0, len(message), MAX_LENGTH):
        await bot.send_message(
            chat_id=CHAT_ID,
            text=message[i:i+MAX_LENGTH]
        )

def send(message):
    asyncio.run(send_to_telegram(message))