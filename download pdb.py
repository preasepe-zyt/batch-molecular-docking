import pandas as pd
import numpy as np
from Bio import SeqIO
from Bio import PDB
import requests


import urllib3

urllib3.disable_warnings()

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0'}


def read_file(file_name):
    pro_swissProt = []
    with open(file_name, 'r') as fp:
        for line in fp:
            if line.startswith("<"):  # 作用：判断字符串是否以指定字符或子字符串开头
                pro_swissProt.append(line[1:-1])
    return pro_swissProt


file1 = 'C:/Users/79403/Desktop/protein.txt'

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
    with open('C:/Users/79403/Desktop/protein/' + i + '.pdb', 'w') as files:

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
