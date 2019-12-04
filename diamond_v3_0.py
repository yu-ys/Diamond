# Diamond
# 2019.11.12 v3.0   "截图"
# 2019.11.9 v2.0    挑出"比值最大"
# 使用前需修改'测试结果Excel', '源文件夹', '新文件夹' 三者路径名！！！

import sys
import shutil
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot


# ===================================
# 修改路径

# 1.测试结果excel路径
excel = pd.read_excel(r'C:\...', "比值最大")  # 测试结果excel

# 2.全部初始数据文件夹路径
path_origin = 'C:\\...'  # 源文件路径

# 3.筛选后文件夹路径
path_copy = 'C:\\...'  # 筛选后路径

# ===================================

index = pd.Series(excel['序号'])
text = []

postfix_txt = '_1.txt'
postfix_jpeg = '_1.jpeg'

for i in index:
    text.append(i)

# =====================
# 合并路径方法
def join(ori_path, copy_path):
    text2 = []
    for x in text:
        joined = ori_path + x + postfix_txt
        text2.append(joined)

    for y in text2:
        shutil.copy(y, copy_path)  # 筛选后的新目录


# =====================
# 导出图片方法

def picture_all(copy_path):
    count = 1
    print("开始打印... (别zhuo急)")
    for txt in text:
        data_path = copy_path + '\\' + txt + postfix_txt
        pic_path = copy_path + '\\' + txt + postfix_jpeg
        data = pd.read_table(data_path, header=None)
        y_start = np.floor(data[1].min()*0.8)
        line = (Line(init_opts=opts.InitOpts(width='600px', bg_color='#fff'))
                .add_xaxis(data[0])
                .add_yaxis("", data[1], is_symbol_show=False)
                .set_global_opts(xaxis_opts=opts.AxisOpts(min_=1900), yaxis_opts=opts.AxisOpts(min_=y_start)))
        line.render(path=pic_path)
        make_snapshot(snapshot, line.render(), pic_path, is_remove_html=True)

        sys.stdout.write("\r图片打印中... (%d/%d)" % (count, len(text)))
        count += 1
    print("打印结束！")

join(path_origin, path_copy)
picture_all(path_copy)
