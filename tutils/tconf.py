# coding=utf8

'''
Created on 2016年12月20日

 测试环境的配置

@author: pangt
'''
from os.path import os

PRO_TYPE_DEV = "PRO_TYPE_DEV"
PRO_TYPE_PRD = "PRO_TYPE_PRD"
PRO_TYPE = PRO_TYPE_PRD


T_SUCCESS = 0
T_FAILED = 1
T_CHARCODE = 'utf-8'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
