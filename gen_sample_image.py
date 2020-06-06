import requests
import random
import os
import pandas as pd
from time import sleep
import re
from PIL import Image, ImageDraw, ImageFont, ImageChops


dir_path = './currency_sample/'
canvasSize    = (1200, 1200)
backgroundRGB = (10, 10, 10)

samples = os.listdir(dir_path)

canvas  = Image.new('RGB', canvasSize, backgroundRGB)
draw = ImageDraw.Draw(canvas)

# for i in range(1,4):
image_height = 100
paste_coord_y = 10

count = 0
for image_path in random.choices(samples, k=30):
    
    image = Image.open(dir_path+image_path)
    print(image.mode)
    if ImageChops.invert(image).getbbox() is None:
        print("Empty box found")
        continue
    else:
        ratio = image_height / image.size[1]
        image = image.convert('1')
        image.show()
        print(image.mode)
        # image_width = int(image.size[0] * ratio)
        # image = image.resize((image_width, image_height))
        # canvas.paste(image, (10, paste_coord_y))
        # paste_coord_y += 120
        count += 1

    if count == 10:
        break
    # paste_coord_y = 10
    # for image_path in random.choices(samples, k=10):
    #     image = Image.open(dir_path+image_path)
    #     ratio = image_height / image.size[1]
    #     image_width = int(image.size[0] * ratio)
    #     image = image.resize((image_width, image_height))
    #     canvas.paste(image, (450, paste_coord_y))
    #     paste_coord_y += 120

# canvas.show()
        
filename = 'sample_currency_1.png'
canvas.save(filename, "PNG")