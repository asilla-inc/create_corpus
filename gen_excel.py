import os
import re
import openpyxl
from openpyxl.styles.borders import Border, Side 
import random

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "pdf0"

data = []
for i in range(3000):
    generated_float = round(random.uniform(1,99), 1)
    if i < 2500:
        data.append(str(generated_float))
    else:
        data.append(str(-generated_float))
random.shuffle(data)

columns = 4
rows = 25

side = Side(style='thin', color='000000')
border = Border(top=side, bottom=side, left=side, right=side)

for page in range(round(len(data)/(rows*columns))):
    data_begin = page * columns * rows
    data_end = (page+1) * columns * rows
    print(data_begin, data_end)
    data_for_row = data[data_begin:data_end]
    print(data_for_row)

    count = 0
    for row in range(1, rows+1):
        cells = [f'A{row}', f'B{row}', f'C{row}', f'D{row}']
        for cell in cells:
            sheet[cell] = str(data_for_row[count])
            sheet[cell].border = border
            count+=1
    sheet = workbook.create_sheet(f'pdf{page+1}')

workbook.save('number2.xlsx')

