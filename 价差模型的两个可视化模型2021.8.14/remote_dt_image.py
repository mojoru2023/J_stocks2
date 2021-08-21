import pymysql
from sshtunnel import SSHTunnelForwarder
import pygal


def get_image(list_dt):

    view = pygal.Line()
    #图表名
    view.title = 'js225_400'
    #添加数据
    view.add('js225_400',list_dt)
    #在浏览器中查看
    view.render_in_browser()
    #保存为view.svg(也可以保存为jpg)
    line.legend_at_bottom = True
    # 设置将图片输出到SVG图片中
    # line.render_to_file('line.svg')
    line.render_to_png('line.png')
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
    result_list = []


    for item in result:
        result_list.append(item[0])
    get_image(result_list)