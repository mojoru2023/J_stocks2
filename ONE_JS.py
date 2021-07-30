import time

import pyecharts.options as opts
from pyecharts.charts import Line
import os
import xlrd
import sys
from xlrd import xldate_as_tuple
import datetime

# 读取xlxs数据
# 数据处理整理
# 测试
# 可以部署到服务器上面！彻底解放人力！

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://www.echartsjs.com/examples/editor.html?c=line-log

目前无法实现的功能:

1、暂无
"""

from shutil import copyfile

# ! -*- coding:utf-8 -*-
import json
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import copy
import operator

app = Flask(__name__)


@app.route('/jsin')
def js_j225():
    return render_template('js_industryDT.html')  # 在一个目录下,templates中


@app.route('/')
def index():
    return "部署测试"


def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

    # # if 去掉表头
    # if rowNum > 0:

    return dataFile


def text_save(filename, data):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')  # 去除[],这两行按数据不同，可以选择
        s = s.replace("'", '').replace(',', '') + '\n'  # 去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")


# 时间日期的转换


# float--->日期字符串？
def handle_date(dates):
    f_ = []

    for item in dates:
        tuple = xldate_as_tuple(item, 0)
        excel_datetime = datetime.datetime(*tuple)
        f_.append(str(excel_datetime))

    return f_


# 需要修改纵坐标刻度 # 默认是从
def get_v(l):
    f = []

    for num in range(0, len(l) - 1):
        f_da = "%.4f" % (l[num] / l[0] - 1)

        f.append(f_da)

    return f


def jsIn_ep():
    y_data_1 = []
    y_data_2 = []
    y_data_3 = []
    y_data_4 = []
    y_data_5 = []
    y_data_6 = []
    y_data_7 = []
    y_data_8 = []
    y_data_9 = []
    y_data_10 = []
    y_data_11 = []
    y_data_12 = []
    y_data_13 = []
    y_data_14 = []
    y_data_15 = []
    y_data_16 = []
    y_data_17 = []
    y_data_18 = []
    y_data_19 = []
    y_data_20 = []
    y_data_21 = []
    y_data_22 = []
    y_data_23 = []
    y_data_24 = []
    y_data_25 = []
    y_data_26 = []
    y_data_27 = []
    y_data_28 = []
    y_data_29 = []
    y_data_30 = []
    y_data_31 = []
    y_data_32 = []
    y_data_33 = []

    date_ = []
    excelFile = 'js_industryDT.xlsx'
    full_items = read_xlrd(excelFile=excelFile)
    for item in full_items:

        if type(item[2]) == float:
            y_data_1.append(item[2])  # 水産・農林業
        if type(item[3]) == float:
            y_data_2.append(item[3])  # J3141
        if type(item[4]) == float:
            y_data_3.append(item[4])  # J3148
        if type(item[5]) == float:
            y_data_4.append(item[5])  # J3254
        if type(item[6]) == float:
            y_data_5.append(item[6])  # J3288
        if type(item[7]) == float:
            y_data_6.append(item[7])  # J3549
        if type(item[8]) == float:
            y_data_7.append(item[8])  # J3769
        if type(item[9]) == float:
            y_data_8.append(item[9])  # J4091
        if type(item[10]) == float:
            y_data_9.append(item[10])  # J4568
        if type(item[11]) == float:
            y_data_10.append(item[11])  # J4684
        if type(item[12]) == float:
            y_data_11.append(item[12])  # J4768
        if type(item[13]) == float:
            y_data_12.append(item[13])  # J5929
        if type(item[14]) == float:
            y_data_13.append(item[14])  # J6877
        if type(item[15]) == float:
            y_data_14.append(item[15])  # J7309
        if type(item[16]) == float:
            y_data_15.append(item[16])  # J7532
        if type(item[17]) == float:
            y_data_16.append(item[17])  # J7649
        if type(item[18]) == float:
            y_data_17.append(item[18])  # J7974
        if type(item[19]) == float:
            y_data_18.append(item[19])  # J8111
        if type(item[20]) == float:
            y_data_19.append(item[20])  # J8424
        if type(item[21]) == float:
            y_data_20.append(item[21])  # J9065
        if type(item[22]) == float:
            y_data_21.append(item[22])  # J9697
        if type(item[23]) == float:
            y_data_22.append(item[23])  # J_index400

        if type(item[24]) == float:
            y_data_23.append(item[24])  # J_index400
        if type(item[25]) == float:
            y_data_24.append(item[25])  # J_index400
        if type(item[26]) == float:
            y_data_25.append(item[26])  # J_index400
        if type(item[27]) == float:
            y_data_26.append(item[27])  # J_index400
        if type(item[28]) == float:
            y_data_27.append(item[28])  # J_index400
        if type(item[29]) == float:
            y_data_28.append(item[29])  # J_index400
        if type(item[30]) == float:
            y_data_29.append(item[30])  # J_index400
        if type(item[31]) == float:
            y_data_30.append(item[31])  # J_index400
        if type(item[32]) == float:
            y_data_31.append(item[32])  # J_index400
        if type(item[33]) == float:
            y_data_32.append(item[33])  # J_index400
        if type(item[34]) == float:
            y_data_33.append(item[34])  # J_index400

        if item[len(item) - 1] != "LastTime":
            date_.append(item[len(item) - 1])
    # 日期搞定
    x_data = handle_date(date_)

    f_y_data_1 = get_v(y_data_1)
    f_y_data_2 = get_v(y_data_2)
    f_y_data_3 = get_v(y_data_3)
    f_y_data_4 = get_v(y_data_4)
    f_y_data_5 = get_v(y_data_5)
    f_y_data_6 = get_v(y_data_6)
    f_y_data_7 = get_v(y_data_7)
    f_y_data_8 = get_v(y_data_8)
    f_y_data_9 = get_v(y_data_9)
    f_y_data_10 = get_v(y_data_10)
    f_y_data_11 = get_v(y_data_11)
    f_y_data_12 = get_v(y_data_12)
    f_y_data_13 = get_v(y_data_13)
    f_y_data_14 = get_v(y_data_14)
    f_y_data_15 = get_v(y_data_15)
    f_y_data_16 = get_v(y_data_16)
    f_y_data_17 = get_v(y_data_17)
    f_y_data_18 = get_v(y_data_18)
    f_y_data_19 = get_v(y_data_19)
    f_y_data_20 = get_v(y_data_20)
    f_y_data_21 = get_v(y_data_21)
    f_y_data_22 = get_v(y_data_22)
    f_y_data_23 = get_v(y_data_23)
    f_y_data_24 = get_v(y_data_24)
    f_y_data_25 = get_v(y_data_25)
    f_y_data_26 = get_v(y_data_26)
    f_y_data_27 = get_v(y_data_27)
    f_y_data_28 = get_v(y_data_28)
    f_y_data_29 = get_v(y_data_29)
    f_y_data_30 = get_v(y_data_30)
    f_y_data_31 = get_v(y_data_31)
    f_y_data_32 = get_v(y_data_32)
    f_y_data_33 = get_v(y_data_33)
    print(x_data)

    c = (
        Line()
            .add_xaxis(xaxis_data=x_data)

            .add_yaxis(
            "水産・農林業",
            y_axis=f_y_data_1,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "鉱業",
            y_axis=f_y_data_2,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "建設業",
            y_axis=f_y_data_3,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "食料品",
            y_axis=f_y_data_4,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "繊維製品",
            y_axis=f_y_data_5,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "パルプ・紙",
            y_axis=f_y_data_6,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "化学",
            y_axis=f_y_data_7,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "医薬品",
            y_axis=f_y_data_8,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "石油・石炭",
            y_axis=f_y_data_9,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ゴム製品",
            y_axis=f_y_data_10,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "ガラス・土石",
            y_axis=f_y_data_11,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "鉄鋼",
            y_axis=f_y_data_12,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "非鉄金属",
            y_axis=f_y_data_13,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "金属製品",
            y_axis=f_y_data_14,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "機械",
            y_axis=f_y_data_15,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "電気機器",
            y_axis=f_y_data_16,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "輸送用機器",
            y_axis=f_y_data_17,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "精密機器",
            y_axis=f_y_data_18,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "その他製品",
            y_axis=f_y_data_19,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "電気・ガス",
            y_axis=f_y_data_20,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "陸運業",
            y_axis=f_y_data_21,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        ).add_yaxis(
            "海運業",
            y_axis=f_y_data_22,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )

            .add_yaxis(
            "空運業",
            y_axis=f_y_data_23,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        ).add_yaxis(
            "倉庫・運輸",
            y_axis=f_y_data_24,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        ).add_yaxis(
            "情報・通信業",
            y_axis=f_y_data_25,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        ).add_yaxis(
            "卸売業",
            y_axis=f_y_data_26,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        ).add_yaxis(
            "小売業",
            y_axis=f_y_data_27,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        ).add_yaxis(
            "銀行業",
            y_axis=f_y_data_28,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        ).add_yaxis(
            "証券・商品",
            y_axis=f_y_data_29,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        ).add_yaxis(
            "保険業",
            y_axis=f_y_data_30,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        ).add_yaxis(
            "その他金融業",
            y_axis=f_y_data_31,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        ).add_yaxis(
            "不動産業",
            y_axis=f_y_data_32,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .add_yaxis(
            "サービス業",
            y_axis=f_y_data_33,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(title="jsIndustry", pos_bottom="bottom", pos_right="middle"),
            # xaxis_opts=opts.AxisOpts(name="x"),
            yaxis_opts=opts.AxisOpts(
                # name="y",
                splitline_opts=opts.SplitLineOpts(is_show=True),
                is_scale=True,

            ),
            legend_opts=opts.LegendOpts(is_show=False),  # 隐藏图例

        )

            .render("js_industryDT.html")
    )


if __name__ == "__main__":
    jsIn_ep()

    # 等待5秒钟，然后将文件移动到templates目录下

    srcJSin = 'd:\\Downloads\\js_industryDT.html'
    dstJSin = 'd:\\Downloads\\templates\\js_industryDT.html'
    copyfile(srcJSin, dstJSin)
    app.run(debug=True)



