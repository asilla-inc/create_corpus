from bs4 import BeautifulSoup
import requests
from time import sleep
import selenium
import json
from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager


url = 'https://rakuten.co.jp'
url = 'https://www.amazon.co.jp'
yen = '￥'
# driver = webdriver.Chrome('./chromedriver')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

def get_from_rakuten(html, data):
    # print(url)
    # res = requests.get(url)
    # res.encoding = res.apparent_encoding
    soup = BeautifulSoup(html, 'html.parser')
    lists = soup.find_all(class_="rnkTop_price")
    if lists == []:
        lists = soup.find_all(class_='rnkRanking_price')
        
    for content in lists:
        if "送料無料" in content.text:
            text = content.text.strip('送料無料')
            print(text)
            data.append(text)
        else:
            print(content.text)
            data.append(content.text)

def get_from_amazon(html):
    # print(url)
    # res = requests.get(url)
    # res.encoding = res.apparent_encoding
    data = []
    soup = BeautifulSoup(html, 'html.parser')
    lists = soup.find_all(class_="p13n-sc-price")
        
    for content in lists:
        print(content.text)
        data.append(content.text)
    return data


for i in range(100):
    waiting = input('OKならEnterを押してください')
    if waiting == '':
        print('we\'ll get this page\'s html in 3 secs')
        html = driver.page_source.encode('UTF-8')
        data = get_from_amazon(html)
        print('Let\'s go to next page')
        with open('currency_amazon.txt', 'a') as file:
            for text in data:
                file.write(text+'\n')

driver.close()


