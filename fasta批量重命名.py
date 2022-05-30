# 创建时间：2021/6/1 8:20
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
    list = range(1, 100)
    x = 0
    for line in lines:
        if line.startswith('>'):
            a = ">Pch"+str(list[x])
            print(a.rstrip())
            x += 1
        else:
            print(line.rstrip())




file_object.close()