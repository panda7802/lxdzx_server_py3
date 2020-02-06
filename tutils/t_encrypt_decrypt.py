# coding=utf-8

'''
加解密
Created on 2016年12月19日


@author: pangt
'''

import md5
import hashlib
from tutils.ttools import TTools

class TEncryptDecrypt :
    
    @classmethod
    def md5_str(cls,str):
        m2 = hashlib.md5()   
        m2.update(str)
        res = m2.hexdigest()    
        return res
    
if "__main__" == __name__ :
    s_md5 = TEncryptDecrypt.md5_str("hello1234")