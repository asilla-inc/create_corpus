from fpdf import FPDF
import glob
import random
import os

columns = 3
rows = 25

def read_txt(filepath):
    data = []
    with open(filepath, 'r', encoding='utf8') as file:
        lines = file.readlines()
        for l in lines:
            l = l.replace('\n','')
            data.append(l)
    return data

def gen_template(spacing):
    pdf = FPDF()
    font_name = '0_Meiryo-01'
    pdf.add_page()
    pdf.add_font('0_Meiryo-01', '', '0_Meiryo-01.ttf', uni=True)
    pdf.set_font("0_Meiryo-01", size=10)
    cell_width = pdf.w / 3.9
    cell_height = 10
    count = 0
    for index in range(0, columns * rows):    
        pdf.cell(cell_width, cell_height*spacing, txt='', border=1, align = "C")
        current_column = index % (columns)                 
        if current_column + 1 == columns:
            #pdf.cell(cell_width, cell_height*spacing, txt='', border=1, align = "C")
            pdf.ln(cell_height*spacing)
        
    basename = 'mix_ambiguous'            
    pdf.output("./{}.pdf".format(basename))    
    
def simple_table(spacing, data_full, des_path):
    num_page = round(len(data_full)/columns*rows)
    print("pages", num_page)
    for i in range(num_page):
        print(f"====Page {i+1}=====")
        pdf = FPDF()
        font_name = '0_Meiryo-01'
        pdf.add_page()
        pdf.add_font(font_name, '', f'./fonts/{font_name}.ttf', uni=True)
        pdf.set_font(font_name, size=10)
        cell_width = pdf.w / 3.9
        cell_height = 10
        count = 0
        index_start = i * rows * columns
        index_end = (i + 1) * rows * columns
        print(index_start, index_end)
        data = data_full[index_start:index_end] 
        for index in range(0, columns * rows):
            
            current_column = index % (columns)
                       
            if index == 2:
                pdf.cell(cell_width, cell_height*spacing, txt=f"address_{i+1}.pdf", border=1, align = "C")
                pdf.ln(cell_height*spacing)
                count += 1

            elif current_column + 1 == columns:
                pdf.cell(cell_width, cell_height*spacing, txt=data[count], border=1, align = "C")
                pdf.ln(cell_height*spacing)
                count += 1

            else:
                if count < len(data):
                    print(data[count])
                    pdf.cell(cell_width, cell_height*spacing, txt=data[count], border=1, align = "C")
                    count += 1
                else:
                    pdf.cell(cell_width, cell_height*spacing, txt='', border=1, align = "C")

        pdf.output(f"{des_path}/address_{i+1}.pdf")        
    # for index, row in enumerate(data):
        # #print(row)
        # current_column = index % (columns) 
        # if current_column + 1 == columns:
            # pdf.cell(cell_width, cell_height*spacing, txt='', border=1, align = "C")
            # pdf.ln(cell_height*spacing)
        # else:
            # pdf.cell(cell_width, cell_height*spacing, txt=row, border=1, align = "C")
        
if __name__ == '__main__':
    des_path = './address/source_pdf_new'
    if not os.path.isdir(des_path):
        os.makedirs(des_path)

    data = []
    filepaths = ['./address/address_gen.txt', './address/address_buildings.txt']
    # for filepath in filepaths:
    filepath = './address/address_buildings_removedups.txt'
    with open(filepath, 'r') as file:
        lines = file.readlines()
        lines = [line.strip('\n') for line in lines]
        data += lines

    data_10k = random.choices(data, k=1)
    splitted_data = []

    for data in data_10k:
        data = data.replace(' ', '')
        prev = 0
        while True:
            n = random.randint(2,6)
            splitted_data.append(data[prev:prev+n])
            print(data[prev:prev+n])
            prev = prev + n
            if prev >= len(data):
                splitted_data.append('')
                break
    print(splitted_data)
        
    # for data in data_10k:
    #     if len(data) <= 15:
    #         i = len(data) / 2 - 1
    #         splitted = [data[0:round(i)], data[round(i):]]
    #         splitted_data += splitted

    #     elif 15 < len(data) <= 21:
    #         i = len(data) / 3
    #         splitted = [data[0:round(i)], data[round(i):round(i)*2], data[round(i)*2:]]
    #         splitted_data += splitted

    #     elif 21 < len(data) <= 28:
    #         i = len(data) / 4
    #         splitted = [data[0:round(i)], data[round(i):round(i)*2], data[round(i)*2:round(i)*3], data[round(i)*3:]]
    #         splitted_data += splitted

    #     else:
    #         i = len(data) / 5
    #         splitted = [data[0:round(i)], data[round(i):round(i)*2], data[round(i)*2:round(i)*3], data[round(i)*3:round(i)*4], data[round(i)*5:]]
    #         splitted_data += splitted

    # simple_table(1, splitted_data, des_path)
        