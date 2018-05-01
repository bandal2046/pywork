# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
import xlrd,xlwt,os

class py:
    def __init__(self):
        self.qt_url = []
        self.ht_url = []
        self.path = os.getcwd()  # 取得当前工作目录
        self.wb = xlrd.open_workbook(self.path + '\date\url.xls')

    def date_qt(self):
        #前台数据读取
        sheet = self.wb.sheet_by_name('Sheet1')  # 通过excel表格名称(rank)获取工作表
        for i in range(sheet.nrows - 1):  # 获取表行数减一
            cells = sheet.row_values(i + 1)  # 取下标行加一的数据
            case = cells[0]
            self.qt_url.append(cells[1])
            #print u"链接：%s\t " %(self.run[i])
        return self.qt_url

    def date_ht(self):
        #后台数据读取
        sheet = self.wb.sheet_by_name('Sheet2')  # 通过excel表格名称(rank)获取工作表
        for i in range(sheet.nrows - 1):  # 获取表行数减一
            cells = sheet.row_values(i + 1)  # 取下标行加一的数据
            case = cells[0]
            self.ht_url.append(cells[1])
            #print u"链接：%s\t " %(self.ht_url[i])
        return self.ht_url

    def login_qt(self):
        # 设置保存cookie的文件，同级目录下的cookie.txt
        filename = 'cookie.txt'
        # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
        cookie = cookielib.MozillaCookieJar(filename)
        # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
        opener_qt = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        postdata = urllib.urlencode({
            'UserName': '18684891869',
            'Password': '123456'
        })
        # 登录URL
        loginUrl = 'https://vshop.xiaokeduo.com/mid2948/did0/Account/Login'
        # 模拟登录，并把cookie保存到变量
        opener_qt.open(loginUrl, postdata)
        # 保存cookie到cookie.txt中
        cookie.save(ignore_discard=True, ignore_expires=True)
        return opener_qt

    def login_ht(self):
        # 设置保存cookie的文件，同级目录下的cookie.txt
        filename = 'cookie_ht.txt'
        # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
        cookie = cookielib.MozillaCookieJar(filename)
        # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
        opener_ht = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        postdata = urllib.urlencode({
            'Telphone': '18573175650',
            'Password': '123456'
        })
        # 登录URL
        loginUrl_ht = 'https://passport.xiaokeduo.com/Login/Index2?ReturnUrl=https%3A%2F%2Fmy.xiaokeduo.com%2Fstore%3Ftype%3D3&channelId=18'
        # 模拟登录，并把cookie保存到变量
        opener_ht.open(loginUrl_ht, postdata)
        # 保存cookie到cookie.txt中
        cookie.save(ignore_discard=True, ignore_expires=True)
        return opener_ht
        '''
        url = 'https://my.xiaokeduo.com/ProductInfo/ProductList'
        jg  = opener_ht.open(url)  # 在此执行
        xl = jg.read().decode('utf-8')
        print 'aa:',xl
        
        '''

    def check(self):
        #URL = 'https://vshop.xiaokeduo.com/mid2948/did215157/Distributor'
        url_qt = self.date_qt()
        url_ht = self.date_ht()

        req_qt = self.login_qt()
        req_ht = self.login_ht()

        print u'待检测链接共:',len(url_qt)+len(url_ht),u'条','\n'

        filename = 'Excel_Workbook.xls'  # 检测当前目录下是否有Excel_Workbook.xls文件，如果有则清除以前保存文件
        if os.path.exists(filename):
            os.remove(filename)
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('My Sheet')
        worksheet1 = workbook.add_sheet('My Sheet1')

        # worksheet.col.width = 0x0d00 + 50
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = 'Times New Roman'  # 设置字体
        font.bold = True  # 黑体
        style.font = font  # 设定样式
        worksheet.write(0, 1, 'URL', style)  # 带样式的写入

        for i in range(len(url_qt)):
            print '执行链接检查：:', url_qt[i]
            #req = urllib2.Request(url[i])
            try:
                encode = req_qt.open(url_qt[i]).code#在此执行
                print u"成功状态码：",encode,'\n'
                worksheet.write(1 + i, 1, label=url_qt[i])  # 写入URL
                worksheet.write(1 + i, 2, req_qt.open(url_qt[i]).code)  # 写入code
            except urllib2.HTTPError, e:
                print u'失败状态码：',e.code
                print u'失败原因：',e.reason,'\n'
                worksheet.write(1 + i, 1, label=url_qt[i])  # 写入URL
                worksheet.write(1 + i, 2, e.code)  # 写入code
                worksheet.write(1 + i, 3, e.reason)  # 写入失败原因

        for i in range(len(url_ht)):
            print '执行链接检查：:', url_ht[i]
            #req_ht = urllib2.Request(url_ht[i])
            try:
                encode = req_ht.open(url_ht[i]).code#在此执行
                print u"成功状态码：",encode,'\n'
                worksheet1.write(1 + i, 1, label=url_ht[i])  # 写入URL
                worksheet1.write(1 + i, 2, req_ht.open(url_ht[i]).code)  # 写入code
            except urllib2.HTTPError, e:
                print u'失败状态码：',e.code
                print u'失败原因：',e.reason,'\n'
                worksheet1.write(1 + i, 1, label=url_ht[i])  # 写入URL
                worksheet1.write(1 + i, 2, e.code)  # 写入code
                worksheet1.write(1 + i, 3, e.reason)  # 写入失败原因
        workbook.save('Excel_Workbook.xls')

        #print req.open(url[2]).read()


    def report(self, url):
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('My Sheet')
        worksheet.write(1, 1, label=url[i])
        workbook.save('Excel_Workbook.xls')

w1 = py()
w1.check()
#w1.login_ht()
