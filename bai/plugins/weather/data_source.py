import json
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup

moji_api_get_city_code_url = 'http://tianqi.moji.com/api/citysearch/'
moji_api_get_weather_url = 'http://tianqi.moji.com/api/redirect/'


async def get_weather_of_city(city: str) -> str:
    citycode = get_city_code_by_str(city)
    if citycode is None:
        return '呃，没有听说过这个地方🦢'
    else:
        return city+","+get_weather_from_moji(citycode)


def get_city_code_by_str(city: str) -> int:
    response = requests.get(moji_api_get_city_code_url + quote(city))
    try:
        return json.loads(response.text).get('city_list')[0].get('cityId')
    except:
        return None


def get_weather_from_moji(city: int) -> str:
    response = requests.get(moji_api_get_weather_url + str(city))
    soup = BeautifulSoup(response.text, 'html.parser')
    temperature = soup.find(class_='wea_weather').find('em').get_text()
    meteorological = soup.find(class_='wea_weather').find('b').get_text()
    humidity = soup.find(class_='wea_about').find('span').get_text()
    wind = soup.find(class_='wea_about').find('em').get_text()
    tips = soup.find(class_='wea_tips').find('em').get_text()
    return f'温度{temperature}℃，{meteorological}，{humidity}，{wind}，{tips}'
