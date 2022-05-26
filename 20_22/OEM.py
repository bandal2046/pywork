# -*- coding:utf-8 -*-
import urllib
import urllib2
import cookielib
import re
import thread
import time

#OME
class QSBK:

    #初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 'index'
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        #初始化headers
        self.headers = {'User-Agent' :self.user_agent}
        #存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        #存放程序是否继续运行的变量
        self.enable = False
    #传入某一页的索引获得页面代码
    def getPage(self,pageIndex):
        # 设置保存cookie的文件，同级目录下的cookie.txt
        filename = 'cookie.txt'
        # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
        cookie = cookielib.MozillaCookieJar(filename)
        # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        postdata = urllib.urlencode({
            'UserName': '18684891869',
            'Password': '123456'
        })
        # 登录URL
        loginUrl = 'https://vshop.xiaokeduo.com/mid2948/did0/Account/Login'
        # 模拟登录，并把cookie保存到变量
        result = opener.open(loginUrl, postdata)
        # 保存cookie到cookie.txt中
        cookie.save(ignore_discard=True, ignore_expires=True)
        # 利用cookie请求访问另一个网址
        gradeUrl = 'https://vshop.xiaokeduo.com/mid2948/did215157/distributor/index'
        # 请求访问会员中心
        response = opener.open(gradeUrl)
        pageCode = response.read().decode('utf-8')
        return pageCode
        '''
        try:
            self.url = 'https://vshop.xiaokeduo.com/mid2948/did0/Product/' + str(pageIndex)
            #构建请求的request
            request = urllib2.Request(self.url,headers=self.headers)
            #利用urlopen获取页面代码headers
            response = urllib2.urlopen(request)
            #将页面转化为UTF-8编码
            #pageCode = response
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接糗事百科失败，错误原因",e.reason
                #print "error",e.reason
                return None
        '''
    #传入某一页代码，返回本页不带图片的段子列表
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print u"页面加载失败..."
            return None
        '''
        href_re = re.compile('href="(.*?)"', re.S)
        src_re = re.compile('src="(.*?)"', re.S)

        items = re.findall(href_re, pageCode)
        items_1 = re.findall(src_re, pageCode)
        '''

        https = re.compile('https:(.*?)"',re.S)
        http = re.compile('http:(.*?)\)"', re.S)
        http1 = re.compile('http:(.*?)"', re.S)
        title = re.compile('<title>(.*?)</title>', re.S)
        
        items = re.findall(title, pageCode)
        items_1 = re.findall(http, pageCode)
        items_2 = re.findall(http1, pageCode)
        items_3 = re.findall(https, pageCode)

        #用来存储每页的段子们
        pageStories = []

        #遍历正则表达式匹配的信息
        for item in items:
                #intem[0]是一个段子的发布者，item[1]是内容，item[2]好笑数
                pageStories.append([item.strip()])

        for item in items_1:
            pageStories.append([item.strip()])

        for item in items_2:
            pageStories.append([item.strip()])

        for item in items_3:
            pageStories.append([item.strip()])

        return pageStories

    #加载并提取页面的内容，加入到列表中
    def loadPage(self):
        #如果当前未看到的页数少于2页，则加载新一页
        if self.enable==True:
            #首次运行，self.stories列表为空，所以进入if块
            if len(self.stories)<1:
                #获取新一页
                pageStories = self.getPageItems(self.pageIndex)
                #将该页的段子存放到全局list中
                if pageStories:
                    self.stories.append(pageStories)
                    #获取完之后页码索引加一，表示下一次读取下一页
                    #self.pageIndex +=1

    #调用该方法，每次敲回车打印输出一个段子
    def getOneStory(self,pageStories,page):
        print u'当前页共有链接：',len(pageStories),u'条'

        #遍历一页的段子
        for story in pageStories:
            '''
            #等待用户输入
            input = raw_input()
            #每当输入回车一次，判断一下是否要加载新页面
            self.loadPage()
            '''
            # 如果输入Q则程序结束
            if input == "Q":
                self.enable = False
                return
            #print "第%d条\t链接：%s\t " %(page,story)
            page +=1
            print page,story[0]

    #开始方法
    def start(self):
        print u'正在读取，回车查看，Q退出'
        #使变量为True，程序可以正常运行
        self.enable = True
        #先加载一页内容
        self.loadPage()
        #局部变量，控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                #从全局list中获取一页的段子
                pageStories = self.stories[0]
                #当前读到的页数加一
                nowPage ==0
                #将全局list中第一个元素删除，因为已经取出
                del self.stories[0]
                #输出该页段子
                self.getOneStory(pageStories,nowPage)

spider = QSBK()
spider.start()