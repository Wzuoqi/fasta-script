# 创建时间：2021/3/20 11:06
from tkinter.filedialog import askopenfilename

file = askopenfilename()

with open(file) as file_object:
    lines = file_object

    t_line = ''
    for line in lines:
        if line.startswith('>'):
            continue
        else:
            t_line += line.strip()
file_object.close()

length_t_line = len(t_line)
total = t_line.count('C')

C_percentage = total / length_t_line * 100

print(C_percentage)
