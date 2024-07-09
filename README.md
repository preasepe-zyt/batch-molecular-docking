# batch-molecular-docking

1 step 创建环境<br>
conda env create -n env -f env.yml <br>

2 step 解压vina和转移（直接上传vina会报错不能用）<br>
解压vina <br>
tar -zxvf autodock_vina_1_1_2_linux_x86.tgz<br>
转移vina到当前目录<br>
cp /root/autodl-tmp/autodock_vina_1_1_2_linux_x86/bin/vina /root/autodl-tmp <br>
