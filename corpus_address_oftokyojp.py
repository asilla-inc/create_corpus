import csv
import re
import requests
import random
from time import sleep
from bs4 import BeautifulSoup

csv_file = '/Users/tatsuki/python/prepare_images/buildings_reviewed.csv'
buildings = list(csv.reader(open(csv_file, 'r')))
# random.shuffle(buildings)
base_url = 'https://of-tokyo.jp/search/p/search_string:'

def make_soup(url):
    headers = {'User-Agent':'Mozilla/5.0'}
    result = requests.get(url, headers=headers)
    result.encoding = result.apparent_encoding
    return BeautifulSoup(result.text, 'html.parser')

file = open('./address/address_buildings_order.txt', 'a')

exclude = ['計画', 'PJ', '仮', 'プロジェクト', '名称']

count = 0
total = len(buildings)
# for building in buildings:
#     count += 1
#     print(f'{total-count} more left')

#     url = base_url + building[0] + '/'
#     print(url)
#     soup = make_soup(url)
#     infos = soup.find_all(class_='build_info')
#     for info in infos:
#         building_name = info.find('h3').text.replace('\n', '')
#         address = info.find(class_='pt map').contents[0]
#         print(f'{building_name}: {address}')

#         if any(word in building_name for word in exclude):
#             print(f'Found excluding data: {building_name}')
#         else:
#             file.write(f'東京都{address} {building_name}\n')

#     sleep(3)

file = open('./address/address_buildings.txt', 'r')

texts = file.readlines()
texts = [line.strip('\n') for line in texts]

print(len(texts))

new_texts = []
for index, text in enumerate(texts):
    if index % 2 == 1:
        new_texts.append(text+'\n')
    else:
        if text[-1].isdigit():
            print(f'Ends with number: {text}')
            new_texts.append(text+'\n')
        else:
            text = f'{text}{random.randint(1,30)}階'
            print(text)
            new_texts.append(text+'\n')
    
with open('./address/address_buildings_floored.txt', 'w') as file:
    for text in new_texts:
        file.write(text)



    


