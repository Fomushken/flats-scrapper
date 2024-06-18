import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import json
import re

translator = Translator()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
url = 'https://www.argenprop.com/departamentos/alquiler/palermo/1-dormitorio-o-2-dormitorios?orden-masnuevos'



def get_images_urls(item):
    item_photos = item.find(
        'ul', attrs={'class': 'card__photos'}).find_all('img')
    result = list(map(lambda x: x['data-src'], item_photos))
    return result


def get_details(item):
    item_details = item.find('div', attrs={'class': 'card__details-box'})
    res = {}
    res['title'] = item_details.find('h2', attrs={'class': 'card__title'}).text
    res['address'] = item_details.find('p', attrs={'class': 'card__address'}).text.strip()
    res['currency'], res['price'] = item_details.find('span', attrs={'class': 'card__currency'}).text, item_details.find(
        'span', attrs={'class': 'card__currency'}).next_element.next_element.strip()
    expensas_pattern = r'<span class="card__expenses" title="\$(.*?) expensas">\s*\+\s*\$(.*?)\s*expensas\s*</span>'
    match = re.search(expensas_pattern, str(item_details.find('span', attrs={'class': 'card__expenses'})))
    res['expensas'] = f'${match.group(1)}' if match else None
    main_features = item_details.find('ul', attrs={'class': 'card__main-features'}).find_all('li')
    res['area'] = main_features[0].text.strip()
    res['rooms'] = main_features[1].text.strip()
    res['building_age'] = main_features[2].text.strip()
    res['about'] = item_details.find('p', attrs={'class': 'card__info'}).text



    return res

def scrap_argenprop(headers, url):
    html = requests.get(url, headers=headers).content
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('div', attrs={'class': 'listing__item'})

    flats_dict = {}

    for item in results:
        item_photos = get_images_urls(item)
        flats_dict[item['id']] = {}
        flats_dict[item['id']]['images'] = item_photos
        flats_dict[item['id']]['details'] = get_details(item)
        flats_dict[item['id']]['link'] = 'https://www.argenprop.com' + item.find('a')['href']
    return flats_dict