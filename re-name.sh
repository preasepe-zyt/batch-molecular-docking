file_list=$(ls -1 *.pdbqt)
file_txt=$(ls -1 *.txt)
file_count=$(echo "$file_list" | wc -l)

# 循环遍历文件列表
for ((i=1; i<=$file_count; i++)); do
  current_file=$(echo "$file_list" | awk -v var=$i 'NR==var {print $0}')
  name=$(paste -d '-' <(awk '{print $2}' output.txt | sed -n "$((i+1))p") <(awk '{print $3}' output.txt | sed -n "$((i+1))p") )
  mv  "$current_file"  "$name.pdbqt"
  current_text=$(echo "$file_txt" | awk -v var=$i 'NR==var {print $0}')
  mv  "$current_text"  "$name.txt"
done




