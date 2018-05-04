# -*- coding: utf-8 -*-
import urllib
import urllib2
import cookielib
import xlrd,xlwt,os

class py:
    def __init__(self):
        #设置请求头
        self.loginHeaders =  {
            'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cache-Control':'Cache-Control',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Connection' : 'keep-alive',
            'Pragma':'no-cache',
            'X-Requested-With':'XMLHttpRequest'
        }
        self.qt_url = []  # 前台URL
        self.ht_url = []  # 后台URL
        self.dlzx_url = []  # 代理中心
        self.dlsht_url = []   # 代理商后台
        self.gysht_url = []   # 供应商后台
        self.path = os.getcwd()  # 取得当前工作目录
        self.wb = xlrd.open_workbook(self.path + '\date\url.xls')

    def date_qt(self):
        #前台数据读取
        sheet = self.wb.sheet_by_name(u'前台')  # 通过excel表格名称(rank)获取工作表
        case = []
        for i in range(sheet.nrows - 1):  # 获取表行数减一
            cells = sheet.row_values(i + 1)  # 取下标行加一的数据
            case.append(cells[0])
            self.qt_url.append(cells[1])
            #print u"链接：%s\t " %(self.run[i])
        #case = sheet.row_values(i + 1)
        return case

    def date_ht(self):
        #后台数据读取
        sheet = self.wb.sheet_by_name(u'后台')  # 通过excel表格名称(rank)获取工作表
        case = []
        for i in range(sheet.nrows - 1):  # 获取表行数减一
            cells = sheet.row_values(i + 1)  # 取下标行加一的数据
            case.append(cells[0])
            self.ht_url.append(cells[1])
            #print u"链接：%s\t " %(self.ht_url[i])
        return case

    def date_dlzx(self):
        # 代理中心数据读取
        sheet = self.wb.sheet_by_name(u'代理中心')  # 通过excel表格名称(rank)获取工作表
        case = []
        for i in range(sheet.nrows - 1):  # 获取表行数减一
            cells = sheet.row_values(i + 1)  # 取下标行加一的数据
            case.append(cells[0])
            self.dlzx_url.append(cells[1])
            #print u"链接：%s\t " %(self.ht_url[i])
        return case

    def date_dlsht(self):
        #代理商后台数据读取
        sheet = self.wb.sheet_by_name(u'代理商后台')  # 通过excel表格名称(rank)获取工作表
        case = []
        for i in range(sheet.nrows - 1):  # 获取表行数减一
            cells = sheet.row_values(i + 1)  # 取下标行加一的数据
            case.append(cells[0])
            self.dlsht_url.append(cells[1])
        return case

    def date_gysht(self):
        #供应商后台数据读取
        sheet = self.wb.sheet_by_name(u'供应商后台')  # 通过excel表格名称(rank)获取工作表
        case = []
        for i in range(sheet.nrows - 1):  # 获取表行数减一
            cells = sheet.row_values(i + 1)  # 取下标行加一的数据
            case.append(cells[0])
            self.gysht_url.append(cells[1])
        return case


    def login_qt(self):
        # 获取前台登录cookie
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

    def login_dlzx(self):
        # 获取代理商中心登录cookie
        # 设置保存cookie的文件，同级目录下的cookie.txt
        filename = 'cookie_dlzx.txt'
        # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
        cookie = cookielib.MozillaCookieJar(filename)
        # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
        opener_dlzx = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        postdata = urllib.urlencode({
            'UserName': '18784891869',
            'Password': '123456'
        })
        # 登录URL
        loginUrl = 'https://vshop.xiaokeduo.com/mid2948/did0/Account/Login'
        # 模拟登录，并把cookie保存到变量
        opener_dlzx.open(loginUrl, postdata)
        # 保存cookie到cookie.txt中
        cookie.save(ignore_discard=True, ignore_expires=True)
        return opener_dlzx

    def login_ht(self):
        # 获取后台登录cookie
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

    def login_dlsht(self):
        # 获取代理商登录cookie
        # 设置保存cookie的文件，同级目录下的cookie.txt
        filename = 'cookie_dlsht.txt'
        # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
        cookie = cookielib.MozillaCookieJar(filename)
        # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
        opener_dlsht = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        postdata = urllib.urlencode({
            'code': 'j2w3',
            'ReturnUrl': '/mid2948/Agents',
            'UserName': '18784891869',
            'Password': '123456'
        })
        #获取登录验证码
        url_code = 'https://agent.xiaokeduo.com/mid2948/Account/ValidateCodeImg'
        opener_dlsht.open(url_code)
        # 登录URL
        loginUrl_dlsht = 'https://agent.xiaokeduo.com/mid2948/Account/Login'
        # 模拟登录，并把cookie保存到变量
        opener_dlsht.open(loginUrl_dlsht, postdata)
        # 保存cookie到cookie.txt中
        cookie.save(ignore_discard=True, ignore_expires=True)

        '''
        url = 'https://agent-online.xiaokeduo.com/mid2948/Agents/AgentsList'
        jg  = opener_dlsht.open(url)  # 在此执行
        xl = jg.read().decode('utf-8')
        print 'dlsht:',xl
        '''
        return opener_dlsht

    def login_gysht(self):
        # 获取供应商后台登录cookie
        # 设置保存cookie的文件，同级目录下的cookie.txt
        filename = 'cookie_gysht.txt'
        # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
        cookie = cookielib.MozillaCookieJar(filename)
        # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
        opener_gysht = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        postdata = urllib.urlencode({
            'code': '8734',
            'ReturnUrl': '/mid/2948/SupplierOrder',
            'UserName': '13100131001',
            'Password': '123456'
        })

        #获取登录验证码
        url_code = 'https://gys.xiaokeduo.com/mid/2948/Account/ValidateCodeImg'
        opener_gysht.open(url_code)
        # 登录URL
        loginUrl_gysht = 'https://gys.xiaokeduo.com/mid/2948/Account/Login'
        #构建请求
        request = urllib2.Request(loginUrl_gysht, postdata, self.loginHeaders)
        # 模拟登录，并把cookie保存到变量
        opener_gysht.open(request)
        # 保存cookie到cookie.txt中
        cookie.save(ignore_discard=True, ignore_expires=True)
        '''
        url = 'http://gys.xiaokeduo.com/mid/2948/SupplierOrder'
        jg  = opener_gysht.open(url)  # 在此执行
        xl = jg.read().decode('utf-8')
        print 'gysht:',xl
        '''
        return opener_gysht

    def check(self):
        #URL = 'https://vshop.xiaokeduo.com/mid2948/did215157/Distributor'
        name_qt = self.date_qt() # 前台URL
        name_ht = self.date_ht() # 前台URL
        name_dlzx = self.date_dlzx() #代理中心URL
        name_dlsht = self.date_dlsht() #代理商后台
        name_gysht = self.date_gysht() #供应商后台

        req_qt = self.login_qt()  # 前台带cookie的open
        req_ht = self.login_ht()  # 后台带cookie的open
        req_dlzx = self.login_dlzx()  # 代理中心cookie的open
        req_dlsht = self.login_dlsht() # 代理商后台cookie的open
        req_gysht = self.login_gysht() # 供应商后台cookie的open

        print u'待检测链接共:',len(self.qt_url)+len(self.ht_url)+len(self.dlzx_url)+len(self.dlsht_url)+len(self.gysht_url),u'条','\n'

        filename = 'Excel_Workbook.xls'  # 检测当前目录下是否有Excel_Workbook.xls文件，如果有则清除以前保存文件
        if os.path.exists(filename):
            os.remove(filename)
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding='utf-8')

        '''
        worksheet = workbook.add_sheet('My Sheet') #   前台
        worksheet1 = workbook.add_sheet('My Sheet1') #  后台
        worksheet2 = workbook.add_sheet('My Sheet2') #  代理中心
        '''
        sheetname = [u'前台',u'后台',u'代理商中心',u'代理商后台',u'供应商后台']
        WorkSheetGroup = []
        for i in range(len(sheetname)):
            WorkSheetGroup.append(workbook.add_sheet(sheetname[i]))
        '''
        worksheet = workbook.add_sheet(u'前台') #   前台
        worksheet1 = workbook.add_sheet(u'后台') #  后台
        worksheet2 = workbook.add_sheet(u'代理商中心') #  代理中心
        worksheet3 = workbook.add_sheet(u'代理商后台')  # 代理商后台
        worksheet4 = workbook.add_sheet(u'供应商后台')  # 供应商后台
        '''
        # worksheet.col.width = 0x0d00 + 50
        style = xlwt.XFStyle()  # 初始化样式
        font = xlwt.Font()  # 为样式创建字体
        font.name = 'Times New Roman'  # 设置字体
        font.bold = True  # 黑体
        style.font = font  # 设定样式
        for i in range(len(sheetname)):
            print 'type:',WorkSheetGroup[i]

        for i in range(len(sheetname)):
            WorkSheetGroup[i].write(0, 0, 'Module', style)  # 带样式的写入
            WorkSheetGroup[i].write(0, 1, 'URL', style)  # 带样式的写入
            WorkSheetGroup[i].write(0, 2, 'Code', style)  # 带样式的写入

        '''
        worksheet.write(0, 0, 'Module', style)  # 带样式的写入
        worksheet.write(0, 1, 'URL', style)  # 带样式的写入
        worksheet.write(0, 2, 'Code', style)  # 带样式的写入

        worksheet1.write(0, 0, 'Module', style)  # 带样式的写入
        worksheet1.write(0, 1, 'URL', style)  # 带样式的写入
        worksheet1.write(0, 2, 'Code', style)  # 带样式的写入

        worksheet2.write(0, 0, 'Module', style)  # 带样式的写入
        worksheet2.write(0, 1, 'URL', style)  # 带样式的写入
        worksheet2.write(0, 2, 'Code', style)  # 带样式的写入
        '''

        for i in range(len(self.qt_url)):
            #前台
            print '执行链接检查：:', self.qt_url[i]
            #req = urllib2.Request(url[i])
            try:
                encode = req_qt.open(self.qt_url[i]).code#在此执行
                print u"成功状态码：",encode,'\n'
                '''
                worksheet.write(1 + i, 0, label=name_qt[i])  # 前台模块名
                worksheet.write(1 + i, 1, label=self.qt_url[i])  # 写入URL
                worksheet.write(1 + i, 2, req_qt.open(self.qt_url[i]).code)  # 写入code
                '''
                WorkSheetGroup[0].write(1 + i, 0, label=name_qt[i])  # 前台模块名
                WorkSheetGroup[0].write(1 + i, 1, label=self.qt_url[i])  # 写入URL
                WorkSheetGroup[0].write(1 + i, 2, req_qt.open(self.qt_url[i]).code)  # 写入code
            except urllib2.HTTPError, e:
                print u'失败状态码：',e.code
                print u'失败原因：',e.reason,'\n'
                '''
                worksheet.write(1 + i, 0, label=name_qt[i])  # 前台模块名
                worksheet.write(1 + i, 1, label=self.qt_url[i])  # 写入URL
                worksheet.write(1 + i, 2, e.code)  # 写入code
                worksheet.write(1 + i, 3, e.reason)  # 写入失败原因
                '''
                WorkSheetGroup[0].write(1 + i, 0, label=name_qt[i])  # 前台模块名
                WorkSheetGroup[0].write(1 + i, 1, label=self.qt_url[i])  # 写入URL
                WorkSheetGroup[0].write(1 + i, 2, e.code)  # 写入code
                WorkSheetGroup[0].write(1 + i, 3, e.reason)  # 写入失败原因

        for i in range(len(self.ht_url)):
            # 后台
            print '执行链接检查：:', self.ht_url[i]
            #req_ht = urllib2.Request(url_ht[i])
            try:
                encode = req_ht.open(self.ht_url[i]).code#在此执行
                print u"成功状态码：",encode,'\n'
                WorkSheetGroup[1].write(1 + i, 0, label=name_ht[i])  # 后台模块名
                WorkSheetGroup[1].write(1 + i, 1, label=self.ht_url[i])  # 写入URL
                WorkSheetGroup[1].write(1 + i, 2, req_ht.open(self.ht_url[i]).code)  # 写入code
            except urllib2.HTTPError, e:
                print u'失败状态码：',e.code
                print u'失败原因：',e.reason,'\n'
                WorkSheetGroup[1].write(1 + i, 0, label=name_ht[i])  # 后台模块名
                WorkSheetGroup[1].write(1 + i, 1, label=self.ht_url[i])  # 写入URL
                WorkSheetGroup[1].write(1 + i, 2, e.code)  # 写入code
                WorkSheetGroup[1].write(1 + i, 3, e.reason)  # 写入失败原因

        for i in range(len(self.dlzx_url)):
            # 代理中心
            print '执行链接检查：:', self.dlzx_url[i]
            #req_ht = urllib2.Request(url_ht[i])
            try:
                encode = req_dlzx.open(self.dlzx_url[i]).code#在此执行
                print u"成功状态码：",encode,'\n'
                WorkSheetGroup[2].write(1 + i, 0, label=name_dlzx[i])  # 代理中心模块名
                WorkSheetGroup[2].write(1 + i, 1, label=self.dlzx_url[i])  # 写入URL
                WorkSheetGroup[2].write(1 + i, 2, req_dlzx.open(self.dlzx_url[i]).code)  # 写入code
            except urllib2.HTTPError, e:
                print u'失败状态码：',e.code
                print u'失败原因：',e.reason,'\n'
                WorkSheetGroup[2].write(1 + i, 0, label=name_dlzx[i])  # 代理中心模块名
                WorkSheetGroup[2].write(1 + i, 1, label=self.dlzx_url[i])  # 写入URL
                WorkSheetGroup[2].write(1 + i, 2, e.code)  # 写入code
                WorkSheetGroup[2].write(1 + i, 3, e.reason)  # 写入失败原因
        for i in range(len(self.dlsht_url)):
            # 代理商后台
            print '执行链接检查：:', self.dlsht_url[i]
            #req_ht = urllib2.Request(url_ht[i])
            try:
                encode = req_dlsht.open(self.dlsht_url[i]).code#在此执行
                print u"成功状态码：",encode,'\n'
                WorkSheetGroup[3].write(1 + i, 0, label=name_dlsht[i])  # 代理中心模块名
                WorkSheetGroup[3].write(1 + i, 1, label=self.dlsht_url[i])  # 写入URL
                WorkSheetGroup[3].write(1 + i, 2, req_dlsht.open(self.dlsht_url[i]).code)  # 写入code
            except urllib2.HTTPError, e:
                print u'失败状态码：',e.code
                print u'失败原因：',e.reason,'\n'
                WorkSheetGroup[3].write(1 + i, 0, label=name_dlsht[i])  # 代理中心模块名
                WorkSheetGroup[3].write(1 + i, 1, label=self.dlsht_url[i])  # 写入URL
                WorkSheetGroup[3].write(1 + i, 2, e.code)  # 写入code
                WorkSheetGroup[3].write(1 + i, 3, e.reason)  # 写入失败原因
        for i in range(len(self.gysht_url)):
            # 供应商后台
            print '执行链接检查：:', self.gysht_url[i]
            #req_ht = urllib2.Request(url_ht[i])
            try:
                encode = req_gysht.open(self.gysht_url[i]).code#在此执行
                print u"成功状态码：",encode,'\n'
                WorkSheetGroup[4].write(1 + i, 0, label=name_gysht[i])  # 代理中心模块名
                WorkSheetGroup[4].write(1 + i, 1, label=self.gysht_url[i])  # 写入URL
                WorkSheetGroup[4].write(1 + i, 2, req_gysht.open(self.gysht_url[i]).code)  # 写入code
            except urllib2.HTTPError, e:
                print u'失败状态码：',e.code
                print u'失败原因：',e.reason,'\n'
                WorkSheetGroup[4].write(1 + i, 0, label=name_gysht[i])  # 代理中心模块名
                WorkSheetGroup[4].write(1 + i, 1, label=self.gysht_url[i])  # 写入URL
                WorkSheetGroup[4].write(1 + i, 2, e.code)  # 写入code
                WorkSheetGroup[4].write(1 + i, 3, e.reason)  # 写入失败原因
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
#w1.login_dlsht()
