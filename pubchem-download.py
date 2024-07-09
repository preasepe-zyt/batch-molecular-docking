import os
import pubchempy as pcp
import  pandas as pd
path = r"C:\Users\79403\Desktop\dnn+mr+vr\md+md"
path_file = r"C:\Users\79403\Desktop\dnn+mr+vr\md+md\file"
filename = "final_ingredients.xlsx"
full_path = os.path.join(path, filename)
# pubchem_cid = []
# pubchem_name = []
# column_index = 3
# name_index = 2
# with open(full_path, "r") as f:
#     for file in f:
#         col = file.split()
#         select = col[column_index]
#         select_name = col[name_index]
#         pubchem_cid.append(select)
#         pubchem_name.append(select_name)
# data = pd.DataFrame({"name":pubchem_name, "cid": pubchem_cid})
data = pd.read_excel(full_path)
data = data[data["CID"]!="---"]
pubchem_cid = data["CID"]
pubchem_name = data["Ingredient"]
blank_name = []
for index, cid in enumerate(pubchem_cid):
    sdfpath = os.path.join(path_file, "{}.sdf".format(cid))
    try:
        pcp.download('SDF', sdfpath, overwrite=True, identifier=cid, record_type='3d')
    except pcp.NotFoundError as e:
        print('No 3d Conformer for {}.'.format(cid))
        blank_name.append(cid)

#改名
files = os.listdir(path_file)
data = data[~data["CID"].isin(blank_name)]
# 遍历所有文件
for index, i in enumerate(files):
    # 构造新的文件名，这里可以根据你的需求修改文件名的逻辑
    parts = i.split(".")[0]
    name = data.loc[data["CID"] == int(parts), 'Ingredient'].values
    drug_name = name[0]+".sdf"
    # 构造旧的文件路径
    old_filepath = os.path.join(path_file, i)
    # 构造新的文件路径
    new_filepath = os.path.join(path_file, drug_name)
    # 重命名文件
    print(old_filepath, new_filepath)
    try:
       os.rename(old_filepath, new_filepath)
    except os.error as e:
        print(e,old_filepath, index)