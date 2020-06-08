import csv
import re
import requests
import random
from time import sleep
from bs4 import BeautifulSoup
import mojimoji

prefs = [
    'osaka',
    # 'https://www.athome.co.jp/chintai/hyogo/line/'
]
base_url = 'https://www.housecom.jp'
base_url = 'https://www.athome.co.jp/chintai'

chintai = {}

def make_soup(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        }
    result = requests.get(url, headers=headers, timeout=10)
    result.encoding = result.apparent_encoding
    return BeautifulSoup(result.text, 'html.parser')

lines = []
for pref in prefs:
    link = f'{base_url}/{pref}/line/'
    print(link)
    soup = make_soup(link)
    line_list = soup.find(class_='area-group search-items limit-ensen f-fixedTrigger select-search-cond')
    print(line_list)
    all_lines = line_list.find_all('li')
    for link in all_lines:
        try:
            line_url = link.a['href']
            lines.append(line_url)
            print(line_url)
        except TypeError:
            continue
    sleep(5)

stations = []

for line in lines:
    link = f'{base_url}/{line}'
    soup = make_soup(link)
    station_list = soup.find_all(id='station-list')
    for link in station_list:
        try:
            station_url = link.a['href']
            stations.append(station_url)
            print(station_url)
        except TypeError:
            pass
    sleep(5)

# addresses = []
# for station in stations:
#     soup = make_soup(base_url+station)
#     building_list = soup.find_all(class_='ListBukkenBox')
#     for building in building_list:
#         name = building.h3.a.text
#         name = mojimoji.zen_to_han(name, kana=False)
#         print(name)
#         address = building.find(class_='MainDataInner')
#         address = address.find_all('td')[0].text
#         address = mojimoji.zen_to_han(address, kana=False)
#         print(address)
#         addresses.append(f'{address} {name}\n')
    
#     sleep(5)

# file = open('./address/address_buildings_kanagawa.txt', 'a')

# for address in addresses:
#     file.write(address)

# count = 0
# for building in buildings:
#     count += 1
#     if count == 1000:
#         break

#     url = base_url + building[0] + '/'
#     print(url)
#     soup = make_soup(url)
#     infos = soup.find_all(class_='build_info')
#     for info in infos:
#         building_name = info.find('h3').text.replace('\n', '')
#         address = info.find(class_='pt map').contents[0]
#         print(f'{building_name}: {address}')
#         file.write(f'東京都{address} {building_name}\n')

#     sleep(2)



    


