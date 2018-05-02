# repeat_combine_mirna
## Here is the experience of repeating project in 'https://github.com/DavisLaboratory/Combinatorial_miRNAs'

## Fist day
使用pyreference库，需要下载ucsc注释文件.gtf，转化成json格式。
注释文件你懂得，那么多版本，我用了几个版本后都不行，只能用作者说的igenome的注释。  
igenome也是个坑。为ucsc hg19提供了两个注释文件，一个20多g，一个40多g，我的天，40多g的那个是可以运行的。  
使用pyreference_gtf_to_json.py genes.gtf生成了genes.gtf.json文件。  

## Second day
阅读了pyreference库的pyreference_gtf_to_json.py部分，大概明白了reference的数据 $
也阅读HTSeq的一些数据结构，和相关方法调用。

## 

