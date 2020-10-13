# coding: utf-8
import datetime
import logging
import os
import queue
import random
import socket
import threading
import time
from logging import handlers

import requests
import select
from lxml import etree

MAX_QUEUE_SIZE = 500

def get_proxy_alive_time(proxy):
    startTime = datetime.datetime.strptime(proxy["CreateTime"][:19], "%Y-%m-%dT%H:%M:%S")
    endTime = datetime.datetime.now()
    alive = proxy['Interval'] - (endTime - startTime).seconds
    return alive


def proxy_alive_cmp(a, b):
    ta = get_proxy_alive_time(a)
    tb = get_proxy_alive_time(b)
    return ta - tb


def get_proxy_list(alive_time=40):
    records = requests.get("http://119.97.156.100:9010/all", timeout=5).json()
    proxy_list = []
    for item in records.values():
        startTime = datetime.datetime.strptime(item["CreateTime"][:19], "%Y-%m-%dT%H:%M:%S")
        endTime = datetime.datetime.now()
        interval = item['Interval'] - (endTime - startTime).seconds
        if interval >= alive_time:
            proxy_list.append(item)
    if not proxy_list:  # 没有有效代理，过一会再请求
        time.sleep(5)
    random.shuffle(proxy_list)
    return proxy_list


class ProxyService(object):

    def __init__(self):
        self.proxy_queue = queue.Queue(maxsize=MAX_QUEUE_SIZE)
        self.proxy_queue_lock = threading.RLock()

    def refresh_proxy_queue(self, alive_time=40):
        self.proxy_queue = queue.Queue(maxsize=MAX_QUEUE_SIZE)
        proxy_list = get_proxy_list(alive_time=alive_time)
        for proxy in proxy_list:
            if not self.proxy_queue.full():
                self.proxy_queue.put(proxy)

    def get_alive_proxy(self, alive_time=40, crawl_time=20):
        try:
            self.proxy_queue_lock.acquire()
            if self.proxy_queue.empty():
                self.refresh_proxy_queue(alive_time=alive_time)
            proxy = self.proxy_queue.get(timeout=1)
            alive = get_proxy_alive_time(proxy)
            if alive < crawl_time:
                self.refresh_proxy_queue(alive_time=alive_time)
                proxy = self.proxy_queue.get(timeout=1)
            self.proxy_queue_lock.release()
            return proxy
        except Exception as e:
            print('get _alive_proxy exception', e)
            self.proxy_queue_lock.release()
            return None

    def recycle_proxy(self, proxy):
        try:
            self.proxy_queue_lock.acquire()
            if not self.proxy_queue.full():
                self.proxy_queue.put(proxy)
            self.proxy_queue_lock.release()
        except Exception as e:
            print('put _alive_proxy exception', e)
            self.proxy_queue_lock.release()
            return None


def getLogger(name, onlyMsg=True):
    name = os.path.join(os.getenv('COMPINFO_LOG_PREFIX', 'log'), name)
    x = os.path.dirname(name)
    # 解决多进程安全问题，解决方式low
    try:
        if x and not os.path.isdir(x): os.makedirs(x)
    except FileExistsError as error:
        pass
    formater = logging.Formatter("%(message)s" if onlyMsg else "%(asctime)s - %(module)s:%(lineno)dL %(process)d [%(levelname)s]%(message)s")
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.handlers.TimedRotatingFileHandler(name, when='D', backupCount=1000, encoding='utf-8')
    handler.setFormatter(formater)
    logger.addHandler(handler)
    return logger

def get_logger(name, only_msg=True):
    return getLogger(name, onlyMsg=only_msg)


def retry(attempt=3):
    """出错重试"""
    def decorator(func):
        def wrapper(*args, **kw):
            att = 0
            while att < attempt:
                try:
                    r = func(*args, **kw)
                    if r: return r
                    att += 1
                except Exception as e:
                    print(args, kw)
                    # logger.exception('request remote api error')
                    att += 1
                time.sleep(1)
        return wrapper
    return decorator


def check_or_create_dir(path):
    current = os.getcwd()
    dest = os.path.join(current, path)
    if not os.path.exists(dest):
        os.makedirs(dest)
    return dest


PROXIES = [
  "http://hexin:hx300033@101.71.41.129:888",
  "http://hexin:hx300033@101.71.41.130:888",
  "http://hexin:hx300033@101.71.41.131:888",
  "http://hexin:hx300033@101.71.41.132:888",
  "http://hexin:hx300033@101.71.41.133:888",
  "http://hexin:hx300033@101.71.41.135:888",
  "http://hexin:hx300033@101.71.41.136:888",
  "http://hexin:hx300033@101.71.41.137:888",
  "http://hexin:hx300033@101.71.41.139:888",
  "http://hexin:hx300033@101.71.41.141:888",
  "http://hexin:hx300033@101.71.41.142:888",
  "http://hexin:hx300033@101.71.41.143:888",
  "http://hexin:hx300033@101.71.41.144:888",
  "http://hexin:hx300033@101.71.41.145:888",
  "http://hexin:hx300033@101.71.41.146:888",
  "http://hexin:hx300033@101.71.41.147:888",
  "http://hexin:hx300033@101.71.41.149:888",
  "http://hexin:hx300033@101.71.41.150:888",
  "http://hexin:hx300033@101.71.41.152:888",
  "http://hexin:hx300033@101.71.41.153:888",
  "http://hexin:hx300033@101.71.41.154:888",
  "http://hexin:hx300033@101.71.41.155:888",
  "http://hexin:hx300033@101.71.41.156:888",
  "http://hexin:hx300033@101.71.41.157:888",
  "http://hexin:hx300033@101.71.41.158:888",
  "http://hexin:hx300033@101.71.41.159:888",
  "http://hexin:hx300033@101.71.41.160:888",
  "http://hexin:hx300033@101.71.41.161:888",
  "http://hexin:hx300033@101.71.41.162:888",
  "http://hexin:hx300033@101.71.41.163:888",
  "http://hexin:hx300033@101.71.41.164:888",
  "http://hexin:hx300033@101.71.41.165:888",
  "http://hexin:hx300033@101.71.41.166:888",
  "http://hexin:hx300033@101.71.41.168:888",
  "http://hexin:hx300033@101.71.41.170:888",
  "http://hexin:hx300033@101.71.41.171:888",
  "http://hexin:hx300033@101.71.41.172:888",
  "http://hexin:hx300033@101.71.41.173:888",
  "http://hexin:hx300033@101.71.41.174:888",
  "http://hexin:hx300033@101.71.41.175:888",
  "http://hexin:hx300033@101.71.41.176:888",
  "http://hexin:hx300033@101.71.41.177:888",
  "http://hexin:hx300033@101.71.41.178:888",
  "http://hexin:hx300033@101.71.41.179:888",
  "http://hexin:hx300033@101.71.41.180:888",
  "http://hexin:hx300033@101.71.41.182:888",
  "http://hexin:hx300033@101.71.41.183:888",
  "http://hexin:hx300033@101.71.41.184:888",
  "http://hexin:hx300033@101.71.41.185:888",
  "http://hexin:hx300033@101.71.41.187:888",
  "http://hexin:hx300033@101.71.41.188:888",
  "http://hexin:hx300033@101.71.41.189:888",
  "http://hexin:hx300033@101.71.41.190:888",
  "http://hexin:hx300033@101.71.41.192:888",
  "http://hexin:hx300033@101.71.41.193:888",
  "http://hexin:hx300033@101.71.41.194:888",
  "http://hexin:hx300033@101.71.41.195:888",
  "http://hexin:hx300033@101.71.41.196:888",
  "http://hexin:hx300033@101.71.41.197:888",
  "http://hexin:hx300033@101.71.41.198:888",
  "http://hexin:hx300033@101.71.41.199:888",
  "http://hexin:hx300033@101.71.41.200:888",
  "http://hexin:hx300033@101.71.41.201:888",
  "http://hexin:hx300033@112.17.10.176:888",
  "http://hexin:hx300033@112.17.10.178:888",
  "http://hexin:hx300033@112.17.10.179:888",
  "http://hexin:hx300033@112.17.10.191:888",
  "http://hexin:hx300033@112.17.10.192:888",
  "http://hexin:hx300033@112.17.10.203:888",
  "http://hexin:hx300033@112.17.10.204:888",
  "http://hexin:hx300033@112.17.10.208:888",
  "http://hexin:hx300033@112.17.10.209:888",
  "http://hexin:hx300033@112.17.10.210:888",
  "http://hexin:hx300033@112.17.10.211:888",
  "http://hexin:hx300033@112.17.10.215:888",
  "http://hexin:hx300033@112.17.10.216:888",
  "http://hexin:hx300033@112.17.10.220:888",
  "http://hexin:hx300033@112.17.10.221:888",
  "http://hexin:hx300033@112.17.10.222:888",
  "http://hexin:hx300033@112.17.10.223:888",
  "http://hexin:hx300033@112.17.10.224:888",
  "http://hexin:hx300033@112.17.10.225:888",
  "http://hexin:hx300033@112.17.10.226:888",
  "http://hexin:hx300033@112.17.10.227:888",
  "http://hexin:hx300033@112.17.10.228:888",
  "http://hexin:hx300033@112.17.10.229:888",
  "http://hexin:hx300033@112.17.10.230:888",
  "http://hexin:hx300033@112.17.10.231:888",
  "http://hexin:hx300033@112.17.10.232:888",
  "http://hexin:hx300033@112.17.10.233:888",
  "http://hexin:hx300033@112.17.10.234:888",
  "http://hexin:hx300033@112.17.10.235:888",
  "http://hexin:hx300033@112.17.10.236:888",
  "http://hexin:hx300033@112.17.10.237:888",
  "http://hexin:hx300033@112.17.10.238:888",
  "http://hexin:hx300033@112.17.10.239:888",
  "http://hexin:hx300033@112.17.10.240:888",
  "http://hexin:hx300033@112.17.10.241:888",
  "http://hexin:hx300033@112.17.10.242:888",
  "http://hexin:hx300033@112.17.10.243:888",
  "http://hexin:hx300033@112.17.10.244:888",
  "http://hexin:hx300033@112.17.10.245:888",
  "http://hexin:hx300033@119.97.156.23:888",
  "http://hexin:hx300033@119.97.156.24:888",
  "http://hexin:hx300033@119.97.156.25:888",
  "http://hexin:hx300033@119.97.156.26:888",
  "http://hexin:hx300033@119.97.156.39:888",
  "http://hexin:hx300033@119.97.156.40:888",
  "http://hexin:hx300033@119.97.156.42:888",
  "http://hexin:hx300033@119.97.156.43:888",
  "http://hexin:hx300033@119.97.156.45:888",
  "http://hexin:hx300033@119.97.156.47:888",
  "http://hexin:hx300033@119.97.156.48:888",
  "http://hexin:hx300033@119.97.156.49:888",
  "http://hexin:hx300033@119.97.156.50:888",
  "http://hexin:hx300033@119.97.156.51:888",
  "http://hexin:hx300033@119.97.156.52:888",
  "http://hexin:hx300033@119.97.156.53:888",
  "http://hexin:hx300033@119.97.156.54:888",
  "http://hexin:hx300033@119.97.156.55:888",
  "http://hexin:hx300033@119.97.156.56:888",
  "http://hexin:hx300033@119.97.156.57:888",
  "http://hexin:hx300033@119.97.156.58:888",
  "http://hexin:hx300033@119.97.156.59:888",
  "http://hexin:hx300033@119.97.156.60:888",
  "http://hexin:hx300033@119.97.156.61:888",
  "http://hexin:hx300033@119.97.156.63:888",
  "http://hexin:hx300033@119.97.156.63:888",
  "http://hexin:hx300033@119.97.156.63:888",
  "http://hexin:hx300033@119.97.156.63:888",
  "http://hexin:hx300033@119.97.156.63:888",
  "http://hexin:hx300033@119.97.156.63:888",
  "http://hexin:hx300033@119.97.156.63:888",
  "http://hexin:hx300033@119.97.156.64:888",
  "http://hexin:hx300033@119.97.156.66:888",
  "http://hexin:hx300033@119.97.156.67:888",
  "http://hexin:hx300033@119.97.156.70:888",
  "http://hexin:hx300033@119.97.156.72:888",
  "http://hexin:hx300033@119.97.156.73:888",
  "http://hexin:hx300033@119.97.156.74:888",
  "http://hexin:hx300033@119.97.156.75:888",
  "http://hexin:hx300033@119.97.156.76:888",
  "http://hexin:hx300033@119.97.156.77:888",
  "http://hexin:hx300033@119.97.156.78:888",
  "http://hexin:hx300033@119.97.156.80:888",
  "http://hexin:hx300033@119.97.156.82:888",
  "http://hexin:hx300033@119.97.156.84:888",
  "http://hexin:hx300033@119.97.156.85:888",
  "http://hexin:hx300033@119.97.156.86:888",
  "http://hexin:hx300033@119.97.156.87:888",
  "http://hexin:hx300033@119.97.156.89:888",
  "http://hexin:hx300033@119.97.156.90:888",
  "http://hexin:hx300033@119.97.156.96:888",
  "http://hexin:hx300033@119.97.156.98:888",
  "http://hexin:hx300033@119.97.156.99:888",
  "http://hexin:hx300033@121.201.108.140:888",
  "http://hexin:hx300033@121.201.108.142:888",
  "http://hexin:hx300033@121.201.108.143:888",
  "http://hexin:hx300033@121.201.108.144:888",
  "http://hexin:hx300033@121.201.108.148:888",
  "http://hexin:hx300033@121.201.108.149:888",
  "http://hexin:hx300033@121.201.108.151:888",
  "http://hexin:hx300033@121.201.108.156:888",
  "http://hexin:hx300033@121.201.108.157:888",
  "http://hexin:hx300033@121.201.108.158:888",
  "http://hexin:hx300033@121.201.108.161:888",
  "http://hexin:hx300033@121.201.108.163:888",
  "http://hexin:hx300033@121.201.108.164:888",
  "http://hexin:hx300033@121.201.108.165:888",
  "http://hexin:hx300033@121.201.108.166:888",
  "http://hexin:hx300033@121.201.108.167:888",
  "http://hexin:hx300033@121.201.108.168:888",
  "http://hexin:hx300033@121.201.108.169:888",
  "http://hexin:hx300033@121.201.108.170:888",
  "http://hexin:hx300033@121.201.108.171:888",
  "http://hexin:hx300033@121.201.108.172:888",
  "http://hexin:hx300033@121.201.108.173:888",
  "http://hexin:hx300033@121.201.108.174:888",
  "http://hexin:hx300033@121.201.108.175:888",
  "http://hexin:hx300033@121.201.108.176:888",
  "http://hexin:hx300033@121.201.108.177:888",
  "http://hexin:hx300033@121.201.108.178:888",
  "http://hexin:hx300033@121.201.108.179:888",
  "http://hexin:hx300033@121.201.108.180:888",
  "http://hexin:hx300033@121.201.108.181:888",
  "http://hexin:hx300033@121.201.108.182:888",
  "http://hexin:hx300033@121.201.108.183:888",
  "http://hexin:hx300033@121.201.108.184:888",
  "http://hexin:hx300033@121.201.108.186:888",
  "http://hexin:hx300033@121.201.108.187:888",
  "http://hexin:hx300033@121.201.108.188:888",
  "http://hexin:hx300033@121.201.108.190:888",
  "http://hexin:hx300033@121.201.108.191:888",
  "http://hexin:hx300033@121.201.108.192:888",
  "http://hexin:hx300033@121.201.108.193:888",
  "http://hexin:hx300033@121.201.108.195:888",
  "http://hexin:hx300033@121.201.108.196:888",
  "http://hexin:hx300033@121.201.108.197:888",
  "http://hexin:hx300033@121.201.108.198:888",
  "http://hexin:hx300033@121.201.108.200:888",
  "http://hexin:hx300033@121.201.108.201:888",
  "http://hexin:hx300033@121.201.108.202:888",
  "http://hexin:hx300033@121.201.108.203:888",
  "http://hexin:hx300033@121.201.108.204:888",
  "http://hexin:hx300033@121.201.108.205:888",
  "http://hexin:hx300033@121.201.108.206:888",
  "http://hexin:hx300033@121.201.108.207:888",
  "http://hexin:hx300033@121.201.108.208:888",
  "http://hexin:hx300033@121.201.108.209:888",
  "http://hexin:hx300033@121.201.108.210:888",
  "http://hexin:hx300033@121.201.108.211:888",
  "http://hexin:hx300033@121.201.108.212:888",
  "http://hexin:hx300033@121.201.108.213:888",
  "http://hexin:hx300033@121.201.108.214:888",
  "http://hexin:hx300033@121.201.108.215:888",
  "http://hexin:hx300033@121.201.108.216:888",
  "http://hexin:hx300033@122.228.73.133:888",
  "http://hexin:hx300033@122.228.73.141:888",
  "http://hexin:hx300033@122.228.73.143:888",
  "http://hexin:hx300033@122.228.73.148:888",
  "http://hexin:hx300033@122.228.73.150:888",
  "http://hexin:hx300033@122.228.73.158:888",
  "http://hexin:hx300033@122.228.73.159:888",
  "http://hexin:hx300033@122.228.73.160:888",
  "http://hexin:hx300033@122.228.73.161:888",
  "http://hexin:hx300033@122.228.73.163:888",
  "http://hexin:hx300033@122.228.73.164:888",
  "http://hexin:hx300033@122.228.73.167:888",
  "http://hexin:hx300033@122.228.73.171:888",
  "http://hexin:hx300033@122.228.73.173:888",
  "http://hexin:hx300033@122.228.73.174:888",
  "http://hexin:hx300033@122.228.73.176:888",
  "http://hexin:hx300033@122.228.73.181:888",
  "http://hexin:hx300033@122.228.73.184:888",
  "http://hexin:hx300033@122.228.73.187:888",
  "http://hexin:hx300033@122.228.73.188:888",
  "http://hexin:hx300033@122.228.73.192:888",
  "http://hexin:hx300033@183.131.2.130:888",
  "http://hexin:hx300033@183.131.2.131:888",
  "http://hexin:hx300033@183.131.2.132:888",
  "http://hexin:hx300033@183.131.2.134:888",
  "http://hexin:hx300033@183.131.2.135:888",
  "http://hexin:hx300033@183.131.2.136:888",
  "http://hexin:hx300033@183.131.2.140:888",
  "http://hexin:hx300033@183.131.2.146:888",
  "http://hexin:hx300033@183.131.2.148:888",
  "http://hexin:hx300033@183.131.2.149:888",
  "http://hexin:hx300033@183.131.2.150:888",
  "http://hexin:hx300033@183.131.2.153:888",
  "http://hexin:hx300033@183.131.2.154:888",
  "http://hexin:hx300033@183.131.2.155:888",
  "http://hexin:hx300033@183.131.2.156:888",
  "http://hexin:hx300033@183.131.2.157:888",
  "http://hexin:hx300033@183.131.2.158:888",
  "http://hexin:hx300033@183.131.2.159:888",
  "http://hexin:hx300033@183.131.2.161:888",
  "http://hexin:hx300033@183.131.2.162:888",
  "http://hexin:hx300033@183.131.2.163:888",
  "http://hexin:hx300033@183.131.2.164:888",
  "http://hexin:hx300033@183.131.2.165:888",
  "http://hexin:hx300033@183.131.2.166:888",
  "http://hexin:hx300033@183.131.2.169:888",
  "http://hexin:hx300033@101.71.41.140:888",
  "http://hexin:hx300033@121.201.108.162:888",
  "http://hexin:hx300033@163.177.148.118:888",
  "http://hexin:hx300033@101.71.41.184:888",
  "http://hexin:hx300033@183.131.2.140:888",
  "http://hexin:hx300033@111.206.217.158:888"
]


TRADEMARK_TID_KEY = 'trademark_{reg_num}_{int_cls}'

REDIS_EXPIRE_TIME = 60 * 60 * 24 * 30     # 过期时间，一个月

RETRY = 5

NOT_TID_RECORDS = '<record/>'

MAX_CONTINUE_FAIL = 50  # 最大连续抓取错误

SLEEP_TIME = 60 * 10    # 连续抓取错误休息时间

MAX_INT_CLS = 45

NOTICE_PAGE_SIZE = 10000

NOTICE_REQUEST_TIMEOUT = 1000 * 60 * 2  # 单位毫秒


def extract_tm_name(html):
    """抽取商标名，当返回值不为空时，才允许使用"""
    tm_name = ''
    try:
        selector = etree.HTML(html)
        temp = selector.xpath('//*[@name="info:mno"]//@value')
        if temp:
            tm_name = temp[0]
    except:
        pass
    return tm_name


