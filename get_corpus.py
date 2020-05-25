from bs4 import BeautifulSoup
import requests
import random
import os
from time import sleep
import words_to_search

# path = "/Users/tatsuki/Downloads/big_img"
# files=[[int(file.split("_")[0]),file.split("_")[1].split(".")[0]]for file in os.listdir(path)]
# paris = []
# for file in files:
#     paris.append(file)
# # print(paris)
# df = pd.DataFrame(paris, columns=['Freq', 'Char'])
# df = df.sort_values('Freq', ascending=False)
# print(df[0:100]['Char'].to_list())

base = "http://fuseji.net/"
maru = "○"
sample = ["ロ", "口", "菱", "ス", "タ", "夕"]
words = ['頼']
param_lists = []
param_dict = {}

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

existing = [word.split('.')[0].strip('courpus-fuseji-') for word in os.listdir('./corpus_fuseji')]

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
            res = requests.get(url, headers=headers, timeout=5)
            res.encoding = res.apparent_encoding
        except Exception as e:
            print(e)
            continue

        soup = BeautifulSoup(res.text, 'html.parser')
        words = soup.find_all('tt')
        for word in words:
            text = key + ' ' + word.text + '\n'
            print(word.text)
            filename = f'./corpus_fuseji/courpus-fuseji-{key}.txt'
            with open(filename, 'a') as file:
                file.writelines(text)
        sleep(6)
