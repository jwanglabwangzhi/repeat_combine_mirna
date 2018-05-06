# repeat_combine_mirna
## Here is the experience of repeating project in 'https://github.com/DavisLaboratory/Combinatorial_miRNAs'

## Fist day
使用pyreference库，需要下载ucsc注释文件.gtf，转化成json格式。
注释文件你懂得，那么多版本，我用了几个版本后都不行，只能用作者说的igenome的注释。  
igenome也是个坑。为ucsc hg19提供了两个注释文件，一个20多g，一个40多g，我的天，40多g的那个是可以运行的。  
使用pyreference_gtf_to_json.py genes.gtf生成了genes.gtf.json文件。  

## Second day
阅读了pyreference库的pyreference_gtf_to_json.py部分，大概明白了reference的数据结构,大致上根据注释文件使用HTSeq形成每一行的GenomicFeature数据。
提取GenomicFeature中的基本信息，并形成genes_by_id（搜集一个gene id对应的所有转录本及基本信息，所有的feature），transcripts_by_id（类似genes_by_id），gene_id_by_name(gene_id和gene_name的字典)，gene_ids_by_biotype(特征（外显子等）对应的gene_id)  。并把它们写入json文件。  
也阅读HTSeq的一些数据结构，和相关方法调用。

## Third day 
阅读项目中的两个重要函数的实现，get_overlapping_gene_names，prepare_gas_for_exons_and_introns。
首先实例化Reference读取注释genes_gtf.json。get_overlapping_gene_names根据参考基因组得到重叠基因和非重叠基因，原理是使用GenomicArrayofSets这种结构存储iv和gene_name。通过iv找gene_name的集合，如果集合中只有一个gene_name就是非重叠基因。  
Prepare_gas_for_exons_and_introns使用GenomicArrayOfSets存储exon_iv和对应的gene_name。

## Fouth day
程序跑起来，第一个数据如果只用单端数据计算count，计算不出来。SRA的sra_instant挂掉了，只能单个从ENA上下载，但ENA上的SRA镜像是错误的，比对了一个文件，比对率几乎为0。  
所以选择ENA上paired fastq文件，再测试。  

## Fifth day
比对命令：bowtie2 -x /home/biodancer/bioinfor_soft/file/index/hg19_bowtie2_index -1 ./ERR2309103_1.fastq -2 ./ERR2309103_2.fastq -S ERR2309103.sam  
比对结果：

'''
55737508 reads; of these:
  55737508 (100.00%) were paired; of these:
    12640123 (22.68%) aligned concordantly 0 times
    27234975 (48.86%) aligned concordantly exactly 1 time
    15862410 (28.46%) aligned concordantly >1 times
    ----
    12640123 pairs aligned concordantly 0 times; of these:
      2188950 (17.32%) aligned discordantly 1 time
    ----
    10451173 pairs aligned 0 times concordantly or discordantly; of these:
      20902346 mates make up the pairs; of these:
        13709765 (65.59%) aligned 0 times
        5459696 (26.12%) aligned exactly 1 time
        1732885 (8.29%) aligned >1 times
87.70% overall alignment rate

'''
