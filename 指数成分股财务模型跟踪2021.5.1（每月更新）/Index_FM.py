# -*- coding:utf-8 -*-
import datetime
import re
import time

import pymysql

from lxml import etree
from selenium import webdriver
import string
import time
# -*- coding: utf-8 -*-

# 读取页面文本
# 按照标题，保存整个文本



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



import csv
import datetime

import os
import re
import time
import sys
type = sys.getfilesystemencoding()
import pymysql
import xlrd
import requests
from requests.exceptions import RequestException
from lxml import etree

driver = webdriver.Chrome()



def get_first_page(url):

    driver.get(url)
    html = driver.page_source
    return html



# 可以尝试第二种解析方式，更加容易做计算
def parse_stock_note(html):

    selector = etree.HTML(html)
    profits= selector.xpath('//*[@id="right_col"]/table/tbody/tr[1]/td/table/tbody/tr[7]/td/text()')
    d_2018= "".join(profits[1][:-3].split(","))
    d_2017= "".join(profits[2][:-3].split(","))
    d_2016= "".join(profits[3][:-3].split(","))

    big_tuple = (d_2018,d_2017,d_2016)
    return big_tuple






def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into index_SM (name,code,indus,d2018,d2017,d2016) values (%s,%s,%s,%s,%s,%s)', content)
        connection.commit()

        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass

#
if __name__ == '__main__':

    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    options = webdriver.ChromeOptions()
    excelFile = 'index_ss.xlsx'
    full_items = read_xlrd(excelFile=excelFile)
    for s_item in full_items:



    #sql 语句

        big_list = []
        data_code = str(int(s_item[1]))

        url = 'https://profile.yahoo.co.jp/independent/' + str(data_code)

        html = get_first_page(url)
        content = parse_stock_note(html)
        f_tuple = tuple(s_item)+content





        finanl_content = [f_tuple]

        insertDB(finanl_content)
        print(finanl_content)

        print(datetime.datetime.now())



# 因为板块数据是最后嵌套进去的，所以要保持，１．数据库表结构，２．解析整理后的数据结构　３．　插入的字段结构　三者之间都要保持一致
# create table index_SM(
# id int not null primary key auto_increment,
# name varchar(50),
# code float,
# indus varchar(15),
# d2018 varchar(20),
# d2017 varchar(20),
# d2016 varchar(20)
# ) engine=InnoDB  charset=utf8;

#  drop table index_SM;