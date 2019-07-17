# -*- coding: utf-8 -*-

import json
# Create your views here.
import logging
import urllib
from json import JSONDecoder

ERR_CODE_SESSION = 1
ERR_CODE_DATA = 2
ERR_CODE_PARM = 3
ERR_CODE_EXCEPTION = 4


def check_session(json_obj):
    # print("检测session")
    # TODO session校验
    return True


# 解析url
def parse_url(request, is_check_session=True):
    # logging.debug(request.get_full_path())
    parm = request.GET.get('parm')
    json_obj = JSONDecoder().decode(urllib.parse.unquote(parm))
    res_session = True
    if is_check_session:
        res_session = check_session(json_obj)
    return json_obj, res_session


def get_file_url(file_field):
    # 绝对路径
    abs_url = ""
    # 文件名称
    file_url = ""
    if len(str(file_field)) > 0:
        abs_url = urllib.unquote(file_field.url)
        file_url = abs_url.replace("\\", "/")
        file_url = file_url[file_url.rindex("/") + 1:]
    return abs_url, file_url


# 将数据字典的结果集返回成json
def get_response_str(response_data, success=True, msg="", err_code=0):
    if success:
        res = {'success': success, 'msg': msg}
    else:
        res = {'success': success, 'msg': msg, "errcode": err_code}
    if None != response_data:
        res['data'] = response_data
    else:
        res['data'] = {}
    s = json.dumps(res)
    s = eval("u" + "\'" + s + "\'")
    # logging.debug(s)
    return s


# 返回session异常失败
def get_session_err_res():
    s = get_response_str(None, msg="session失效，请重新登录", err_code=ERR_CODE_SESSION, success=False)
    return s
