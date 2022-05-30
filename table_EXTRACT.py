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


sys.stdout = Logger('BLASTlist6.fasta')
# 将结果保存在output.fasta中

with open(file) as file_object:
    lines = file_object
    blast_string = ""
    set1 = set()
    title = ""
    for line in lines:
        if line.startswith("#"):
            continue
        else:
            t = line.split('\t')
            set1.add(t[1])

for x in set1:
    print(x)






file_object.close()