LEXICON: dict[str, str] = {
    '/start': '<b>Hello, {}!</b>\nI am a multifunctional bot, still in training,'  # the user's full name is inserted in place of {}
'Enter the /help command to learn about my functionality\n\n'
'<b>Below you can choose a category</b>',
    '/help': 'I can currently only send raw data about apartments in Buenos Aires from the Argenprop website. To do this, just click the button below.',
    '/mydev': 'You can contact my developer with button below',
    'unsubscribe': 'You\'ve unsibscribed',
    'subscribe': 'You have subscribed',
    'to_baires': 'Press the button below',
    'back': 'Returning back'
}

COMMANDS: dict[str, str] = {
    '/start': 'Start',
    '/help': 'What can I do?',
    '/mydev': 'Contact my developer'
}

KEYBOARDS: dict[str, str] = {
    'to_baires_btn': 'Buenos Aires Listings',
    'back_btn': 'Back',
    'subscribe_btn': 'Subscribe',
    'unsubscribe_btn': 'Unsubscribe',
    'dev_tg_btn': 'Telegram',
    'dev_linkedin_btn': 'LinkedIn',
    'dev_github_btn': 'GitHub'
}

