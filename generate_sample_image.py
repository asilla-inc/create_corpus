import requests
import random
import os
import pandas as pd
from time import sleep
import re
from PIL import Image, ImageDraw, ImageFont


dir_path = './numberonly_sample/'
canvasSize    = (500, 1200)
backgroundRGB = (10, 10, 10)

samples = os.listdir(dir_path)

canvas  = Image.new('RGB', canvasSize, backgroundRGB)
draw = ImageDraw.Draw(canvas)

image_height = 100
paste_coord_y = 10

for image_path in random.choices(samples, k=10):
    image = Image.open(dir_path+image_path)
    ratio = image_height / image.size[1]
    image_width = int(image.size[0] * ratio)
    image = image.resize((image_width, image_height))
    canvas.paste(image, (10, paste_coord_y))
    paste_coord_y += 120

paste_coord_y = 10
for image_path in random.choices(samples, k=10):
    image = Image.open(dir_path+image_path)
    ratio = image_height / image.size[1]
    image_width = int(image.size[0] * ratio)
    image = image.resize((image_width, image_height))
    canvas.paste(image, (250, paste_coord_y))
    paste_coord_y += 120

canvas.show()
    
filename = 'sample.png'
canvas.save(filename, "PNG")