import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.storage.redis import RedisStorage
from service.scrap_baires import scrap_argenprop, headers, url
from handlers import scrap_handlers
from redis.asyncio.client import Redis
from config import load_config
import json

async def main() -> None:

    config = load_config()

    redis = Redis()
    storage = RedisStorage(redis=redis)
    dp = Dispatcher(storage=storage)

    @dp.message(CommandStart())
    async def command_start_handler(message: Message) -> None:
        await message.answer(f'Hello, {html.bold(message.from_user.full_name)}!')

    dp.include_router(scrap_handlers.rt)

    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())