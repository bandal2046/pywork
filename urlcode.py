# -*- coding: utf-8 -*-
import urllib2
import cookielib
import xlrd,xlwt,os
import urllib

class py:
    def __init__(self):
        self.run = []
    def date(self):
        path = os.getcwd()#取得当前工作目录
        #print path
        wb = xlrd.open_workbook(path+'\date\url.xls')
        sheet = wb.sheet_by_name('Sheet1')  # 通过excel表格名称(rank)获取工作表
        for i in range(sheet.nrows - 1):  # 获取表行数减一
            cells = sheet.row_values(i + 1)  # 取下标行加一的数据
            case = cells[0]
            self.run.append(cells[1])
            #print u"链接：%s\t " %(self.run[i])
        return self.run

    def login_qt(self):
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
        opener.open(loginUrl, postdata)
        # 保存cookie到cookie.txt中
        cookie.save(ignore_discard=True, ignore_expires=True)
        return opener

    def check(self):
        #URL = 'https://vshop.xiaokeduo.com/mid2948/did215157/Distributor'
        url = self.date()
        req = self.login_qt()
        print u'待检测链接共:',len(url),u'条','\n'

        filename = 'Excel_Workbook.xls'  # 检测当前目录下是否有Excel_Workbook.xls文件，如果有则清除以前保存文件
        if os.path.exists(filename):
            os.remove(filename)
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('My Sheet')
        # worksheet.col.width = 0x0d00 + 50
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = 'Times New Roman'  # 设置字体
        font.bold = True  # 黑体
        style.font = font  # 设定样式
        worksheet.write(0, 1, 'URL', style)  # 带样式的写入

        for i in range(len(url)):
            print '执行链接检查：:', url[i]
            #req = urllib2.Request(url[i])
            try:
                encode = req.open(url[i]).code
                #print u'成功状态码：',urllib2.urlopen(req).code,'\n'
                print u"成功状态码：",encode,'\n'
                worksheet.write(1 + i, 1, label=url[i])  # 写入URL
                #worksheet.write(1 + i, 2, urllib2.urlopen(req).code)  # 写入code
                worksheet.write(1 + i, 2, req.open(url[i]).code)  # 写入code
            except urllib2.HTTPError, e:
                print u'失败状态码：',e.code
                print u'失败原因：',e.reason,'\n'
                worksheet.write(1 + i, 1, label=url[i])  # 写入URL
                worksheet.write(1 + i, 2, e.code)  # 写入code
                worksheet.write(1 + i, 3, e.reason)  # 写入失败原因
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
