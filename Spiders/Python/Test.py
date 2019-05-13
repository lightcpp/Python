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
#     response = urllib2.urlopen(request)
#     print response.read()

#     values = {"username":"light_cpp@163.com","password":"csdn134"}
#     data = urllib.urlencode(values)
#     url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
#     request = urllib2.Request(url,data,socket._GLOBAL_DEFAULT_TIMEOUT)
#     response = urllib2.urlopen(request)
#     print response.read()
    
    url = "https://www.zhihu.com/signin"
    user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    values = {"username":"1342002963@qq.com","password":"zhihu134"}
    headers = {"User-Agent":user_agent, 'Referer':'http://www.zhihu.com/'}
    data = urllib.urlencode(values)
    request = urllib2.Request(url,data,headers)
    response = urllib2.urlopen(request)
    print response.read()
    
    