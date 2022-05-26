#coding=utf-8
import urllib
import urllib2
'''
#Post方式
values = {"username":"1016903103@qq.com","password":"XXX"}#创建一个字典
data = urllib.urlencode(values)#对字典编码
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)#构造Request
reponse = urllib2.urlopen(request)
print reponse.read()
'''
#GET方式
values={}#定义一个字典，[]定义列表，()定义元组
values['username']="1016903103@qq.com"
values['password']='XXXX'
data = urllib.urlencode(values)#字典编码
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
urllib2.Request
response = urllib2.urlopen(request)
print values
print geturl
#print response.read()

#总结：
'''
1、由urlencode将字典编码如：用户名和密码数据，提交时还原成服务器可接受编码
2、通过Request构造请求数据如：URL、编码后的数据
3、urlopen发起请求
'''