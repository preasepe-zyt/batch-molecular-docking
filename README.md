# batch-molecular-docking
<h1>1 step 
<h4>创建环境<br>
<h5>conda env create -n env -f env.yml <br>

<h1>2 step 
<h4>解压vina和转移（直接上传vina会报错不能用）<br>

<h4>解压vina <br>
<h5>tar -zxvf autodock_vina_1_1_2_linux_x86.tgz<br>

<h4>转移vina到当前目录<br>
<h5>cp /root/autodl-tmp/autodock_vina_1_1_2_linux_x86/bin/vina /root/autodl-tmp <br>

<h1>3 step 
<h4>下载蛋白和小分子<br>
<h5>mkdir -p protein ligand results<br>

<h4>把小分子导入 ligand 文件夹，蛋白导入protein文件夹。（要求：3d结构。可以从uniprot、pbd下载蛋白，pubchem下载小分子。也可以用提供的脚本下载）<br>

<h4>蛋白质的下载目录通过argument-parse写成命令行了，小分子的需要自己看懂代码使用。<br>
<h5>cat > protein.txt #创建存储uniprot的文件。<br>

<h4>下载蛋白的代码<br>
<h5>python pdb.py --protein protein.txt --file protein <br>


<h1>4 step 
<h4>配置分子对接的环境<br>
<h5>wget https://ccsb.scripps.edu/mgltools/download/495/mgltools_x86_64Linux2_1.5.6p1.tar.gz 
<h4>tar mgltools_x86_64Linux2_1.5.6.tar.gz
<h4>cd mgltools_x86_64Linux2_1.5.6
<h4>sudo bash install.sh
<h4>#修改bashrc。安装完软件后会提示你需要将哪些内容添加到bashrc文件里，这里只展示我自己的。
<h4>vim ~/.bashrc
<h4>下面的粘贴进去
  
<h4>alias pmv='/root/autodl-tmp/mgltools_x86_64Linux2_1.5.6/bin/pmv'
<h4>alias adt='/root/autodl-tmp/mgltools_x86_64Linux2_1.5.6/bin/adt'
<h4>alias vision='/root/autodl-tmp/mgltools_x86_64Linux2_1.5.6/bin/vision'
<h4>alias pythonsh='/root/autodl-tmp/mgltools_x86_64Linux2_1.5.6/bin/pythonsh'
  
<h4>source ~/.bashrc
<h4>export PATH=/root/autodl-tmp/mgltools_x86_64Linux2_1.5.6/bin:$PATH
<h4>开始批量分子对接<br>
<h4>需要ligand和protein文件夹下存在对应的文件<br>
<h5>bash vina.sh --protein_dir protein  --ligand_dir ligand <br>
<h4>output.csv 为十个构象中最低的那个整合在一起，results文件夹是对接的原始结果，包括十个对接函数打分和可视化所需要的文件。
