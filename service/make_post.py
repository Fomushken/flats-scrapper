from aiogram.types.input_media_photo import InputMediaPhoto
from googletrans import Translator

translator = Translator()

def make_post(item, language='en'):
    media_group = [InputMediaPhoto(media=url) for url in item['images']]
    text = f'<a href="{item["link"]}">{translator.translate(item["details"]["title"], dest=language).text}</a>\n\n{translator.translate(item["details"]["about"], dest=language).text}\n\nAddress: {item["details"]["address"]}\nSquare: {item["details"]["area"]}\nRooms: {item["details"]["rooms"]}\nBuilding\'s age : {translator.translate(item["details"]["building_age"], dest=language).text}\n\nPrice: {item["details"]["currency"]}{item["details"]["price"]} + {item["details"]["expensas"]} expensas'
    return {
        'media': media_group,
        'text': text
    }
