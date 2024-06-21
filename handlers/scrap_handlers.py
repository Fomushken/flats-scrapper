from aiogram import Router, F
from aiogram.types import Message
from service.scrap_baires import scrap_argenprop, headers, url
import json

rt = Router()

@rt.message(F.text == 'baires')
async def baires_handler(message:Message) -> None:
    a, b = scrap_argenprop(headers=headers, url=url)
    await message.answer(json.dumps(a[b], indent=3))