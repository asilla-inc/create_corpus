import requests
import random
import os
import pandas as pd
from time import sleep
import re
from PIL import Image, ImageDraw, ImageFont


dir_path = './numberonly_sample/'
canvasSize    = (800, 1200)
backgroundRGB = (0, 0, 0)

samples = os.listdir(dir_path)

canvas  = Image.new('RGB', canvasSize, backgroundRGB)
draw = ImageDraw.Draw(canvas)

image_height = 100
for image_path in random.choices(samples, k=10):
    image = Image.open(dir_path+image_path)
    ratio = image_height / image.size[1]
    image_width = int(image.size[0] * ratio)
    image = image.resize((image_width, image_height))
    canvas.show()
    
filename = 'sample.png'
canvas.save(filename, "PNG")