# 创建时间：2021/9/28 17:05
from tkinter.filedialog import askopenfilename
import sys
import re

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


sys.stdout = Logger('result1.fasta')
# 将结果保存在output.fasta中

with open(file) as file_object:
    lines = file_object
    t = ''
    title = ''
    key_string = ''
    test_string = ''
    key = re.compile('RGC*.{5}C') # 只需要在这里改正则表达式即可
    for line in lines:
        if line.startswith('>'):
            test_string = re.search(key, t)
            if test_string is not None:
                key_string = key.search(t).group()
                print(title.rstrip())
                print(key_string)
            title = line
            t = ''
        else:
            t += line
    test_string = re.search(key, t)
    if test_string is not None:
        key_string = key.search(t).group()
        print(title.rstrip())
        print(key_string)
file_object.close()
