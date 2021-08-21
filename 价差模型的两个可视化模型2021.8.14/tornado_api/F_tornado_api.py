"""
    tornado web app对于网页模板的处理和静态文件的操作
    网页模板：html页面
    处理：定义html页面、渲染html页面，响应html页面[浏览器]
    静态资源：图片/js/css/字体...
    操作：配置静态资源、查询静态资源[html]、响应数据
"""

# 引入需要的模块
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
from tornado.httpserver import HTTPServer
import os.path
import json
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sshtunnel import SSHTunnelForwarder
import pymysql




# def getdt():
#     with SSHTunnelForwarder(
#             ('47.105.163.6', 22),
#             ssh_username="root",
#             ssh_password="Mingyifan2007",
#             remote_bind_address=('127.0.0.1', 3306)) as server:
#         db_connect = pymysql.connect(
#             host='127.0.0.1',
#             port=server.local_bind_port,
#             user='root',
#             password='123456',
#             database='JS_Mons',
#         )
#         db_curs = db_connect.cursor()
#         sql_cmd = f"SELECT js_225_4000 FROM FJSs "
#         db_curs.execute(sql_cmd)
#         result = db_curs.fetchall()
#         db_curs.close()
#         db_connect.close()
#         for item in result:
#             result_list.append(item[0])


# 创建视图类
class IndexHandler(RequestHandler):
    def get(self):


        with SSHTunnelForwarder(
                ('47.105.163.6', 22),
                ssh_username="root",
                ssh_password="Mingyifan2007",
                remote_bind_address=('127.0.0.1', 3306)) as server:
            db_connect = pymysql.connect(
                host='127.0.0.1',
                port=server.local_bind_port,
                user='root',
                password='123456',
                database='JS_Mons',
            )
            db_curs = db_connect.cursor()
            sql_cmd = f"SELECT js_225_4000 FROM FJSs "
            db_curs.execute(sql_cmd)
            result = db_curs.fetchall()
            db_curs.close()
            db_connect.close()
            for item in result:
                result_list.append(item[0])



        t = {}
        t['data'] = result_list
        f_json = json.dumps(t)
        self.write(f_json)


class Image(RequestHandler):
    def get(self):
        self.render("fjss_api.html")



# 程序入口
if __name__ == '__main__':
    result_list = []

    # 开始监听
    parse_command_line()
    app = Application(
        [
            (r"/data", IndexHandler),
            (r"/fjss", Image),
        ],

        # 项目配置信息
        # 网页模板
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        # 静态文件
        static_path=os.path.join(os.path.dirname(__file__), "static"),

        debug=True
    )

    # 部署
    server = HTTPServer(app)
    # server.listen(options.port)
    # 轮询监听
    IOLoop.current().start()