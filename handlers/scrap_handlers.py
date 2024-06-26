from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from service.scrap_baires import scrap_argenprop, headers, url
from lexicon.lexicon_ru import KEYBOARDS, LEXICON
from service.make_post import make_post, item
from keyboards.main_keyboard import baires_kb, main_kb, subscribers_keyboard
from states.states import FSMBairesScrap
import json

rt = Router()

@rt.message(F.text == KEYBOARDS['to_baires_btn'], StateFilter(FSMBairesScrap.on_main))
async def baires_handler(message:Message, state: FSMContext) -> None:
    a, b = scrap_argenprop(headers=headers, url=url)
    # await message.answer(json.dumps(a[b], indent=3))
    await state.set_state(FSMBairesScrap.on_baires)
    await message.answer(text='Выбери ниже кнопку', reply_markup=baires_kb)

@rt.message(F.text == KEYBOARDS['subscribe_btn'], StateFilter(FSMBairesScrap.on_baires))
async def subscribe_handler(message: Message, state: FSMContext) -> None:
    # post = make_post(item=item, language='ru')
    await state.set_state(FSMBairesScrap.subscribed)
    await message.answer(text=LEXICON['subscribe'], reply_markup=subscribers_keyboard)
    # await message.answer_media_group(media=post['media'])
    # await message.answer(text=post['text'])


@rt.message(F.text == KEYBOARDS['unsubscribe_btn'], StateFilter(FSMBairesScrap.subscribed))
async def unsubscribe_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(FSMBairesScrap.on_main)
    await message.answer(text=LEXICON['unsubscribe'], reply_markup=main_kb)


@rt.message(F.text == KEYBOARDS['back_btn'])
async def back_to_main_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(FSMBairesScrap.on_main)
    # await state.set_data()
    await message.answer(text='Возвращаю назад', reply_markup=main_kb)