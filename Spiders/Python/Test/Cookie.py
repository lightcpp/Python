#-*- coding:utf-8 -*-
'''
Created on 2019年5月10日

@author: Light
'''
import cookielib
import urllib2
import urllib

if __name__ == '__main__':
# Cookie，指某些网站为了辨别用户身份、进行session跟踪而储存在用户本地终端上的数据（通常经过加密）
# 
# 比如说有些网站需要登录后才能访问某个页面，在登录之前，你想抓取某个页面内容是不允许的。那么我们可以利用Urllib2库保存我们登录的Cookie，然后再抓取其他页面就达到目的了。
# 1）获取Cookie保存到变量
#     #声明一个CookieJar对象实例来保存cookie
#     cookie = cookielib.CookieJar()
#     #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
#     handler = urllib2.HTTPCookieProcessor(cookie)
#     #构建opener
#     opener = urllib2.build_opener(handler)
#     rsp = opener.open("http://www.baidu.com")
#     for item in cookie:
#         print "name = "+item.name
#         print "value = "+item.value
    
    
# 2）保存Cookie到文件
#     #设置保存cookie的文件，同级目录下的cookie.txt
#     filename = "D:/cookie.txt"
#     cookie = cookielib.MozillaCookieJar(filename)
#     #创建cookie处理器
#     handler = urllib2.HTTPCookieProcessor(cookie)
#     #通过handler构建opener
#     opener = urllib2.build_opener(handler)
#     #创建一个请求
#     rsp = opener.open("http://www.baidu.com")
#     #保存cookie到文件
#     cookie.save(ignore_discard=True, ignore_expires=True)

# 3）从文件中获取Cookie并访问
#     #创建MozillaCookieJar实例对象
#     cookie = cookielib.MozillaCookieJar()
#     #从文件中读取cookie内容到变量
#     cookie.load("D:/cookie.txt", ignore_discard=True, ignore_expires=True)
#     #创建请求
#     req = urllib2.Request("http://www.baidu.com")
#     #创建handler
#     handler = urllib2.HTTPCookieProcessor(cookie)
#     #创建opener
#     opener = urllib2.build_opener(handler)
#     rsp = opener.open(req)
#     print rsp.read()

#  4）利用cookie模拟网站登录
    filename = "D:/cookie.txt"
    cookie = cookielib.MozillaCookieJar(filename)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    values = {"username":"1342002963@qq.com","password":"zhihu134"}
    postdata = urllib.urlencode(values)
    #登录的URl
    loginUrl = "https://www.zhihu.com/signin"
    #模拟登录，并把cookie保存到变量
    result = opener.open(loginUrl, postdata)
    print result.read()
    #保存cookie到文件
    cookie.save(ignore_discard=True, ignore_expires=True)
    #利用cookie访问一个私人网址
    privateUrl = "https://www.zhihu.com/people/light-cui-31/activities"
    rsp = opener.open(privateUrl)
    print rsp.read()
    