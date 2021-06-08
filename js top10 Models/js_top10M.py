
# 放弃vba,直接上python

# -*- coding: utf-8 -*-

# 读取页面文本
# 按照标题，保存整个文本


import csv
import datetime
import numpy as np


import os
import re
import time
import sys

type = sys.getfilesystemencoding()
import pymysql
import xlrd






def writerDt_csv(headers, rowsdata):
    # rowsdata列表中的数据元组,也可以是字典数据
    with open('sc_jsIndex.csv', 'w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rowsdata)


def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

    # # if 去掉表头
    # if rowNum > 0:

    return dataFile


# xlsx---list_url----单页url
def get_allURL():

    lpath = os.getcwd()
    for item in ["JS_Mons225.xlsx","JS_Mons400.xlsx"]:

        excelFile = '{0}//{1}'.format(lpath,item)
        full_items = read_xlrd(excelFile=excelFile)


        #2---362
        for num in range(2,len(full_items[0])-1):
            _list= []

            for item in full_items:

                _list.append((item[num]))
            operate_list.append(_list)


def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS_Mons',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:

        cursor.executemany('insert into JS_Daily_T10 (N1,N2,N3,N4,N5,N6,N7,N8,N9,N10) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass




if __name__ == '__main__':
    operate_list = []
    f_lst = []
    last_max_min_ = []
    headers=["US_title","last_","max_","_min","_stdev"]

    get_allURL()
    for a in operate_list:


        f_1_0 = a[1:][0]
        if f_1_0 != 0:

            for i in a[1:]:
                last_max_min_.append(round((i - f_1_0) / f_1_0, 4))


            _last = last_max_min_[-1]

            f_lst.append((a[0], _last))
        else:
            pass

    print(f_lst)
    # 关键的排序
    # 先剔除重复项
    f_set = list(set(f_lst))
    f_lst.sort(key=lambda x:x[1],reverse=True)

    l_set = list(set(f_lst))
    l_set.sort(key=lambda x: x[1], reverse=True)
    title_l = [x[0] for x in l_set[:10]]
    ff_l = []
    f_tup = tuple(title_l)
    ff_l.append((f_tup))
    print(f_lst)
    print(l_set)
    print(ff_l)
    insertDB(ff_l)


#  create table JS_Daily_T10(
# id int not null primary key auto_increment,
# N1 varchar(10),
# N2 varchar(10),
# N3 varchar(10),
# N4 varchar(10),
# N5 varchar(10),
# N6 varchar(10),
# N7 varchar(10),
# N8 varchar(10),
# N9 varchar(10),
# N10 varchar(10),
#  LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;

