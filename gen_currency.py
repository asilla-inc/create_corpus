from fpdf import FPDF
import glob
import random
import os

columns = 2
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
    pdf.add_font(font_name, '', f'./fonts/{font_name}.ttf', uni=True)
    pdf.set_font("0_Meiryo-01", size=10)
    cell_width = pdf.w / 2.3
    cell_height = 10.6
    count = 0
    for index in range(0, columns * rows):    
        pdf.cell(cell_width, cell_height*spacing, txt='', border=1, align = "C")
        current_column = index % (columns)                 
        if current_column + 1 == columns:
            #pdf.cell(cell_width, cell_height*spacing, txt='', border=1, align = "C")
            pdf.ln(cell_height*spacing)
        
    basename = './address/address_template'    
    pdf.output(f"./{basename}.pdf")
    
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
                pdf.cell(cell_width, cell_height*spacing, txt=f"currency_{i+1}.pdf", border=1, align = "C")
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

        pdf.output(f"{des_path}/currency_{i+1}.pdf")        
    # for index, row in enumerate(data):
        # #print(row)
        # current_column = index % (columns) 
        # if current_column + 1 == columns:
            # pdf.cell(cell_width, cell_height*spacing, txt='', border=1, align = "C")
            # pdf.ln(cell_height*spacing)
        # else:
            # pdf.cell(cell_width, cell_height*spacing, txt=row, border=1, align = "C")
        
if __name__ == '__main__':
    gen_template(1)
    # des_path = './address'
    # if not os.path.isdir(des_path):
    #     os.makedirs(des_path)

    # data = []
    # # for i in range(3000):
    # #     bloodpressure_high = random.randint(90, 180)
    # #     bloodpressure_low = random.randint(40,110)
    # #     data.append(f'{bloodpressure_high}/{bloodpressure_low}')

    # # random.shuffle(data)

    # filepaths = ['currency_amazon.txt', 'currency_rakuten.txt', 'currency_autogen.txt']
    # data = {}
    # for filepath in filepaths:
    #     filename = filepath.split('.')[0]
    #     texts = []
    #     with open(filepath, 'r') as file:
    #         for line in file.readlines():
    #             texts.append(line.strip('\n'))
    #     data[filename] = texts
    
    # weights_amazon = [7 for i in range(len(
    #     data['currency_amazon']
    # ))]
    # weights_rakuten = [8 for i in range(len(
    #     data['currency_rakuten']
    # ))]
    # weights_gen = [1 for i in range(len(
    #     data['currency_autogen']
    # ))]

    # texts_list = data['currency_autogen'] + data['currency_amazon'] + data['currency_rakuten']
    # weights_list = weights_gen + weights_amazon + weights_rakuten

    # data_10k = random.choices(texts_list, weights=weights_list, k=1500)

    # simple_table(1, data_10k, des_path)
        