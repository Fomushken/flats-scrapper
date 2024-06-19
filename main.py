import asyncio
import logging
import sys
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from service.scrap_baires import scrap_argenprop, headers, url
import json


load_dotenv()

TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f'Hello, {html.bold(message.from_user.full_name)}!')

@dp.message(F.text == 'baires')
async def baires_handler(message:Message) -> None:
    a, b = scrap_argenprop(headers=headers, url=url)
    await message.answer(json.dumps(a[b], indent=3))

@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())