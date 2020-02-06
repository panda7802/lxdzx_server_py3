# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import sys
import traceback

import os
from imp import reload

from django.http import HttpResponse, FileResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from scrapy import cmdline

from love.models import ZF
from tutils import t_url_tools
from tutils.t_global_data import TGlobalData

reload(sys)
# sys.setdefaultencoding('utf-8')


def love_index(request):
    t = get_template('love/love_index.html')
    items = [
        {'title': "第一次微信聊天", "desc": "我说：“您好”", "time": "2016-03-29 20:45:43"},
        {'title': "第一次见面", "desc": "你说：“你是姓潘吧”", "time": "2016-04-09 11:45:54"},
        {'title': "第一次看电影", "desc": "看得是愤怒的小鸟", "time": "2016-05-21 15:10:13"},
        {'title': "表白", "desc": "在天之都大厦门口", "time": "2016-05-21 20:15:02"},
        {'title': "牵手", "desc": "用得是过马路法则", "time": "2016-05-28 17:30:32"},
        {'title': "第一次过情人节", "desc": "在七夕", "time": "2016-08-09 18:30:43"},
        {'title': "第一次见家长", "desc": "我提心吊胆", "time": "2016-09-16 17:30:23"},
        {'title': "谈婚论嫁", "desc": "你说：“好的”", "time": "2016-11-27 18:10:43"},
        {'title': "第一次见我父母", "desc": "我手心冒汗", "time": "2017-01-30 11:30:56"},
        {'title': "第一次回你老家", "desc": "你爸说我很内向", "time": "2017-02-20 17:30:41"},
        {'title': "第一次旅游", "desc": "在杭州", "time": "2017-05-20 09:30:56"},
        {'title': "第一次双方高层会晤", "desc": "很顺利！", "time": "2017-11-18 11:50:32"},
        {'title': "买婚戒", "desc": "你说：“太大了，上班不方便”", "time": "2017-12-10 18:10:41"},
    ]
    show_data = {'res': items, 'len': items.__len__()}
    s = t.render(show_data)
    return HttpResponse(s)


def marry(request):
    t = get_template('love/marry.html')
    show_data = {}
    s = t.render(show_data)
    return HttpResponse(s)


def love_action(request, action):
    logging.debug(request.get_host() + " -- " + request.get_full_path())
    s = ""
    try:
        if action == "addzf":  # 增加祝福
            json_obj, session_res = t_url_tools.parse_url(request, is_check_session=False)
            name = json_obj['name']
            zf = json_obj['zf']
            ozf = ZF.objects.all().filter(name=name).first()
            if (None is ozf) or (name == ''):
                ozf = ZF()
                ozf.name = name
                ozf.zf = zf
                ozf.save()
            else:
                ozf.zf = zf
                ozf.save()
            s = t_url_tools.get_response_str({})
            return
        if action == "getZfByName":  # 通过姓名获取祝福
            json_obj, session_res = t_url_tools.parse_url(request, is_check_session=False)
            name = json_obj['name']
            zf = ZF.objects.all().filter(name=name).first()
            if None is zf:
                zfy = ""
            else:
                zfy = zf.zf
            s = t_url_tools.get_response_str({"zf": zfy})
            return
        if action == "getZfs":  # 获取所有祝福
            zfs = ZF.objects.all()
            res_zf = []
            for item in zfs:
                res_item = {}
                res_item['name'] = item.name
                res_item['zf'] = item.zf
                res_zf.append(res_item)
            s = t_url_tools.get_response_str(res_zf)
            return
        else:
            s = t_url_tools.get_response_str({}, success=False, msg="action不存在" + action)
            return
    except Exception as e:
        traceback.print_exc()
        logging.exception(e)
        s = t_url_tools.get_response_str({}, success=False, msg=action + " 异常",
                                         err_code=t_url_tools.ERR_CODE_EXCEPTION)
    finally:
        logging.debug(s)
        return HttpResponse(s)


# def tjbili(request, action):
#     # 开始爬虫
#     cmd = "cd " + TGlobalData.FILE_PATH + "../scrapy_test/  && scrapy crawl lxdzx_bili"
#     os.popen(cmd)
#
#     t = get_template('scrapy_data/lxdzx.html')
#     show_data = {}
#     s = t.render(show_data)
#     return HttpResponse(s)
#
#     # down_file = open(TGlobalData.STATIC_FILE_PATH + '/lxdzx_bili.csv', 'rb')
#     # response = FileResponse(down_file)
#     # response['Content-Type'] = 'application/octet-stream'
#     # response['Content-Disposition'] = 'attachment;filename="lxdzx_bili.csv"'
#     # return response
#     # # 下载
#     # t = get_template("files/lxdzx_bili.csv")
#     # s = t.render()
#     # return HttpResponse(s)
