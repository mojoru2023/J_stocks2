# !/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import datetime
import pymysql
import pandas as pd

from sqlalchemy import create_engine
import pymysql
import pandas as pd
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime

engine_jsMons = create_engine('mysql+pymysql://root:123456@localhost:3306/JS_Mons')
# 查询语句，选出employee表中的所有数据 "JS225_JS400"



ln = os.getcwd()


def LT_S1_():
    sql_sp_LJ = 'select * from LT_S1  ; '

    df_js225 = pd.read_sql_query(sql_sp_LJ, engine_jsMons)
    excelFile3 = '{0}/{1}.xlsx'.format(ln, "LT_S1")  # 处理了文件属于当前目录下！
    df_js225.to_excel(excelFile3)


def LT_S2_():
    sql_sp_LJ = 'select * from LT_S2  ; '

    df_js225 = pd.read_sql_query(sql_sp_LJ, engine_jsMons)
    excelFile3 = '{0}/{1}.xlsx'.format(ln, "LT_S2")  # 处理了文件属于当前目录下！
    df_js225.to_excel(excelFile3)



def LT_S3_():
    sql_sp_LJ = 'select * from LT_S3  ; '

    df_js225 = pd.read_sql_query(sql_sp_LJ, engine_jsMons)
    excelFile3 = '{0}/{1}.xlsx'.format(ln, "LT_S3")  # 处理了文件属于当前目录下！
    df_js225.to_excel(excelFile3)

if __name__ == '__main__':
    LT_S1_()
    LT_S2_()
    LT_S3_()

