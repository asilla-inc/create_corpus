from bs4 import BeautifulSoup
import requests
import random
import os
from time import sleep
import words_to_search

base = "http://fuseji.net/"
maru = "○"
param_lists = []
param_dict = {}
timeout = 5
sleep_seconds = 6

for char in words_to_search.words2:
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
    param_lists.append({char: search_words})
    param_dict[char] = search_words

# print(param_dict)

count = len(param_dict)
# while len(os.listdir('./corpus_fuseji')) < 500:
# for key in random.choice(list(param_dict)):

existing = [word.split('.')[0].strip('corpus-fuseji-') for word in os.listdir('./corpus_fuseji')]

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
            text = key + ' ' + word.text + '\n'
            print(word.text)
            filename = f'./corpus_fuseji/corpus-fuseji-{key}.txt'
            with open(filename, 'a') as file:
                file.writelines(text)
        sleep(sleep_seconds)
