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


@app.route('/fjss')
def js_j225():
    return render_template('FJS_s.html')  # 在一个目录下,templates中


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

    y_data_3 = []

    date_ = []
    excelFile = 'FJSs.xlsx'
    full_items = read_xlrd(excelFile=excelFile)
    for item in full_items:

        if type(item[4]) == float:
            y_data_3.append(item[4])  # J3148





        if item[len(item) - 1] != "LastTime":
            date_.append(item[len(item) - 1])
    # 日期搞定
    x_data = handle_date(date_)


    f_y_data_3 = get_v(y_data_3)




    c = (
        Line()
            .add_xaxis(xaxis_data=x_data)

            .add_yaxis(
            "js225_400",
            y_axis=f_y_data_3,
            linestyle_opts=opts.LineStyleOpts(width=1),
            label_opts=opts.LabelOpts(is_show=False), symbol_size=1
        )

            .set_global_opts(
            title_opts=opts.TitleOpts(title="FJSs", pos_bottom="bottom", pos_right="middle"),
            # xaxis_opts=opts.AxisOpts(name="x"),
            yaxis_opts=opts.AxisOpts(
                # name="y",
                splitline_opts=opts.SplitLineOpts(is_show=True),
                is_scale=True,

            ),
            legend_opts=opts.LegendOpts(is_show=False),  # 隐藏图例

        )

            .render("FJS_s.html")
    )


if __name__ == "__main__":
    jsIn_ep()

    # 等待5秒钟，然后将文件移动到templates目录下

    srcJSin = 'd:\\Downloads\\FJS_s.html'
    dstJSin = 'd:\\Downloads\\templates\\FJS_s.html'
    copyfile(srcJSin, dstJSin)
    app.run(debug=True)



