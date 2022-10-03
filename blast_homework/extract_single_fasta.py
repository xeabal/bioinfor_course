# encoding:utf-8
#该脚本用于完成对于含有fasta格式的seqdump.txt文件中序列的拆分，并返回一个随机的、配对完毕的txt文档
import os
import argparse
import random
if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--path', type = str, default = "./")#输入工作路径，需要含有含有fasta序列的txt文件，默认当前文件
  parser.add_argument('--txt_name', type = str, default = "./seqdump.txt")#输入含有fasta序列的txt文件名，默认sedump.txt
args = parser.parse_args()
path = args.path
os.mkdir(path+"fasta_seqs/")#存放输出文件的dir
txt_name = args.txt_name
filenames = []
f = open(args.txt_name)
data = f.readlines()
tmp = [line for line in range(0,len(data)) if data[line].startswith('>')] #记录">"所在行

#tmp.append(len(data)-1)#增加一个元素，指示data的最后一行，方便最后一个fasta序列能够输入
for loc in range(1, len(tmp)):
    file_new = open(path+"fasta_seqs/" + data[tmp[loc-1]].replace(" ","").strip().strip('>')+'.fasta',"a")#以基因名字创建新的fasta子文件
    filenames.append(data[tmp[loc-1]].replace(" ","").strip().strip('>')+'.fasta')#记录所有新建的文件名字
    file_new.writelines(data[tmp[loc-1]:tmp[loc]])#将fasta形式的序列写入目标文件
    file_new.close()
file_new=open(path+"fasta_seqs/" + data[tmp[loc]].replace(" ","").strip().strip('>')+'.fasta',"a")#txt的最后一个文件的拆分
filenames.append(data[tmp[loc]].replace(" ","").strip().strip('>')+'.fasta')
file_new.writelines(data[tmp[loc]:len(data)-1])
file_new.close()
random.shuffle(filenames)#打乱文件顺序
match = open(path+"fasta_seqs/" + 'match.txt',"a")
pairs = [filenames[i]+ '\t' + filenames[i+1] + '\n' for i in range(0,len(filenames),2)]
match.writelines(pair for pair in pairs)#将fasta文件名按对输出到最终的txt文件中，方便blast使用
match.close()






