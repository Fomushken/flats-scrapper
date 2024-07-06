from aiogram.types.input_media_photo import InputMediaPhoto
from googletrans import Translator

translator = Translator()

item: dict[str, dict[str, str]|list[str, str]] = {
   "images": [
      "https://static1.sosiva451.com/63791851/957bfe87-d783-46bf-88ef-48b98e256de8_u_small.jpg",
      "https://static1.sosiva451.com/63791851/83879fd2-64a1-4069-8b50-a040841699e9_u_small.jpg",
      "https://static1.sosiva451.com/63791851/3869d045-ea5f-40a6-b776-e5b223524e0e_u_small.jpg",
      "https://static1.sosiva451.com/63791851/e0eb01de-47be-400c-8139-e3d499500218_u_small.jpg",
      "https://static1.sosiva451.com/63791851/9b03bd04-8496-4dd4-b85d-3e440f41eafb_u_small.jpg",
      "https://static1.sosiva451.com/63791851/692d71d9-fc88-40da-9bc2-1d68e9d9550a_u_small.jpg",
      "https://static1.sosiva451.com/63791851/9210c999-b017-4d04-b390-f6436f39cc90_u_small.jpg",
      "https://static1.sosiva451.com/63791851/09824f9e-405d-4b27-9486-d831e30f2e65_u_small.jpg"
   ],
   "details": {
      "title": "Departamento 2 ambientes en ALQUILER en Ca\u00f1itas",
      "address": "Baez al 600",
      "currency": "$",
      "price": "790.000",
      "expensas": "$200.000",
      "area": "45  m\u00b2 cubie.",
      "rooms": "1 dorm.",
      "building_age": "10 a\u00f1os",
      "about": "\n            Espectacular departamento de 2 ambientes con cochera en alquiler las ca\u00f1itas.\nTiene una distribucion muy c\u00f3moda con ba\u00f1o en suite y toilette de recepci\u00f3n. La cocina integrada, super comoda y completa. \nTiene balc\u00f3n aterrazado con parrilla propia. Lavadero incorporado.\nEl edificio es super moderno y cuenta con pileta, gimnasio, parrilla, sum, solarium con jacuzzi\n        "
   },
   "link": "https://www.argenprop.com/departamento-en-alquiler-en-las-canitas-2-ambientes--15819736"
}

def make_post(item, language='ru'):
    media_group = [InputMediaPhoto(media=url) for url in item['images']]
    text = f'<a href="{item['link']}">{translator.translate(item['details']['title'], dest=language).text}</a>\n\n{translator.translate(item['details']['about'], dest=language).text}\n\nАдрес: {item['details']['address']}\nПлощадь: {item['details']['area']}\nКомнат: {item['details']['rooms']}\nВозраст дома: {translator.translate(item['details']['building_age'], dest=language).text}\n\nЦена: {item['details']['currency']}{item['details']['price']} + {item['details']['expensas']} expensas'
    return {
        'media': media_group,
        'text': text
    }