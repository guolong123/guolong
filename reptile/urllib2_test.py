# coding=utf-8

import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def getHtml(url):
    '''此方法用来将传入的url进行访问并返回html数据'''
    try:
        header = {'Accept': 'image / webp, image / *, * / *;q = 0.8',
                  'Accept - Encoding': 'gzip, deflate, sdch',
                  'Accept-Language': 'zh-CN,zh;q=0.8',
                  'Proxy-Connection': 'keep-alive',
                  'Referer': 'http://kan.sogou.com/dianying/',
                  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'


        }
        request = urllib2.Request(url, headers=header)
        response = urllib2.urlopen(request)
        html = response.read()
        return html
    except Exception, e:  # 异常处理，如果网络异常的情况下会报错
        return e
