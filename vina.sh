#!/bin/bash

# Function to display usage information
usage() {
    echo "Usage: $0 --protein_dir DIR --ligand_dir DIR [--output_dir DIR]"
    exit 1
}

# Parse command line arguments using getopt
PARSED_ARGUMENTS=$(getopt -o '' --long protein_dir:,ligand_dir:,output_dir: -- "$@")
VALID_ARGUMENTS=$?
if [ "$VALID_ARGUMENTS" != "0" ]; then
    usage
fi

# Assign arguments to variables
eval set -- "$PARSED_ARGUMENTS"
while :
do
    case "$1" in
        --protein_dir) protein_dir="$2" ; shift 2 ;;
        --ligand_dir) ligand_dir="$2" ; shift 2 ;;
        --output_dir) output_dir="$2" ; shift 2 ;;
        --) shift; break ;;
        *) echo "Unexpected option: $1 - this should not happen." ; usage ;;
    esac
done

# Check required arguments
if [ -z "$protein_dir" ] || [ -z "$ligand_dir" ]; then
    usage
fi

# Set default output directory if not provided
if [ -z "$output_dir" ]; then
    output_dir="results"
fi

cat  << EOF  > config.txt
center_x = 10.190
center_y = 10.903
center_z = 10.917
size_x = 40.0
size_y = 40.0
size_z = 40.0
EOF

echo "开始转化格式"
#ligand
file=$(ls $ligand_dir)
for i in $file; do
  ligand_name=$(basename $i)
  if [[ $ligand_name == *".mol2"* ]]; then
     echo "$ligand_name 已经为mol2" 
  else
     ligand_trans=$(awk -F "." '{print $1}' <<< "$ligand_name")
     obabel $ligand_dir/$ligand_name 	-O $ligand_dir/$ligand_trans.mol2
     echo "$ligand_trans 转化为mol2"
  fi
done

#protein
file=$(ls $protein_dir)
for i in $file; do
  protein_name=$(basename $i)
  if [[ $protein_name == *".pdb"* ]]; then
     echo "$protein_name 已经为pdb" 
  else
     protein_trans=$(awk -F "." '{print $1}' <<< "$protein_name")
     obabel $protein_dir/$protein_name 	-O $protein_dir/$protein_trans.pdb
     echo "$protein_trans 转化为pdb"
  fi
done
echo "格式转化完成"

for protein in $protein_dir/*.pdb; do
    for ligand in $ligand_dir/*.mol2; do
        protein_name=$(basename "$protein" .pdb)
        ligand_name=$(basename "$ligand" .mol2)
        pythonsh prepare_receptor4.py -r protein/$protein_name.pdb -o protein/$protein_name.pdbqt
        #pythonsh prepare_flexreceptor.py -r $protein_name.pdbqt
        cp ligand/$ligand_name.mol2 .
        pythonsh prepare_ligand4.py -l ligand/$ligand_name.mol2 -F -A hydrogens -o ligand/$ligand_name.pdbqt
        rm $ligand_name.mol2 
        ./vina --ligand ligand/$ligand_name.pdbqt --receptor protein/$protein_name.pdbqt --exhaustiveness 10 --config config.txt --out results/$protein_name-$ligand_name.pdbqt --log results/$protein_name-$ligand_name.txt --num_modes 10 --cpu 96
        obabel results/$protein_name-$ligand_name.pdbqt  -O  results/$protein_name-$ligand_name.pdb
        echo "导入$protein_name-$ligand_name"
        colnames="protein ligand (kcal/mol)" 
        echo "$colnames" > output.csv
        for file in  results/*.txt; do
        row=$(cat $file | grep -n "affinity"| awk -F ":" '{print $1}')
        energy=$(cat $file  | awk "NR==($row+3)" | awk -F " " '{print $2}')
        name=$(basename "$file" .txt)
        final="$name  $energy"
        echo "$final" >> output.csv
        done
     done
done
