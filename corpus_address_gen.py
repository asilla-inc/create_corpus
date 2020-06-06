import csv
import re
import requests
import random
from random import randint, choice, choices

csv_file = './address_ord.csv'
addresses = list(csv.reader(open(csv_file, 'r')))

chome_kanji = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
chome_kanji2 = ['一', '二', '三', '四', '五', '六', '七', '八', '九']


count = 0
total_patterns = 6000
first_pattern = 2000
second_pattern = 2000
third_pattern = 500

file = open('address_gen.txt', 'a')

for address in choices(addresses, k=total_patterns):
    print(count)
    address = address[1]
    if count < first_pattern:
        kansuji_chome_pattern = f'{randint(1,9)}丁目{randint(1,50)}'
        address = address.replace('X丁目', kansuji_chome_pattern)
        print(address)
        file.write(address+'\n')
    elif first_pattern < count < second_pattern:
        kansuji_chome_pattern = f'{randint(1,9)}丁目{randint(1,20)}-{randint(1,50)}'
        address = address.replace('X丁目', kansuji_chome_pattern)
        print(address)
        file.write(address+'\n')
    elif second_pattern < count < third_pattern:
        kanji_chome_pattern = f'{choice(chome_kanji)}丁目{choice(chome_kanji)}の十{choice(chome_kanji2)}'
        address = address.replace('X丁目', kanji_chome_pattern)
        print(address)
        file.write(address+'\n')
    else:
        number_chome_pattern = f'{randint(1,9)}-{randint(1,20)}-{randint(1,50)}'
        address = address.replace('X丁目', number_chome_pattern)
        print(address)
        file.write(address+'\n')
    count += 1