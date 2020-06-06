from bs4 import BeautifulSoup
import requests
import random
import os
import pandas as pd
from time import sleep
import re

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
sample = ["く", "ロ", "口", "菱", "ス", "タ", "夕"]
param_dict = {}

for word in sample:
    url = "https://www.sanseido.biz/User/Dic/Index.aspx?TWords=" + word + "&st=5&DORDER=&DailyJJ=checkbox&DailyEJ=checkbox&DailyJE=checkbox"
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, 'html.parser')
    lists = soup.find_all(class_="word text-m")
    for content in lists:
        if "［" in content.text:
            text = re.match(r'.*［(.*)］.*', content.text).group(1)
            print(text)

# print(param_dict)

# count = len(param_dict)
# for key, params in param_dict.items():
#     count -= 1
#     print(f"{count} words left")
#     for param in params:
#         url = base + param
#         res = requests.get(url)
#         res.encoding = res.apparent_encoding
#         soup = BeautifulSoup(res.text, 'html.parser')
#         lists = soup.find_all('tt')
#         for list_ in lists:
#             text = key + ' ' + list_.text + '\n'
#             print(list_.text)
#             filename = 'courpus-ichijo-' + key + '-20200515.txt'
#             with open(filename, 'a') as file:
#                 file.writelines(text)
#         sleep(1)
    