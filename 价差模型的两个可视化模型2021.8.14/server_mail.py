


# coding:utf-8
import json
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import pygal

import os


from email.mime.base import MIMEBase
from email.header import Header
import smtplib
from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText
import email.encoders as Encoders
import os
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime
import smtplib


ln = os.getcwd()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 显示中文


# 在Flask里 sqlachemy是非常方便的，但是假如数据量很大的话，
# 后台返回的json速度就很慢，很影响用户体验，所以用paginate来分页返回数据paginate(id, num)
#  #id为第几页 num表示一页有几条数据很明显
# 我们的页数应该是 [1,sum/num]所以在前台的页数应该是 1到 数据总数/一页的数据量例如 有7311条数据，
# 我们需要一页10条数据的话页数就是 1 ~ 732 因为还有 最后一页 只有一条数据

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/JS_Mons'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Base = declarative_base()

# sqlalchemy 对已有表做操作需要先做一个映射类

class FJSs(Base):
    __tablename__ = 'FJSs'
    id = Column(Integer,primary_key=True,nullable=False, autoincrement=True)
    js_225_4000 = Column(String(12),nullable=True)  # String在数据库中常见为varchar类型



    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


def get_image(list_dt):

    view = pygal.Line()
    #图表名
    view.title = 'js225_400'
    #添加数据
    view.add('js225_400',list_dt)
    #在浏览器中查看
    view.render_in_browser()
    #保存为view.svg(也可以保存为jpg)
    view.legend_at_bottom = True
    # 设置将图片输出到SVG图片中
    # line.render_to_file('line.svg')
    view.render_to_png('fjss_.png')
    print("get the image")


def get_db_image():
    big_list = []
    pls = db.session.query(FJSs.js_225_4000).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
    for item in pls:
        for i in item:
            num_int = float(i)
            big_list.append(num_int)  # 需要把字符串类型转换为浮点型,而不是整型
    get_image(big_list)

def sendto_wechat():


    gmail_user = "min2020fr@gmail.com"
    gmail_pwd = "dwodwugqviervgjo"

    to = "min2020fr@gmail.com"
    subject = "Report"
    text = "Picture report"
    attach = 'fjss_.png'

    msg = MIMEMultipart()

    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    # Should be mailServer.quit(), but that crashes...
    mailServer.close()



if __name__ =="__main__":
    get_db_image()
    sendto_wechat()