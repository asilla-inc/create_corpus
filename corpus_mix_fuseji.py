from bs4 import BeautifulSoup
import requests
import random
import os
from time import sleep
import hung_20200618

base = "http://fuseji.net/"
maru = "○"
param_dict = {}
timeout = 5
sleep_seconds = 3.5
words = ['竺']

with open('1_confuse-character.txt') as file:
    lines = file.readlines()
    lines = [line.strip('\n') for line in lines]
    random.shuffle(lines)

for line in lines:
    char = line.split('=')[0]
    search_words = []
    search_words.append(maru+char)
    search_words.append(char+maru)
    search_words.append(char+maru+maru)
    search_words.append(maru+char+maru)
    search_words.append(maru+maru+char)
    for i in range(3,7):
        search_word = char + maru*i
        for times in range(i+1):
            shuffled = ''.join(random.sample(search_word, len(search_word)))
            while shuffled in search_words:
                shuffled = ''.join(random.sample(search_word, len(search_word)))
            else:
                search_words.append(shuffled)
    print(search_words)
    if 'gt' in line:
        char = char + '-gt'
    else:
        char = char + '-predict'
    param_dict[char] = search_words


count = len(param_dict)
# while len(os.listdir('./corpus_fuseji')) < 500:
# for key in random.choice(list(param_dict)):

existing = [word.split('.')[0].strip('corpus-fuseji-') for word in os.listdir('./corpus_fuseji_hung2')]

for key in list(param_dict):
    count -= 1
    if key in existing:
        print(f"Skipping {key}")
        continue
    print(f"{count} words left")
    for param in param_dict[key]:
        url = base + param
        headers = {'User-Agent':'Mozilla/5.0'}
        try:
            res = requests.get(url, headers=headers, timeout=timeout)
            res.encoding = res.apparent_encoding
        except Exception as e:
            print(e)
            continue

        soup = BeautifulSoup(res.text, 'html.parser')
        words = soup.find_all('tt')
        for word in words:
            text = key.split('-')[0] + ' ' + word.text + '\n'
            print(word.text)
            filename = f'./corpus_fuseji_hung2/corpus-fuseji-{key}.txt'
            with open(filename, 'a') as file:
                file.writelines(text)
        sleep(sleep_seconds)
        
    # with open(f'./corpus_fuseji_hung2/corpus-fuseji-{key}.txt', 'r') as file:
    #     lines = file.readlines()
    
    # os.rename(f'./corpus_fuseji_hung2/corpus-fuseji-{key}.txt', f'./corpus_fuseji_hung/corpus-fuseji-{key}-{len(lines)}.txt')
            
