from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext



rt = Router()

@rt.message()
async def echo_handler(message: Message, state: FSMContext) -> None:
    await message.answer('Не понял, нажмите на кнопку ниже, либо выполните команду /help')
    await state.update_data({str(message.message_id): message.text})
    data = await state.get_data()
    state = await state.get_state()
    print(data, state, sep='\n')