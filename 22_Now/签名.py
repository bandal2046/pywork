import time
'''
2、 sign签名的加密方法：
 （1 将所有的参数去除sign本身以及值为空的参数
 （2 将以上的的参数按照字母升序排序
 （3 将排序后的参数按照：参数1值1参数2值2……拼接成一个字符串
 （4 将秘钥拼接在字符串后面
 （5 将以上字符全部换成小写，通过md5计算加密，得到sign值
 （6 将这个值传到服务器，服务器进行解码，识别这个值是否是我们要传的请求，如果是，则返回值。
'''
# 举个栗子：一个请求的body参数为以下：，提供的apikey为123456
# body = {
#     "username":"test",
#     "password":"123456",
#     "mail":"",
#     "sign":"签名后的值"
# }
#接下来使用python实现签名

print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

def jiami(apikey,body):
    # 1、去除值为空以及sign值的参数
    list=[]
    for i in body.items():
        # print(i) 遍历出来的是元组('username', 'test')。
        if i[0]!='sign' and i[1]!='':
            list.append("".join(i)) # 将遍历出来的元组进行拼接。
    print('去除值为空以及sign值的参数后的list：%s'%list)

    # 2、 将以上的的参数按照字母升序排序
    list.sort() # 默认为升序排序,sort返回结果是一个list
    print('参数按照字母升序排序的list：%s'%list)

    # 3、将排序后的参数按照：参数1值1参数2值2……拼接成一个字符串
    list_a="".join(list)
    print('拼接后返回的新的字符串:%s' % list_a)

    # 4、 将秘钥拼接在字符串后面
    result = list_a + apikey
    print('秘钥拼接在字符串后的结果：%s' % result)

    # 5、将以上字符全部换成小写，通过md5计算加密
    import hashlib
    def jiamind5(src):  # 函数嵌套一个函数
        m = hashlib.md5() # 创建一个对象
        m.update(result.encode('UTF-8'))
        return m.hexdigest()
        # print(sign)

    sign = jiamind5(src='result')
    print(sign)
    # 得到sign签名后的新的body值
    body['sign'] = sign  # 将sign值更新到body
    print(body)

if __name__=='__main__':
    apikey = "123456"  # 秘钥，由开发提供
    body = {  # 这是我们要传的参数
        "username": "test",
        "password": "123456",
        "mail": "",
        "sign": "签名后的值"
    }
    jiami(apikey, body)