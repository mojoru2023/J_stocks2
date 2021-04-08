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

sql_sp_LJ = 'select * from F_js20210408_M  ; '

ln = os.getcwd()


def savedt():

    df_js225 = pd.read_sql_query(sql_sp_LJ, engine_jsMons)
    excelFile3 = '{0}/{1}.xlsx'.format(ln, "Follw_JS_20210408")  # 处理了文件属于当前目录下！
    df_js225.to_excel(excelFile3)




if __name__ == '__main__':
    savedt()

