# coding=utf-8

import logging

from get_web_data.logic.actions import *
from tutils import t_url_tools
from tutils.t_url_tools import ERR_CODE_PARM


def get_web_data(request, action):
    """
    获取网络请求
    :param request:
    :param action:
    :return:
    """
    logging.debug(request.get_full_path())
    # 校验
    json_obj, session_res = t_url_tools.parse_url(request)
    s = ""

    try:
        if not session_res:
            s = t_url_tools.get_session_err_res()
        else:
            if action == "get_dgtj":
                s = get_dgtj(json_obj)
            elif action == "get_dgtj_echart":
                s = get_dgtj_echart(json_obj)
            elif action == "get_bili_video_tj_echart":
                s = get_bili_video_tj_echart(json_obj)
            else:
                s = t_url_tools.get_response_str(None, msg=action + "不存在", err_code=ERR_CODE_PARM, success=False)
    except Exception as e:
        logging.error(e)
        traceback.print_exc()
        s = t_url_tools.get_response_str({}, success=False, msg=action + "异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        return HttpResponse(s)
