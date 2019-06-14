# coding=utf-8

'''
基本工具
@author: pangt
'''
from tutils.t_log import TLog
import logging


class TTools:
    # 字典转到类
    @classmethod
    def tDict2Obj(c, d_dict, cls):

        if None is d_dict or None is cls:
            return None

        ins = cls()
        for k, v in d_dict.items():
            if None is v:
                continue

            old_v = getattr(ins, k)
            if type == type(old_v):
                continue
            elif list == type(old_v):
                sun_cls = getattr(cls, "_get_" + k + "_arr_type")
                tmp_list = TTools.tDicts2List(v, sun_cls)
                setattr(ins, k, tmp_list)
            elif dict == type(old_v):
                sun_cls = type(getattr(ins, k))
                sun_ins = TTools.tDict2Obj(v, sun_cls)
                setattr(ins, k, sun_ins)
            else:
                setattr(ins, k, v)

        return ins

    # 字典转列类
    @classmethod
    def tDicts2List(c, d_list, cls):

        if None is d_list or None is cls:
            return None

        resL = []
        for item in d_list:
            tmp_item = TTools.tDict2Obj(item, cls)
            resL.append(tmp_item)
        return resL

    @classmethod
    def str2Hex(c, str, char_code="UTF-8"):
        res = ""
        try:
            de = str.decode("UTF-8").encode(char_code)
            res = de.encode("hex").upper()
        except Exception as e:
            logging.exception(e)
        return res

    @classmethod
    def hex2Byte(c, hexStr, char_code="UTF-8"):
        """
        Hex 转byte
        """
        de = hexStr.decode("hex")
        res = de.decode(char_code).encode("UTF-8")
        return de


if "__main__" == __name__:
    str = "ABCD"
    sHex = TTools.str2Hex(str, char_code="ISO8859-1")
    print("原： " + sHex)
    strB = TTools.hex2Byte(sHex, char_code="ISO8859-1")
    print("回 ：" + strB)
