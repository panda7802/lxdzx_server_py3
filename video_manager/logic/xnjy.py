# -*- coding: utf-8 -*-

# 视频管理
import hashlib
import json

import time
import urllib
from json import JSONDecoder

# import urllib2
import urllib.request as urllib2
from tutils import twx_tools
from django.template.loader import get_template
import logging

from tutils import t_url_tools
from video_manager.models import People, Xnjy


def xnjy_save_xnjy(json_obj):
    # 增加微信名称
    nick_name = json_obj['nick_name']
    people = People.objects.filter(name=nick_name)
    #   people_count = people.__len__()
    people_count = 0
    if people_count <= 0:
        people = People()
        people.name = nick_name
        people.save()
        #       people = People.objects.filter(name=nick_name).first()
    else:
        people = people.first()

    xnjy = Xnjy.objects.filter(people_id=people).first()
    if xnjy is None:
        xnjy = Xnjy()
    xnjy.school = json_obj['school']
    xnjy.jy = json_obj['jy']
    xnjy.lx_time = json_obj['lx_time']
    xnjy.people_id = people
    xnjy.save()
    # res = {"id": people_id}
    s = t_url_tools.get_response_str({})
    return s


def xnjy_get_xnjy(json_obj):
    # 增加微信名称
    nick_name = json_obj['nick_name']
    people = People.objects.filter(name=nick_name).first()
    res_item = {'school': ""}
    res_item['jy'] = ""
    res_item['lx_time'] = ""
    if people is not None:
        xnjy = Xnjy.objects.filter(people_id=people).first()
        if xnjy is not None:
            res_item = {'school': xnjy.school}
            res_item['jy'] = xnjy.jy
            res_item['lx_time'] = xnjy.lx_time
    # res = {"id": people_id}
    s = t_url_tools.get_response_str({'res': res_item})
    return s


def xnjy_index1(request):
    """
    新年寄语
    :param request:
    :return:
    """
    ui_type = 1
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
        ui_type = int(json_obj['ui_type'])
    except Exception as e:
        pass

    if 1 == ui_type:
        ui_type = "yellow"
    else:
        ui_type = "blue"

    t = get_template('xnjy/index1.html')
    s = t.render({'ui_type': ui_type})
    return s


def xnjy_index(request):
    """
    新年寄语
    :param request:
    :return:
    """
    ui_type = 1
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
        ui_type = int(json_obj['ui_type'])
    except Exception as e:
        pass

    if 1 == ui_type:
        ui_type = "yellow"
    else:
        ui_type = "blue"

    t = get_template('xnjy/index.html')
    s = t.render({'ui_type': ui_type})
    return s


def xnjy_input(request):
    """
    新年寄语 录入
    :param request:
    :return:
    """

    ui_type = 1
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
        ui_type = int(json_obj['ui_type'])
    except Exception as e:
        pass

    if 1 == ui_type:
        ui_type = "yellow"
    else:
        ui_type = "blue"

    wx_name = ""
    try:
        wx_name = json_obj['wx_name']
    except Exception as e:
        pass

    xnjy = Xnjy.objects.filter(people_id__name=wx_name).first()
    if xnjy is None:
        xnjy = Xnjy()
    t = get_template('xnjy/input.html')
    s = t.render({'xnjy': xnjy, 'ui_type': ui_type})
    return s


def xnjy_show(request):
    """
    新年寄语
    :param request:
    :return:
    """

    ui_type = 1
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
        ui_type = int(json_obj['ui_type'])
    except Exception as e:
        pass

    if 1 == ui_type:
        ui_type = "yellow"
    else:
        ui_type = "blue"
    nick_name = ""
    try:
        nick_name = json_obj['nick_name']
    except Exception as e:
        pass

    xnjy = Xnjy.objects.filter(people_id__name=nick_name).first()
    if xnjy is None:
        print(xnjy)
        xnjy = Xnjy()
    # t = get_template('xnjy/input.html')
    # s = t.render({'xnjy': xnjy, 'ui_type': ui_type})

    t = get_template('xnjy/show.html')
    s = t.render({'xnjy': xnjy, 'ui_type': ui_type})
    return s


def xnjy_gzh(request):
    ui_type = 0
    try:
        json_obj, session_res = t_url_tools.parse_url(request)
        ui_type = int(json_obj['ui_type'])
    except Exception as e:
        pass

    # url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxaa3e9bee4d1d172d&redirect_uri=https%3a%2f%2fwww.pandafly.cn%2flxdzx_show%2fxnjy_gzh&response_type=code&scope=snsapi_base&state=123#wechat_redirect"
    # res = urllib2.urlopen(url).read()
    #   logging.debug("xnjy_gzh : " + res)

    # s = t.render({'xnjy': xnjy, 'ui_type': ui_type})
    #   s = "panguotian"
    code = request.GET.get('code')
    appid = "wxaa3e9bee4d1d172d"
    secret = "d0a7b8b491c15da6e3670da3d142495e"
    # 获取openid
    url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=" + appid + "&secret=" + secret + "&code=" + code + "&grant_type=authorization_code"
    res = urllib2.urlopen(url).read()
    logging.debug(res)
    json_obj = JSONDecoder().decode(urllib.unquote(res))
    open_id = json_obj['openid']
    logging.debug("open_id : " + open_id)

    # 获取access_token
    # url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid="+appid+"&secret="+secret+"&code="+code+"&grant_type=authorization_code"
    # res = urllib2.urlopen(url).read()
    # logging.debug(res)
    # json_obj = JSONDecoder().decode(urllib.unquote(res))
    access_token = json_obj['access_token']  # twx_tools.getAccessToken(appid,secret)
    # 获取用户信息
    url = "https://api.weixin.qq.com/sns/userinfo?access_token=" + access_token + "&openid=" + open_id + "&lang=zh_CN"
    res = urllib2.urlopen(url).read()
    logging.debug(res)
    s = res

    return s


def xnjy_share(request):
    logging.debug(request.get_full_path())
    timeStamp = "1414587458"  # str(time.time())
    nonceStr = "panguotian"
    url = request.GET.get("url")
    url = str(url)
    url = url.split('&_=')[0]
    # url = urllib.unquote(url)
    logging.debug("---url : " + url)
    url = url.replace("%7B", "{").replace("%7D", "}")
    #   urls = url.split('?')
    #   if urls.__len__() > 0:
    #       url_parm = urls[1]
    #       url_parm = urllib.quote(url_parm)
    #       url_parm = url_parm.replace("%3D%7B","={").replace("%7D","}")
    #       url_parm = url_parm.replace("\"","%22")
    #       url = urls[0] + '?' + url_parm
    logging.debug("parse url " + url)
    res = {}
    res['timeStamp'] = timeStamp
    res['nonceStr'] = nonceStr
    res['url'] = url
    res['signature'] = twx_tools.get_sing(url, timeStamp, nonceStr)
    s = json.dumps(res)
    return s
