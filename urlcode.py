# -*- coding: utf-8 -*-
import urllib2
import xlrd,os

import urllib
class py:
    def __init__(self):
        self.run = []
    def url(self):
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

    def check(self):
        #URL = 'https://vshop.xiaokeduo.com/mid2948/did215157/Distributor'
        url = self.url()
        print u'待检测链接共:',len(url),u'条','\n'

        for i in range(len(url)):
            print '执行链接检查：:', url[i]
            req = urllib2.Request(url[i])
            try:
                urllib2.urlopen(req)
                print u'成功状态码：',urllib2.urlopen(req).code,'\n'
            except urllib2.HTTPError, e:
                print u'失败状态码：',e.code
                print u'失败原因：',e.reason,'\n'

w1 = py()
w1.check()
#except urllib2.URLError, e:

'''
url = 'https://vshop.xiaokeduo.com/mid2948/did215157/Distributo'
response = None
try:
  response = urllib2.urlopen(url,timeout=5)
except urllib2.URLError as e:
  if hasattr(e, 'code'):
    print 'Error code:',e.code
  elif hasattr(e, 'reason'):
    print 'Reason:',e.reason
finally:
  if response:
    response.close()
'''