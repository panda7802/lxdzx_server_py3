# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
import traceback

from django.http import HttpResponse, StreamingHttpResponse

import video_manager.logic.people_manager
import video_manager.logic.play_ctrl
import video_manager.logic.video_ctrl
from tutils.t_global_data import TGlobalData
from video_manager.logic import video_ctrl, people_manager, play_ctrl, show_res, xnjy
from video_manager.logic.xnjy import *


# reload(sys)
# sys.setdefaultencoding('utf-8')


# Create your views here.
def t_index(request):
    t = get_template('index.html')
    s = t.render()
    return HttpResponse(s)


def t_wx_web(request):
    t = get_template('MP_verify_e3MyIfTydXwqxprn.txt')
    s = t.render()
    return HttpResponse(s)


def t_wx_web_self(request):
    t = get_template('MP_verify_rhm9oyjPc3nd0dVB.txt')
    s = t.render()
    return HttpResponse(s)


def wx_token(request):
    try:
        # s = "panguotian"
        # return HttpResponse(s)
        # data = web.input()
        # if len(data) == 0:
        #     return "hello, this is handle view"
        print(request.get_full_path())
        print(request.GET.get('signature'))
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
        echostr = request.GET.get('echostr')
        token = "panguotian"  # 请按照公众平台官网\基本配置中信息填写
        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print("handle/GET func: hashcode, signature: ", hashcode, signature)
        if hashcode == signature:
            return HttpResponse(echostr)  # echostr
        else:
            return ""
    except Exception as Argument:
        return Argument
        # s = request.GET.get('signature')
        # return HttpResponse(s)


def t_test_amaze(request):
    t = get_template('test_amaze.html')
    s = t.render()
    return HttpResponse(s)


def t_test_layui(request, action):
    page = 'test_layui/test_layui_' + action + '.html'
    print(page)
    t = get_template(page)
    s = t.render()
    return HttpResponse(s)


def t_test_jquery(request, action):
    page = 'jquery/' + action + '.html'
    print(page)
    t = get_template(page)
    s = t.render()
    return HttpResponse(s)


def t_test_bootstrap(request, action):
    page = 'bootstrap/' + action + '.html'
    print(page)
    t = get_template(page)
    s = t.render()
    return HttpResponse(s)


def notice(request):
    t = get_template('notice.html')
    s = t.render()
    return HttpResponse(s)


# Create your views here.
def t_home_page(request):
    t = get_template('cpJC9PX6Nu.txt')
    s = t.render()
    return HttpResponse(s)


# 获取文件
def get_file(request, file_name):
    def file_iterator(file_name, chunk_size=512):
        print("file_name : ", file_name)
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    the_file_name = TGlobalData.STATIC_RECV_PATH + file_name
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response


#
# # 获取标签
# def get_tags(request):
#     return logic.video_ctrl.get_tags(request)
#
#
# # 通过标签获取视频
# def get_video_by_tag(request):
#     return logic.video_ctrl.get_video_by_tag(request)
#
#
# # 通过关键字搜索视频
# def get_video_by_gjz(request):
#     return logic.video_ctrl.get_video_by_gjz(request)
#
#
# 登录
def login(request):
    return video_manager.logic.people_manager.login(request)


#
#
# # 播放视频
# def play_video(request):
#     return logic.play_ctrl.play_video(request)
#
#
# # 根据id获取视频
# def get_video_by_id(request):
#     return logic.video_ctrl.get_video_by_id(request)
#
#
# # 排序视频
# def get_videos_order(request):
#     return logic.video_ctrl.get_videos_order(request)
#
#
# # 增加播放记录
# def add_play_record(request):
#     return logic.play_ctrl.add_play_record(request)
#
#
# def get_people_play_record(request):
#     return logic.play_ctrl.get_people_play_record(request)
#
#
# def do_my_fav(request):
#     """
#     删减我的收藏
#     :param request:
#     :return:
#     """
#     return logic.play_ctrl.do_my_fav(request)
#
#
# def get_people_fav(request):
#     """
#     获取是否收藏
#     :param request:
#     :return:
#     """
#     return logic.play_ctrl.get_people_fav(request)
#
#
# # TODO 获取欢迎页面URL
#
# # TODO 记录播放进度
#
# # TODO 统计视频播放量（UI），包括每个视频的播放时间
# def statistics_videos(request):
#     return logic.play_ctrl.statistics_videos(request)


def xnjyshare1(request):
    s = xnjy_share(request)
    return HttpResponse(s)


def lxdzx(request, action):
    print(request.get_full_path())
    logging.debug(request.get_host() + " -- " + request.get_full_path())
    s = ""
    try:
        if action == "MP_verify_e3MyIfTydXwqxprn.txt":
            t = get_template('MP_verify_e3MyIfTydXwqxprn.txt')
            logging.debug(t)
            s = t.render()
            return
        elif action == "xnjy_index":
            s = xnjy_index(request)
            return s
        elif action == "xnjy_index1":
            s = xnjy_index1(request)
            return s
        elif action == "xnjy_gzh":
            s = xnjy_gzh(request)
            return s
        elif action == "xnjy_input":
            s = xnjy_input(request)
            return s
        elif action == "xnjy_show":
            s = xnjy_show(request)
            return s
        elif action == "xnjyshare":
            s = xnjy_share(request)
            return s

        # 校验
        json_obj, session_res = t_url_tools.parse_url(request)
        if not session_res:
            s = t_url_tools.get_session_err_res()
            return

        if action == "get_tags":
            s = video_ctrl.get_tags(json_obj)
        elif action == "get_video_by_tag":
            s = video_ctrl.get_video_by_tag(json_obj)
        elif action == "get_video_by_gjz":
            s = video_ctrl.get_video_by_gjz(json_obj)
        elif action == "login":
            s = people_manager.login(json_obj)
        elif action == "play_video":
            s = play_ctrl.play_video(json_obj)
        elif action == "get_videos_oder":
            s = video_ctrl.get_videos_order(json_obj)
        elif action == "get_video_by_id":
            s = video_ctrl.get_video_by_id(json_obj)
        elif action == "add_play_record":
            s = play_ctrl.add_play_record(json_obj)
        elif action == "get_people_play_record":
            s = play_ctrl.get_people_play_record(json_obj)
        elif action == "do_my_fav":
            s = play_ctrl.do_my_fav(json_obj)
        elif action == "get_people_fav":
            s = play_ctrl.get_people_fav(json_obj)
        elif action == "xnjy_save_xnjy":
            s = xnjy.xnjy_save_xnjy(json_obj)
        elif action == "xnjy_get_xnjy":
            s = xnjy.xnjy_get_xnjy(json_obj)
        elif action == "xnjy_gzh":
            s = xnjy.xnjy_gzh(request)
        else:
            s = t_url_tools.get_response_str({}, success=False, msg="no " + action,
                                             err_code=t_url_tools.ERR_CODE_EXCEPTION)
    except Exception as e:
        traceback.print_exc()
        logging.exception(e)
        s = t_url_tools.get_response_str({}, success=False, msg=action + " 异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        logging.debug(s)
        return HttpResponse(s)


def xnjyshare(request, action):
    s = xnjy_share(request)
    return HttpResponse(s)


def lxdzx_show(request, action):
    logging.debug(request.get_full_path())
    try:
        if action == "statistics_videos":
            s = show_res.statistics_videos(request)
        elif action == "notice":
            s = notice(request)
        elif action == "about":
            s = t_index(request)
        elif action == "xnjy_index":
            s = xnjy_index(request)
        elif action == "xnjy_index1":
            s = xnjy_index1(request)
        elif action == "xnjy_gzh":
            s = xnjy_gzh(request)
        elif action == "xnjy_input":
            s = xnjy_input(request)
        elif action == "xnjy_show":
            s = xnjy_show(request)
        elif action == "xnjyshare":
            s = xnjy_share(request)
        elif action == "MP_verify_e3MyIfTydXwqxprn.txt":
            t = get_template('MP_verify_e3MyIfTydXwqxprn.txt')
            s = t.render()
        else:
            s = "url 不存在:", action
    except Exception as e:
        traceback.print_exc()
        logging.exception(e)
        s = t_url_tools.get_response_str({}, success=False, msg=action + " 错误",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        return HttpResponse(s)


def add_video_comment(request):
    return video_manager.logic.play_ctrl.add_video_comment(request)


def del_video_comment(request):
    return video_manager.logic.play_ctrl.del_video_comment(request)


def get_video_comment(request):
    return video_manager.logic.play_ctrl.get_video_comment(request)
