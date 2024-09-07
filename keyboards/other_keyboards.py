from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_eng import LEXICON, COMMANDS, KEYBOARDS

developer_id = '940933457'
dev_tg_button = InlineKeyboardButton(
    text=KEYBOARDS['dev_tg_btn'],
    url=f'tg://user?id={developer_id}'
)

dev_linkedin_button = InlineKeyboardButton(
    text=KEYBOARDS['dev_linkedin_btn'],
    url='https://www.linkedin.com/in/marat-fomin/'
)

dev_github_button = InlineKeyboardButton(
    text=KEYBOARDS['dev_bithub_btn'],
    url='https://github.com/Fomushken'
)

dev_kb = InlineKeyboardMarkup(
    inline_keyboard=[[dev_tg_button],
                     [dev_github_button],
                     [dev_linkedin_button]
                     ]
)