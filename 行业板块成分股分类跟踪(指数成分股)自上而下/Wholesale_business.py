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

sql_sp_LJ = 'select id,J9962,J9810,J8283,J8088,J8058,J8053,J8031,J8020,J8015,J8002,J8001,J7575,J7459,J7458,J3543,J3360,J3167,J3107,J3038,J2784,J2768,LastTime from sp_LJ_400    ; '

ln = os.getcwd()


def savedt():

    df_js225 = pd.read_sql_query(sql_sp_LJ, engine_jsMons)
    excelFile3 = '{0}/{1}.xlsx'.format(ln, "Wholesale_business")  # 处理了文件属于当前目录下！
    df_js225.to_excel(excelFile3)




if __name__ == '__main__':
    savedt()

