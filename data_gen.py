import requests
import random
import os
import pandas as pd
from time import sleep
import re
from PIL import Image, ImageDraw, ImageFont


dir_path = './corpus/generated_images'
fontfile = '851MkPOP_002.ttf'
fontsize = 36
canvasSize    = (300, 150)
backgroundRGB = (0, 0, 0)
textRGB       = (255, 255, 255)

font = ImageFont.truetype(fontfile, fontsize)

words_list = []
with open('./corpus/corpus-ichijo-20200515.txt', 'r') as file:
    for line in file.readlines():
        words_list.append(line.split(' ')[1].strip('\n'))

count = 1
while count < 1000:
    word = random.choices(words_list, k=1)[0]

    img  = Image.new('RGB', canvasSize, backgroundRGB)
    draw = ImageDraw.Draw(img)

    w, h = draw.textsize(word, font)
    canvasSize = (w+80, h+30)
    img2 = Image.new('RGB', canvasSize, backgroundRGB)
    draw2 = ImageDraw.Draw(img2)
    text_position = (canvasSize[0]/6, canvasSize[1]/2 - h/2) # 前から1/6，上下中央に配置
    draw2.text(text_position, word, fill=textRGB, font=font)

    filename = './corpus/generated_images/corpus-' + word + '.png'
    img2.save(filename, "PNG")
    count += 1
