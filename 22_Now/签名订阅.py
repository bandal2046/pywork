import time
import json
import requests
'''
sign签名的加密方法：
 （1 将所有的参数去除sign本身以及值为空的参数
 （2 将以上的的参数按照字母升序排序
 （3 将排序后的参数按照：参数1值1参数2值2……拼接成一个字符串
 （4 将秘钥拼接在字符串前+后
 （5 将以上字符全部换成小写，通过md5计算加密，得到sign值
 （6 将这个值传到服务器，服务器进行解码，识别这个值是否是我们要传的请求，如果是，则返回值。
'''

def jiami(apikey,body):
    # 1、去除值为空以及sign值的参数
    list=[]
    for i in body.items():
        # print(i) 遍历出来的是元组('username', 'test')。
        if i[0]!='sign' and i[1]!='':
            list.append("".join(i)) # 将遍历出来的元组进行拼接。
    #print('去除值为空以及sign值的参数后的list：%s'%list)

    # 2、 将以上的的参数按照字母升序排序
    list.sort() # 默认为升序排序,sort返回结果是一个list
    #print('参数按照字母升序排序的list：%s'%list)

    # 3、将排序后的参数按照：参数1值1参数2值2……拼接成一个字符串
    list_a="".join(list)
    #print('拼接后返回的新的字符串:%s' % list_a)

    # 4、 将秘钥拼接在字符串后面
    result = apikey + list_a + apikey
    #print('秘钥拼接在字符串后的结果：%s' % result)

    # 5、将以上字符全部换成小写，通过md5计算加密
    import hashlib
    def jiamind5(src):  # 函数嵌套一个函数
        m = hashlib.md5() # 创建一个对象
        m.update(result.encode('UTF-8'))
        return m.hexdigest()
        # print(sign)

    result1 = "lzgwoxNekHvpU17EA68wQFAOjCPkggX6DzATRappKey3834111cpCodeYUNDAformat jsonmailNo4315296484740methodkdzs.logistics.trace.subscribesign_methodmd5timestamp2021-06-16 16:18:59version1.0lzgwoxNekHvpU17EA68wQFAOjCPkggX6DzATR"
    sign = jiamind5(src='result1')

    print('sign:',sign.upper())
    # 得到sign签名后的新的body值
    body['sign'] = sign.upper() # 小写转大写后将sign值更新到body
    print('body:',body)

def requst(date):
    url = "https://gwtest.kuaidizs.cn/router" #测试环境
    #url = "https://gw.kuaidizs.cn/router" #正式环境
    print('data:',date)
    x = requests.post(url, data=date)
    print(x.text)

if __name__=='__main__':
    body = {
        "method": "kdzs.logistics.trace.get",#订阅
        "appKey": "5829972",
        "format": "json",
        "version": "1.0",
        "sign_method": "md5",
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "cpCode":"JD",
        "mailNo":"JDVC08941826756",#每次运单号需要改变，才能够订阅
    }
    #time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    sender = {
        "name":"张三",
        "tel":"13000000000"
    }
    senderAddress = {
        "province":"浙江省",
        "city":"杭州市",
        "district":"滨江区",
        "address":"江南大道"
    }
    sender["address"] = senderAddress
    #print(sender)

    receiver = {
        "name":"李四",
        "tel":"15000000000",
    }
    receiverAddress = {
        "province":"浙江省",
        "city":"宁波市",
        "district":"海曙区",
        "address":"望春街道气象路"
    }
    receiver["address"] = receiverAddress

    #print(json.dumps(sender))
    body["sender"] = json.dumps(sender)
    body["receiver"] = json.dumps(receiver)

    secret = "xYd84l2icLOApQoA1It825jC6JPDM988E2sU1"  # 秘钥，由开发提供


    jiami(secret, body)
    requst(body)