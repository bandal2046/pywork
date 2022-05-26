#coding=utf-8
'''
urllib模块的URL编码解码功能
我们知道，url 中是不能出现一些特殊的符号的，有些符号有特殊的用途。
比如以 get 方式提交数据的时候，会在 url 中添加 key=value 这样的字符串，
所以在 value 中是不允许有 '='，因此要对其进行编码;与此同时服务器接收到这些参数的时候，要进行解码，还原成原始的数据。
这个时候，这些辅助方法会很有用：
urllib.quote(string[, safe])：对字符串进行编码。参数 safe 指定了不需要编码的字符;
urllib.unquote(string) ：对字符串进行解码;
urllib.quote_plus(string [ , safe ] ) ：与 urllib.quote 类似，但这个方法用'+'来替换' '，而 quote 用' '来代替' '
urllib.unquote_plus(string ) ：对字符串进行解码;
urllib.urlencode(query[, doseq])：将dict或者包含两个元素的元组列表转换成url参数。例如 字典{'name': 'dark-bull', 'age': 200}将被转换为"name=dark-bull&age=200"
urllib.pathname2url(path)：将本地路径转换成 url 路径;
urllib.url2pathname(path)：将url路径转换成本地路径;
'''
import urllib
data = 'name = ~nowamagic+5'

data1 = urllib.quote(data)
print data1  # result: name = ~nowamagic+5
print urllib.unquote(data1)  # name = ~nowamagic+5

data2 = urllib.quote_plus(data)
print data2  # result: name+=+~nowamagic+5
print urllib.unquote_plus(data2)  # name = ~nowamagic+5

data3 = urllib.urlencode({'name': 'nowamagic-gonn', 'age': 200})
print data3  # result: age=200&name=nowamagic-gonn

data4 = urllib.pathname2url(r'd:/a/b/c/23.php')
print data4  # result: ///D://a/b/c/23.php
print urllib.url2pathname(data4)  # result: D:/a/b/c/23.php