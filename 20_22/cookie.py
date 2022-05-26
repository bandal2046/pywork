# -*- coding:utf-8 -*-
import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
    'UserName': '18684891869',
    'Password': '123456'
})
# 登录教务系统的URL
loginUrl = 'https://vshop.xiaokeduo.com/mid2948/did0/Account/Login'
# 模拟登录，并把cookie保存到变量
result = opener.open(loginUrl, postdata)
# 保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)
# 利用cookie请求访问另一个网址，此网址是成绩查询网址
gradeUrl = 'https://vshop.xiaokeduo.com/mid2948/did215157/MemberCenter/index'
# 请求访问成绩查询网址
result = opener.open(gradeUrl)
print result.read()
