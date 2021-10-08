

import datetime
import time

import pymysql
import requests
from lxml import etree
import json
from queue import Queue
import threading
from requests.exceptions import RequestException
from retrying import retry


from selenium.common.exceptions import WebDriverException

from retrying import retry
import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException
from lxml import etree
from selenium import webdriver









def retry_if_io_error(exception):
    print("---------------------------")
    return isinstance(exception, WebDriverException)



def RemoveDot(item):
    f_l = []
    for it in item:
        f_str = "".join(it.split(","))
        f_l.append(f_str)

    return f_l

def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items

def retry_if_io_error(exception):
    return isinstance(exception, WebDriverException)
def retry_if_io_error1(exception):
    return isinstance(exception, IndexError)
'''
1. 创建 URL队列, 响应队列, 数据队列 在init方法中
2. 在生成URL列表中方法中,把URL添加URL队列中
3. 在请求页面的方法中,从URL队列中取出URL执行,把获取到的响应数据添加响应队列中
4. 在处理数据的方法中,从响应队列中取出页面内容进行解析, 把解析结果存储数据队列中
5. 在保存数据的方法中, 从数据队列中取出数据,进行保存
6. 开启几个线程来执行上面的方法
'''

def run_forever(func):
    def wrapper(obj):
        while True:
            func(obj)

    return wrapper

def remove_douhao(num):
    num1 = "".join(num.split(","))
    f_num = str(num1)
    return f_num

class JSPool_M(object):

    def __init__(self, url):
        self.url = url

    @retry(retry_on_exception=retry_if_io_error)
    @retry(retry_on_exception=retry_if_io_error1)
    def page_request(self):
        '''
        服务器上必须配置无头模式
        '''
        ch_options = webdriver.ChromeOptions()
        # 为Chrome配置无头模式
        ch_options.add_argument("--headless")
        ch_options.add_argument('--no-sandbox')
        ch_options.add_argument('--disable-gpu')
        ch_options.add_argument('--disable-dev-shm-usage')
        # 在启动浏览器时加入配置
        driver = webdriver.Chrome(options=ch_options)

        driver.get(self.url)
        html = driver.page_source
        driver.quit()
        return html

    def page_parse_(self):
        '''根据页面内容使用lxml解析数据, 获取段子列表'''

        html = self.page_request()
        element = etree.HTML(html)

        now_price = element.xpath(
            '//*[@id="readArea"]/div[2]/div/table/tbody/tr[2]/td[6]/text()[1]')
        f_price = RemoveDot(remove_block(now_price))
        big_list.append(f_price[0])
        return big_list

def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS_Mons',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:

        cursor.executemany('insert into FJSs (js225_,js400_,js_225_4000) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError:
        pass








if __name__ == '__main__':
    while True:
        big_list = []
        js225_url = "https://port.jpx.co.jp/jpx/template/quote.cgi?F=tmp/e_popchart&QCODE=111.555/O"
        js400_url = 'https://port.jpx.co.jp/jpx/template/quote.cgi?F=tmp/e_popchart&QCODE=105.555/O'

        jsp1 = JSPool_M(js225_url)  # 这里把请求和解析都进行了处理
        jsp1.page_parse_()
        jsp2 = JSPool_M(js400_url)  # 这里把请求和解析都进行了处理
        jsp2.page_parse_()

        js225_ = big_list[0]
        js400_ = big_list[1]

        # 要价差，不要比价
        js_225_400 = float(js225_) - float(js400_)

        title_l = [js225_, js400_, js_225_400]

        ff_l = []
        f_tup = tuple(title_l)
        ff_l.append((f_tup))
        print(big_list)
        print(ff_l)
        insertDB(ff_l)
        print(datetime.datetime.now())


#1720
# 1803
# 3612
# 4555




# create table FJSs(id int not null primary key auto_increment, js225_ FLOAT,js400_ FLOAT,js_225_4000 FLOAT, LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ) engine=InnoDB  charset=utf8;


