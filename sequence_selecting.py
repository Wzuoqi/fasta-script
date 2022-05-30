# 创建时间：2021/6/2 9:18
# sequence_selecting.py

import sys
from sys import argv

blastp_list = list(set([((x.rstrip()).split())[1] for x in open(argv[1]).readlines()]))
sequence_list = [x.rstrip() for x in open(argv[2])]
seq_dict = {}
for x in sequence_list:
    if x.startswith('>'):
        dict_id = x[1:]
        seq_dict[dict_id] = ''
    else:
        seq_dict[dict_id] += x

for x in blastp_list:
    for y in seq_dict.keys():
        if x == y:
            print(">" + x + "\n" +seq_dict[y], file = open(x+'.fasta', 'a'))


