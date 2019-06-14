# coding=utf8

"""
Created on 20161215

@author: pangt
"""

import logging
from os.path import os
from sys import platform

from tutils.t_log import TLog


class TGlobalData:
    def __init__(self):
        pass

    plam = "unix"
    FILE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/files/"
    STATIC_FILE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/static/files/"
    # STATIC_RECV_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/static/files/recv"
    STATIC_RECV_PATH = "../static/files/recv"

    @staticmethod
    def init():
        """
        初始化
        """
        logging.info("-------Global_data init")
        TGlobalData.plam = platform
        logging.info("-------FILE_PATH " + TGlobalData.FILE_PATH)
        logging.info("-------Global_data init over")

    @staticmethod
    def is_test_pro():
        """
        是否为测试程序
        """
        res = (TGlobalData.PRO_TYPE == TGlobalData.PRO_TYPE_DEV)
        return res
