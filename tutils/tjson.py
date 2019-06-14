# coding=utf-8

'''
@author: pangt
'''

from array import array
from json import scanner
import json
from json.decoder import JSONDecoder, WHITESPACE, errmsg, WHITESPACE_STR, \
    scanstring, JSONArray, _CONSTANTS
from json.encoder import JSONEncoder
from json.scanner import py_make_scanner
import sys
import traceback

from tutils import ttools
from tutils.t_demo_model import TDemoPerson, TDemoZAddr, TDemoToy
from tutils.ttools import TTools
from json.decoder import JSONDecoder
import django.utils.timezone


class TJsonTools(json.JSONEncoder):
    @classmethod
    def default(c, obj):
        js_encode = {}
        js_encode.update(obj.__dict__)
        return js_encode

    # json转到类
    @classmethod
    def tJsonDecode(c, js_encode, cls):
        if None is js_encode or None is cls:
            return None

        json_load = json.loads(js_encode)
        if None is json_load:
            return None
        if list == type(json_load):
            ins = TTools.tDicts2List(json_load, cls)
        elif dict == type(json_load):
            ins = TTools.tDict2Obj(json_load, cls)
        else:
            ins = None
        return ins

    @classmethod
    def tJsonEncode(c, obj):
        str = TJsonTools().encode(obj)
        return str.decode('unicode_escape')


if "__main__" == __name__:
    p = TDemoPerson('a啊', 'f', "1207", "a")
    p.addr = TDemoZAddr("1", "zfy")
    p.toys.append(TDemoToy('toy1', 1))
    p.toys.append(TDemoToy('toy2', 2))
    p1 = TDemoPerson('P2', 'f', "1208", "b")
    p1.addr = TDemoZAddr("2", "pmx")
    ps = []
    ps.append(p)
    ps.append(p1)

    print("---json 数组")
    js_encode = TJsonTools.tJsonEncode(ps)
    print("encode : ", js_encode)
    ins = TJsonTools.tJsonDecode(js_encode, TDemoPerson)
    print("bak    : ", TJsonTools.tJsonEncode(ps))
