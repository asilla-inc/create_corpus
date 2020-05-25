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
    for i in range(num_page+1):
        print(f"====Page {i+1}=====")
        pdf = FPDF()
        font_name = '0_Meiryo-01'
        pdf.add_page()
        pdf.add_font(font_name, '', './fonts/0_Meiryo-01.ttf', uni=True)
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
                pdf.cell(cell_width, cell_height*spacing, txt=f"number_{i+1}.pdf", border=1, align = "C")
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

        pdf.output(f"{des_path}/number_{i+1}.pdf")        
    # for index, row in enumerate(data):
        # #print(row)
        # current_column = index % (columns) 
        # if current_column + 1 == columns:
            # pdf.cell(cell_width, cell_height*spacing, txt='', border=1, align = "C")
            # pdf.ln(cell_height*spacing)
        # else:
            # pdf.cell(cell_width, cell_height*spacing, txt=row, border=1, align = "C")
        
if __name__ == '__main__':
    #add_font(FONT_FOLDER)
    # base_path = './numbers'
    des_path = './hello'
    if not os.path.isdir(des_path):
        os.makedirs(des_path)
    #gen_template(1)
    # for filename in os.listdir(base_path):
    file_link = "./numbers.txt"
        
    all_lines = read_txt(file_link)
    random.shuffle(all_lines)
    print("data ", len(all_lines))   
    simple_table(1, all_lines, des_path)
        