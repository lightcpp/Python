#-*- coding:utf-8 -*-
'''
Created on 2019年5月10日

@author: Light

'''
import urllib2

if __name__ == '__main__':
# URLError
#     request = urllib2.Request("http://www.swerwq54.com")
#     try:
#         urllib2.urlopen(request)
#     except urllib2.URLError,e:
#         print e.reason

# HTTPError
# HTTPError是URLError的子类，在你利用urlopen方法发出一个请求时，服务器上都会对应一个应答对象response，其中它包含一个数字”状态码”。举个例子，假如response是一个”重定向”，需定位到别的地址获取文档，urllib2将对此进行处理。
    req = urllib2.Request("http://blog.csdn.net/xxx")
    try:
        rsp = urllib2.urlopen(req)
#         print rsp.read()
    except urllib2.HTTPError,e:
        print "HTTPError:"+str(e.code)
    except urllib2.URLError,e:
        print "URLError"+e.reason
    else:
        print "SUCCESS"