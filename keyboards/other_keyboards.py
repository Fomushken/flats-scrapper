from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_eng import LEXICON, COMMANDS, KEYBOARDS

developer_id = '940933457'
developer_button = InlineKeyboardButton(
    text=KEYBOARDS['dev_btn'],
    url=f'tg://user?id={developer_id}'
)

dev_kb = InlineKeyboardMarkup(
    inline_keyboard=[[developer_button]
                     ]
)