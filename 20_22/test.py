# coding=utf-8
import re
'''
a = [1,2,3]
b = ['a','b','c']
c = []
c.append(a)
c.append(b)
d = c[1]
print d[1]
'''
content = u"晚上下班到家，看到儿子站在可怜巴巴的样子：“儿子，咋的了？”<br/>老婆：“你儿子考试不好，我想啊，要教育好孩子，作为家长必须言传身教，所以我们分工一下，我言传，你身教。”<br/>老公：“这怎么分工？”<br/>老婆一指搓衣板：“跪那去，这小子，连跪都跪不好，给他示范一下。”<br/>老公：……"
a = content.replace("<br/>","\n")
print a
'''
pattern = re.compile('(.*?)<br/>(.*?)<br/>(.*?)<br/>(.*?)<br/>(.*?).',re.S)
items = re.findall(pattern,content)
for item in items:
    print item[0],item[1],item[2],item[3],item[4]
'''
inputStr = "hello 111 world 111"
print inputStr
replacedStr = inputStr.replace("111", "222")
print replacedStr