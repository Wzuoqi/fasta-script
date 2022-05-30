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
    flag = False
    dict1 = {}
    s = ""
    a = ""
    for line in lines:
        if line.startswith('>'):
            a = s[4873:4876]
            # 切片位置
            print(a.rstrip())
            print(line.rstrip())
            s = ""
        else:
            s += line
    a = s[4873:4876]
    # 额外做一次切片
    print(a.rstrip())
file_object.close()
