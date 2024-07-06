from bs4 import BeautifulSoup
from googletrans import Translator
import json
from .make_post import make_post
from redis.asyncio import Redis
import re
import aiohttp
import asyncio

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
    currency_span = item_details.find('span', attrs={'class': 'card__currency'})
    price_span = currency_span.next_element.next_element if currency_span else None
    res['currency'] = currency_span.text if currency_span else 'N/A'
    res['price'] = price_span.strip() if price_span else 'N/A'
    expensas_pattern = r'<span class="card__expenses" title="\$(.*?) expensas">\s*\+\s*\$(.*?)\s*expensas\s*</span>'
    match = re.search(expensas_pattern, str(item_details.find('span', attrs={'class': 'card__expenses'})))
    res['expensas'] = f'${match.group(1)}' if match else None
    main_features = item_details.find('ul', attrs={'class': 'card__main-features'}).find_all('li')
    res['area'] = main_features[0].text.strip() if len(main_features) > 0 else 'N/A'
    res['rooms'] = main_features[1].text.strip() if len(main_features) > 1 else 'N/A'
    res['building_age'] = main_features[2].text.strip() if len(main_features) > 2 else 'N/A'
    res['about'] = item_details.find('p', attrs={'class': 'card__info'}).text if item_details.find('p', attrs={'class': 'card__info'}) else 'N/A'

    return res

async def scrap_argenprop(headers, url, redis: Redis):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, 'html.parser')
                results = soup.find_all('div', attrs={'class': 'listing__item'})

    flats_dict = {}
    new_ads = []

    for item in results:
        item_id = item.get('id')
        if item_id:
            item_photos = get_images_urls(item)
            details = get_details(item)
            link = 'https://www.argenprop.com' + item.find('a')['href']
            if not await redis.sismember('ads_ids', item_id):
                new_ads.append({
                    'id': item_id,
                    'images': item_photos,
                    'details': details,
                    'link': link
                })
                await redis.sadd('ads_ids', item_id)
            flats_dict[item['id']] = {
                'images': item_photos,
                'details': details,
                'link': link
            }
    await redis.set('latest_ads', json.dumps(flats_dict))
    return new_ads

async def notify_users(new_ads, redis: Redis, bot):
    subscribers = await redis.smembers('subscribers')
    for ad in new_ads:
        message = make_post(ad)
        for subscriber in subscribers:
            await bot.send_media_group(subscriber, message['media'])
            await bot.send_message(subscriber, message['text'])

async def scheduled_scrap(bot):
    redis = Redis()
    new_ads = await scrap_argenprop(headers, url, redis)
    if new_ads:
        await notify_users(new_ads, redis, bot)
    await redis.close()