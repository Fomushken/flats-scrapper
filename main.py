import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage
from handlers import scrap_handlers, other_handlers, commands_handlers
from redis.asyncio.client import Redis
from config import load_config
from keyboards.set_menu import set_main_menu

async def main() -> None:

    config = load_config()

    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    redis = Redis()
    storage = RedisStorage(redis=redis)
    dp = Dispatcher(storage=storage)

    await set_main_menu(bot)

    dp.include_router(commands_handlers.rt)
    dp.include_router(scrap_handlers.rt)
    dp.include_router(other_handlers.rt)


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s')
    asyncio.run(main())