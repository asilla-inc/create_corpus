from bs4 import BeautifulSoup
import requests
import random
import os
import pandas as pd
from time import sleep
import re
import json

sample = ["く", "ロ", "口", "菱", "ス", "タ", "夕"]
errors_100_most_freq = ["ロ", "口", "菱", "ス", "タ", "夕", ',', '・', '・', '？', '。', 'L', '夕', 'T', '1', 'P', 'り', 'く', 'が', 'F', '', 'ン', 'か', 'し', 'ス', 'エ', 'く', 'l', 'ふ', '件', '竺', '菱', '口', '案', 'フ', '0', 'ア', 'し', 'ご', 'は', 'リ', 'い', 'ニ', 'と', 'ユ', 'ん', 'ま', 'ゴ', 'ク', 'に', 'T', '勤', '様', '上', 'ご', '(', 'k', 'へ', 'レ', '社', '案', 'J', 'づ', 'ナ', 'プ', 'ス', '年', '〆', '二', ')', 'W', '月', 'I', '務', '浜', 'ヵ', '田', '日', 'ノ', 'キ', '0', 'を', '枝', 'O', '室', '頂', 'ミ', 'P', 'ろ', '税', 'ち', '員', '客', 'ビ', 'け', '区', '大', '勤', '左', 'サ', 'カ', '醤', '東', '告']
param_dict = {}

words_list = []
with open('./corpus/corpus-ichijo-20200515.txt', 'r') as file:
    for line in file.readlines():
        words_list.append(line.split(' ')[1].strip('\n'))

while len(os.listdir('./corpus_wikinew')) <= 200:
    print(len(os.listdir('./corpus_wikinew')))
    word = random.choices(words_list, k=1)[0]
    url = "http://wikipedia.simpleapi.net/api?keyword=" + word + "&output=json"
    print(word)
    headers = {'User-Agent':'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    sleep(4)
    try:
        json_dict = json.loads(res.text)
        if json_dict == None:
            print("Empty found")
            continue
        else:
            filename = './corpus_wikinew/corpus-' + word + '.json'
            with open(filename, 'w') as file:
                json.dump(json_dict, file, indent=4, ensure_ascii=False)
            print("Found a result")
    except json.decoder.JSONDecodeError:
        continue

# for word in errors_100_most_freq:
#     url = "http://wikipedia.simpleapi.net/api?keyword=" + word + "&output=json"
#     res = requests.get(url)
#     # print(res.text.decode('utf-8'))
#     try:
#         json_dict = json.loads(res.text)
#         print(json_dict)
#         filename = './corpus_wiki/corpus-' + word + '.json'
#         with open(filename, 'w') as file:
#             json.dump(json_dict, file, indent=4, ensure_ascii=False)
#     except json.decoder.JSONDecodeError:
#         continue
#     sleep(4)