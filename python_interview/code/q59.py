# 统计一个文本中单词频次最高的10个单词？
import re

def test(filepath):
    distone = {}
    numTen = []

    with open(filepath,"r",encoding="utf-8") as f:
        for line in f:
            line = re.sub("\W","",line)
            lineone = line.split()
            for keyone in lineone:
                if not distone.get(keyone):
                    distone[keyone]=1
                else:
                    distone[keyone]+=1

    numTen = sorted(distone.items(),key=lambda x:x[1],reverse=True)[:10]
    numTen =[x[0]for x in numTen]
    return numTen