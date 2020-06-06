from bs4 import BeautifulSoup
import requests
import random
import os
import pandas as pd
from time import sleep
import re
import words_to_search, jijilla_char_list
import json

def make_soup(url):
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup

def find_words(soup, results_list):
    lists = soup.find_all(class_="title")
    for item in lists:
        print(item.text)
        try:
            if "【" in item.text:
                text = re.match(r'.*【(.*)】.*', item.text).group(1)
                print(text)
                results_list.append(text)
        except:
            continue
    sleep(2)

def write_text_file(word_to_search, results_list):
    filename = f'./corpus_goo/courpus-goo-{word_to_search}.txt'
    for result in results_list:
        text_line = word_to_search + ' ' + result + '\n'
        with open(filename, 'a') as file:
            file.writelines(text_line)

for word in words_to_search.words:
    if word in jijilla_char_list.katakanas or word in jijilla_char_list.hiraganas:
        continue

    results_list = []
    print(f"Finding result for {word}")
    url = f"https://dictionary.goo.ne.jp/srch/jn/{word}/m6u/"
    soup = make_soup(url)
    find_words(soup, results_list)

    try:
        last_page = soup.find(class_="last-num").find('a')['title']
        last_page_num = last_page.strip('page ')
        print(f"There are in total {last_page_num} pages")
    except AttributeError:
        print(f"Seems like only found 1 page")
        write_text_file(word, results_list)
        continue

    for page in range(2, int(last_page_num)+1):
        print(f"Now on page {page} out of {last_page_num}")
        after_pages_link = f"https://dictionary.goo.ne.jp/srch/jn/{word}/m6p{page}u/"
        soup = make_soup(after_pages_link)
        find_words(soup, results_list)

    write_text_file(word, results_list)

# try:
#     save_dir = os.mkdir("corpus_goo")
# except FileExistsError:
#     save_dir = "corpus_goo"

# characters = ''.join(words)

# print(results_dict)
# filename = f"./{save_dir}/corpus_goo_{characters}.json"
# with open(filename, 'w') as file:
#     json.dump(results_dict, file, indent=4, ensure_ascii=False)