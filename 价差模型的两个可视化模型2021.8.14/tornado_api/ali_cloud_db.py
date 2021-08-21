import pymysql
from sshtunnel import SSHTunnelForwarder

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
    print(result)