import logging
import traceback

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ncov.logic.actions import get_confirmed, get_pro_his, get_single_pro_his, get_pros
from tutils import t_url_tools
from tutils.t_url_tools import ERR_CODE_PARM


def get_ncov(request, action):
    """
    确诊人数
    :param request:
    :param action:
    :return:
    """
    logging.debug(request.get_full_path())

    # 无json
    try:
        if action == "get_pros":
            s = get_pros()
            return HttpResponse(s)
    except Exception as e:
        logging.error(e)
        traceback.print_exc()
        s = t_url_tools.get_response_str({}, success=False, msg=action + "异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
        return HttpResponse(s)


    # 校验
    json_obj, session_res = t_url_tools.parse_url(request, False)
    s = ""

    try:
        if not session_res:
            s = t_url_tools.get_session_err_res()
        else:
            if action == "get_confirmed":
                s = get_confirmed(json_obj)
            elif action == "get_pro_his":
                s = get_pro_his(json_obj)
            elif action == "get_single_pro_his":
                s = get_single_pro_his(json_obj)
            else:
                s = t_url_tools.get_response_str(None, msg=action + "不存在", err_code=ERR_CODE_PARM, success=False)
    except Exception as e:
        logging.error(e)
        traceback.print_exc()
        s = t_url_tools.get_response_str({}, success=False, msg=action + "异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        return HttpResponse(s)
