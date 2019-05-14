#-*- coding:utf-8 -*-
'''
Created on 2019年5月7日

@author: Light
'''
import urllib2
import urllib
import socket
if __name__ == '__main__':
#     request = urllib2.Request("http://www.baidu.com")
#     response = urllib2.urlopen(request,timeout=10)
#     print response.read()

#     values = {"username":"light_cpp@163.com","password":"csdn134"}
#     data = urllib.urlencode(values)
#     url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
#     request = urllib2.Request(url,data,socket._GLOBAL_DEFAULT_TIMEOUT)
#     response = urllib2.urlopen(request)
#     print response.read()
    
# User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
# Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
# application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
# application/json ： 在 JSON RPC 调用时使用
# application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
# 在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务
#     url = "https://www.zhihu.com/signin"
#     user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
#     values = {"username":"1342002963@qq.com","password":"zhihu134"}
#     headers = {"User-Agent":user_agent, 'Referer':'http://www.zhihu.com/'}
#     data = urllib.urlencode(values)
#     request = urllib2.Request(url,data,headers=headers)
#     response = urllib2.urlopen(request)
#     print response.read()
# 使用DebugLog
    httpHandler = urllib2.HTTPHandler(debuglevel = 1)
    httpsHandler = urllib2.HTTPSHandler(debuglevel= 1)
    opener = urllib2.build_opener(httpHandler,httpsHandler)
    urllib2.install_opener(opener)
    response = urllib2.urlopen("http://www.baidu.com")
    