# 创建时间：2021/3/20 11:06
from tkinter.filedialog import askopenfilename
import sys


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


sys.stdout = Logger('C_percentage.txt')
# 将结果保存在C_percentage.txt中

file = askopenfilename()
# 打开文件

with open(file) as file_object:
    lines = file_object

    t_line = ''
    length = 0
    total_C = 0
    for line in lines:
        if line.startswith('>'):
            if total_C != 0:
                C_percentage = total_C/length*100
                print(f"C_percentage = {C_percentage}%")
                length = 0
                total_C = 0
            else:
                print(' ')
            print(line.rstrip())

        else:
            length += len(line)
            total_C += line.count('C')

    C_percentage = total_C / length * 100
    print(f"C_percentage = {C_percentage}%")


file_object.close()

