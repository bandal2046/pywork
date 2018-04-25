# encoding: UTF-8
import re


href = '"<link rel="stylesheet" href="https://file.xiaokeduo.com/system/phone/Shop/PublicMob/css/SpsBtn.css?114">""<link href="https://img.xiaokeduo.com/Templates/t1/css/head.css" rel="stylesheet">"'
src = '"<script type="text/javascript" src="https://file.xiaokeduo.com/system/phone/Scripts/WeixinShare.js?114"></script>"'

href_re = re.compile('href="(.*?)"',re.S)
src_re = re.compile('src="(.*?)"><',re.S)

items = re.findall(href_re,href)
items1 = re.findall(src_re,src)

print items[0]+"\n"+items[1]
print items1[0]

s = u'\u4f1a\u5458\u4e2d\u5fc3'
print s