# 创建时间：2021/5/27 14:58
from tkinter.filedialog import askopenfilename
import sys

file = askopenfilename()
database = './Cl_backgroud_file.txt'

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


sys.stdout = Logger('GO_annotion.txt')
# 将结果保存在output.fasta中
id_list = []
final_list = []
with open(file) as file_object:
    lines = file_object
    for line in lines:
        id_list.append(line)
file_object.close()

with open(database) as data_object:
    datas = data_object
    for data in datas:
        list2 = data.split('\t')
        a = list2[0]+'\n'
        if a in id_list:
            final_list.append(data)
        else:
            continue
final_list.sort()
for x in final_list:
    print(x.rstrip())

data_object.close()

