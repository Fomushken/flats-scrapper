from aiogram import Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.states import FSMBairesScrap
from keyboards.main_keyboard import main_kb
from keyboards.other_keyboards import dev_kb
from lexicon.lexicon_eng import LEXICON


rt = Router()

@rt.message(CommandStart())  # /start
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(FSMBairesScrap.on_main)
    await message.answer(LEXICON['/start'].format(message.from_user.full_name), reply_markup=main_kb)

@rt.message(Command(commands='help')) # /help
async def command_help_handler(message: Message) -> None:
    await message.answer(LEXICON['/help'])

@rt.message(Command(commands='mydev')) # /mydev
async def command_dev_handler(message: Message) -> None:
    await message.answer(LEXICON['/mydev'], reply_markup=dev_kb)