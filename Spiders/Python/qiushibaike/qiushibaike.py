# -*- coding:utf-8 -*-
'''
Created on 2019年5月14日

@author: Light
'''
import urllib2
import re

# page = 0
# while page <=10:
#     page +=1
#     url = "http://www.qiushibaike.com/hot/page/" + str(page)
#     user_agent = "Mozilla/4.0(compatible;MSIE 5.5;Windows NT)" 
#     headers = {"User-Agent":user_agent}
#     req = urllib2.Request(url,headers=headers)
#     rsp = urllib2.urlopen(req)
#     content = rsp.read().decode("utf-8")
#     pattern = re.compile(r'<h2>(.*?)</h2>.*?<span>(.*?)</span>',re.S)
#     items = re.findall(pattern, content)
#     for item in items:
#         print item[0],"\n",item[1].replace("<br/>","")
#爬取糗事百科的段子和发布用户的名称
class qiushibaike:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = "Mozilla/4.0(compatible;MSIE 5.5;Windows NT)"
        #初始化headers
        self.headers = {"User-Agent":self.user_agent}
        #存放段子的变量，每一个元素是每一页的段子
        self.stories = []
        #存放程序是否继续运行的变量
        self.enable = False
    
    #获取每一页所有内容
    def getPage(self,pageIndex):
        try:
            url = "http://www.qiushibaike.com/hot/page/" + str(pageIndex)
            req = urllib2.Request(url,headers=self.headers)
            rsp = urllib2.urlopen(req)
            #转码
            page = rsp.read().decode("utf-8")
            return page
        except urllib2.URLError,e:
#             u:表示unicode字符串 
# 不是仅仅是针对中文, 可以针对任何的字符串，代表是对字符串进行unicode编码。 
# 一般英文字符在使用各种编码下, 基本都可以正常解析, 所以一般不带u；但是中文, 必须表明所需编码, 否则一旦编码转换就会出现乱码。
            print u"获取糗事百科页面信息失败，失败原因:",e.reason
            return None
    
    #获取网页中的段子列表
    def getPageItems(self,pageIndex):
        page = self.getPage(pageIndex)
        if not page:
            print "页面加载失败..."
            return None
        pattern = re.compile(r'<h2>(.*?)</h2>.*?<span>(.*?)</span>',re.S)
        items = re.findall(pattern,page)
        #存储每页的段子
        pageStories = []
        for item in items:
            replaceBR = re.compile("<br/>")
            story = re.sub(replaceBR, "\n", item[1])
            #item[0]是作者，item[1]是段子内容
            pageStories.append([item[0].strip(),story.strip()])
        return pageStories
    
    #加载并提取页面的内容，加入列表中
    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                #获取新的一页
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1
    
    #每次敲回车打印输出一个段子
    def getOneStory(self,pageStories,page):
        #遍历每一页的段子
        for story in pageStories:
            #用户输入指令
            input = raw_input()
            #如果输入Q或q则程序结束
            if input == 'Q' or input == 'q':
                self.enable = False
                return
            #每当输入回车判断是否需要加载新的页面
            self.loadPage()
            print u"第%d页\t发布人:%s\n%s" %(page,story[0],story[1])
    
    #程序启动的方法
    def start(self):
        print u"正在读取糗事百科，按回车查看下一个段子，按'Q(q)退出'"
        self.enable = True
        #先加载一页内容
        self.loadPage()
        #当前页码
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories, nowPage)

spider = qiushibaike()
spider.start()
         