# batch-molecular-docking

<h1>1 step 创建环境<br>
<h2>conda env create -n env -f env.yml <br>

<h1>2 step 解压vina和转移（直接上传vina会报错不能用）<br>

<h1>解压vina <br>
<h2>tar -zxvf autodock_vina_1_1_2_linux_x86.tgz<br>

<h1>转移vina到当前目录<br>
<h2>cp /root/autodl-tmp/autodock_vina_1_1_2_linux_x86/bin/vina /root/autodl-tmp <br>

<h1>创建文件夹<br>
<h2>mkdir -p protein ligand <br>

<h1>把小分子导入 ligand 文件夹，蛋白导入protein文件夹。（要求：3d结构。可以从uniprot、pbd下载蛋白，pubchem下载小分子。也可以用提供的脚本下载）<br>

<h1>蛋白质的下载目录通过argument-parse写成命令行了，小分子的需要自己看懂代码使用。<br>
<h2>cat > protein.txt #创建存储uniprot的文件。<br>

<h1>下载蛋白的代码<br>
<h2>python pdb.py --protein protein.txt --file protein <br>

<h1>开始批量下载<br>
<h2>bash vina.sh --protein_dir protein  --ligand_dir ligand <br>
