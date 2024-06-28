from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicon.lexicon_ru import KEYBOARDS

to_baires_btn = KeyboardButton(text=KEYBOARDS['to_baires_btn'])

main_kb = ReplyKeyboardMarkup(keyboard=[
    [to_baires_btn]
    ],
    resize_keyboard=True,
    one_time_keyboard=True)

subscribe_btn = KeyboardButton(text=KEYBOARDS['subscribe_btn'])
back_btn = KeyboardButton(text=KEYBOARDS['back_btn'])

baires_kb = ReplyKeyboardMarkup(keyboard=[
    [subscribe_btn],
    [back_btn]
], resize_keyboard=True)

unsubscribe_btn = KeyboardButton(text=KEYBOARDS['unsubscribe_btn'])

subscribers_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [unsubscribe_btn],
        [back_btn]
    ]
, resize_keyboard=True)