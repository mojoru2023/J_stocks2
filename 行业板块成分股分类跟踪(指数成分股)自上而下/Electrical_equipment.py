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

sql_sp_LJ = 'select id,J3105,J6479,J6501,J6503,J6504,J6506,J6645,J6674,J6701,J6702,J6703,J6724,J6752,J6758,J6762,J6770,J6841,J6857,J6902,J6952,J6954,J6971,J6976,J7735,J7751,J7752,J8035,LastTime from  sp_LJ_225  ; '

ln = os.getcwd()


def savedt():

    df_js225 = pd.read_sql_query(sql_sp_LJ, engine_jsMons)

    excelFile3 = '{0}/{1}.xlsx'.format(ln, "Electrical_equipment")  # 处理了文件属于当前目录下！
    df_js225.to_excel(excelFile3)



if __name__ == '__main__':
    savedt()

