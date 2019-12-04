# Diamond v2.0
# 2019.11.9
# 使用前需修改Excel路径名！！！

import shutil
import pandas as pd


data = pd.read_excel(r'C:\Users\yuys\Desktop\合作实验=_=\Diamond\20191031-36\测试结果.xlsx', "比值最大")
data.reindex
index = pd.Series(data['序号'])
text = []

for i in index:
    text.append(i)

def join():
    path = 'C:\\Users\\yuys\\Desktop\\test\\original\\'
    postfix = '_1.txt'

    text2 = []

    for x in text:
        joined = path + x + postfix
        text2.append(joined)

    for y in text2:
        shutil.copy(y, r'C:\\Users\yuys\Desktop\test\copyed')

join()
