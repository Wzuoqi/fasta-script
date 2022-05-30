# 创建时间：2021/5/27 14:58
from tkinter.filedialog import askopenfilename
import sys

file = askopenfilename()


class Logger(object):
    """
    将文件运行中的输出部分保存到特定txt文件中
    """

    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger('output.fasta')
# 将结果保存在output.fasta中

with open(file) as file_object:
    lines = file_object
    number = 0
    number_list = []
    id_list = ['test']
    for line in lines:
        if line.startswith('>'):
            number_list.append(number)
            id_list.append(line)
            number = 0
        else:
            number += len(line)
    number_list.append(number)
    if len(number_list) == len(id_list):
        x = len(id_list)
    else:
        print('the number of list is not equal')
    for i in range(0, x):
        print(id_list[i].rstrip(), number_list[i], sep='\t')
file_object.close()
