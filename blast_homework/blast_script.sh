#需要向脚本输入工作路径以及序列的txt文件的名字及其所在路径
output_dirname=${1}"output"
mkdir $output_dirname #创建输出目录
python extract_single_fasta.py --path $1 --txt_name $2
#cat ${1}"/fasta_seqs/match.txt"|awk '{blastp -query "fasta_seqs/"${1} -subject "fasta_seqs/"${2}    -out output/blastp}'

cat ${1}"fasta_seqs/match.txt"|awk -F '\t' '{cmd="blastp -query fasta_seqs/"$1" -subject fasta_seqs/"$2" -out output/blastp_match_"$1"_";system(cmd)}'