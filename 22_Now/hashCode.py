# -*- coding: utf-8 -*-
'''
Created on 2019-08-22 14:06
---------
@summary: python方法实现java的hash算法
---------
@author: yongxinYang
'''


class GetHashCode:
    def convert_n_bytes(self, n, b):
        bits = b * 8
        return (n + 2 ** (bits - 1)) % 2 ** bits - 2 ** (bits - 1)

    def convert_4_bytes(self, n):
        return self.convert_n_bytes(n, 4)

    @classmethod
    def getHashCode(cls, s):
        '''
        实现java的hash算法
        :param s:
        :return:
        '''
        h = 0
        n = len(s)
        for i, c in enumerate(s):
            h = h + ord(c) * 31 ** (n - 1 - i)
        return cls().convert_4_bytes(h)

    @classmethod
    def get_base_key(self, str):
        str2 = ''
        c = '65535'
        hash_num = self.getHashCode(str)
        if hash_num == -459336179:
            if str == "ACCOUNT":
                c = 0
                return "553a1fd4c7a4d23b2c05bb7b1438f978"

        elif hash_num == 75556:
            if str == "LOG":
                c = 1
                return "3666f801f6d69a75022ca5fc684fb312"
        elif hash_num == 76641:
            if str == "MSG":
                c = 2
                return "21c196b35b19963b6b934685f140b95b"

        elif hash_num == 2337004:
            if str == "LIVE":
                c = 3
                return "abb81dd045c9c995b988108e0024ed0c"
        elif hash_num == 2544374:
            if str == "SHOP":
                c = 4
                return "62dc47996c1dd6b23cecc9e29788b62b"
        elif hash_num == 67081473:
            if str == "FORUM":
                c = 5
                return "c5905376760d7a2cca10d5f684348f5c"
        elif hash_num == 25175104:
            if str == "STAT_CUBE":
                c = 6
                return "da2bdee10cb433a32d8aeaef114b6b6e"
        elif hash_num == 2288:
            if str == "GW":
                c = 7
                return "557ee139b69ca29910eb0c3d3057261f"
        else:
            return str2


if __name__ == "__main__":
    hashCode = GetHashCode.getHashCode("557050977527508")
    print((hashCode & 0x7FFFFFFF) % 1001)

    hashCode2 = GetHashCode.get_base_key("557050977527508")
    print(hashCode2)