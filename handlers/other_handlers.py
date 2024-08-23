from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext



rt = Router()

@rt.message()
async def echo_handler(message: Message, state: FSMContext) -> None:
    await message.answer('Sorry, can\'t understand, please press the button below or choose the command /help')