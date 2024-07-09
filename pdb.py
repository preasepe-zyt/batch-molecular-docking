import pandas as pd
import numpy as np
from Bio import SeqIO
from Bio import PDB
import requests

import sys

import os


import urllib3

import argparse
import pandas as pd

# 创建 ArgumentParser 对象
parser = argparse.ArgumentParser(description='')

# 添加命令行选项
parser.add_argument('--file', type=str, help='一个字符串类型的选项，表示文件名')
parser.add_argument('--protein', type=str, help='一个文本存储代码的uniprot ID')
# 解析命令行参数
args = parser.parse_args()

# 输出解析结果或者执行默认行为
if args.protein and args.file:
    print(f'蛋白质文本: {args.protein}')
    print(f'文件夹路径: {args.file}')
elif args.protein:
    print(f'蛋白质文本: {args.protein}')
    print('请提供 --file 文件夹路径')
    sys.exit()
elif args.file:
    print(f'文件夹路径: {args.file}')
    print('请提供 --protein 参数来指定蛋白质文本')
    sys.exit()
else:
    print('请使用 --protein 和 --file 参数来指定蛋白质文本和目标的文件夹路径')
    sys.exit()

urllib3.disable_warnings()


headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0'}

current = os.getcwd()
def read_file(file_name):
    pro_swissProt = []
    with open(file_name, 'r') as fp:
        for line in fp:
            if line.startswith(""):  # 作用：判断字符串是否以指定字符或子字符串开头
                pro_swissProt.append(line)
    return pro_swissProt


file1 = args.protein

ID = read_file(file1)

j = 0
not_exist_list = []

for i in ID:
    j = j + 1
    print(j)
    print(i)
    url = 'https://alphafold.ebi.ac.uk/files/AF-' + i + '-F1-model_v1' + '.pdb'
    print(url)

    r = requests.get(url, headers=headers, verify=False)
    with open(current+"/"+args.file+"/" + i + '.pdb', 'w') as files:

        r = r.text.splitlines()  # np.array(pssm).tolist()
        for lines in r:
            files.write(lines)
            files.write('\n')

    if r[0][1] == '?':
        print(i + '没有pdb文件。')
        not_exist_list.append(i)

# 输出了未找到的蛋白质的.pdb文件，这些可以在网址里再手动查一下，有遗漏的
print(not_exist_list)
print(len(not_exist_list))
