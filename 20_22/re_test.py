# encoding: UTF-8
import re
'''
#将正则表达式编译成Pattern对象
#pattern = re.compile(r'hello')
pattern = re.compile(r"abc")
#使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('abc')

if match:
    #使用Match获得分组信息
    print match.group()

m = re.match(r'a\dc', 'abc')
print m
# a = re.compile(r'\d+\.\d*', re.x)
'''
#compile()
tt = "Tina is a dgoodz girl, she is dcoolz, clever, and so on..."
rr = re.compile(r'\w*z\w*')
print(rr.findall(tt))

#match()
print (re.match('com','comwww.runcomoob').group())
print(re.match('com','Comwww.runcomoob',re.I).group())

#search()
print(re.search('\dcom','www.4comrunoob.5com').group())

a = "123abc456"
#123abc456,返回整体
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0))
#123
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1))
#abc
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2))
#456
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3))

