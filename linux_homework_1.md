### Linux basic command homework
#### 1.解释 1.gtf 文件中第4、5列代表什么，exon长度应该是$5-$4+1 还是 $5-$4 ？
4、5列分别代表序列在基因组上的起始位置。因为gff/gtf文件的坐标从1开始，序列区间是闭区间，所以算序列长度是，需要“终点位置-起始位置+1”，将终点位置的碱基也纳入长度计算范围中。

&nbsp;

#### 2.列出1.gtf文件中 XI 号染色体上的后 10 个 CDS （按照每个CDS终止位置的基因组坐标进行sort）。
命令：  
`cat 1.gtf | awk '$1=="XI"&&$3 == "CDS"' | sort -n -k 5| tail -10`

结果：  
![图片1](/./picutre/linux_homework_pic1.png)

&nbsp;

#### 3.统计 IV 号染色体上各类 feature （1.gtf文件的第3列，有些注释文件中还应同时考虑第2列） 的数目，并按升序排列
命令：  
`grep -v '^#' 1.gtf | cut -f 3| sort | uniq -c|sort -k 1`

结果：  
![图片2](/./picutre/linux_homework_pic2.png)

&nbsp;

