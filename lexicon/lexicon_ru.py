LEXICON: dict[str, str] = {
    '/start': '<b>Привет, {}!</b>\nЯ буду многофункциональным ботом, пока еще меня учат,' # in handler user's full name puts instead {}
              ' Введи команду /help, чтобы узнать мой функционал\n\n'
              '<b>Ниже ты можешь выбрать категорию</b>',
    '/help': 'Пока что я умею отправлять только необработанные данные о квартирах в Буэнос-Айресе с сайта argenprop, для этого напиши мне \'baires\'',
    '/mydev': 'Попозже доработаю эту команду'
}

COMMANDS: dict[str, str] = {
    '/start': 'Начать',
    '/help': 'Подсказки',
    '/mydev': 'Связь с разработчиком'
}

CALLBACKS: dict[str, str] = {

}

KEYBOARDS: dict[str, str] = {
    'to_baires_btn': 'Объявления Буэнос-Айрес',
    'back_btn': 'Назад',
    'send_announcement_btn': 'Получить объявление'
}