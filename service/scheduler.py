import asyncio
import aioschedule
import datetime
from service.scrap_baires import scrap_argenprop


async def get_scrap_schedule():
    aioschedule.every(10).minutes.do(scrap_argenprop)


async def on_startup():
    await asyncio.create_task(get_scrap_schedule())
    