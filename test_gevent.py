from gevent import monkey
monkey.patch_socket()
import gevent


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0)

n = 50
g1 = gevent.spawn(f, n)
g2 = gevent.spawn(f, n)
g3 = gevent.spawn(f, n)
g1.join()
g2.join()
g3.join()

import urllib2


def f(url):
    print('GET: %s' % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
    gevent.spawn(f, 'http://www.python.org/'),
    gevent.spawn(f, 'http://www.yahoo.com/'),
    gevent.spawn(f, 'http://www.baidu.com/'),
])
