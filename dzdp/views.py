# Create your views here.
import logging
import traceback

from django.http import HttpResponse

from dzdp.logic.action import get_types, get_types_view
from tutils import t_url_tools
from tutils.t_url_tools import ERR_CODE_PARM


def dzdp(request, action):
    """
       获取网络请求
       :param request:
       :param action:
       :return:
       """
    # 校验
    json_obj, session_res = t_url_tools.parse_url(request)
    s = ""

    try:
        if not session_res:
            s = t_url_tools.get_session_err_res()
        else:
            logging.debug("------%s " % action)
            logging.debug("------ " + str(action == "get_types"))
            if action == "get_types":
                s = get_types(json_obj)
                logging.debug(s)
            elif action == "get_types_view":
                s = get_types_view(json_obj)
            else:
                s = t_url_tools.get_response_str(None, msg=action + "不存在", err_code=ERR_CODE_PARM, success=False)
    except Exception as e:
        logging.error(e)
        traceback.print_exc()
        s = t_url_tools.get_response_str({}, success=False, msg=action + "异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        return HttpResponse(s)
