from aiogram import Router, F
from aiogram.types import Message
from service.scrap_baires import scrap_argenprop, headers, url
from lexicon.lexicon_ru import KEYBOARDS
from service.make_post import make_post, item
from keyboards.main_keyboard import baires_kb, main_kb
import json

rt = Router()

@rt.message(F.text == KEYBOARDS['to_baires_btn'])
async def baires_handler(message:Message) -> None:
    a, b = scrap_argenprop(headers=headers, url=url)
    # await message.answer(json.dumps(a[b], indent=3))
    await message.answer(text='Выбери ниже кнопку', reply_markup=baires_kb)

@rt.message(F.text == KEYBOARDS['send_announcement_btn'])
async def announcement_handler(message: Message) -> None:
    post = make_post(item=item, language='ru')
    await message.answer_media_group(media=post['media'])
    await message.answer(text=post['text'])

@rt.message(F.text == KEYBOARDS['back_btn'])
async def back_to_main_handler(message: Message) -> None:
    await message.answer(text='Возвращаю назад', reply_markup=main_kb)