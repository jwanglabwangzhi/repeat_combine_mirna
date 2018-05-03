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

