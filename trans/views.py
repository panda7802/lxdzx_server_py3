# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import logging
import traceback
import urllib
# import urllib2
from json import JSONDecoder

from django.http import HttpResponse
import sys

from django.template.loader import get_template

# reload(sys)
# sys.setdefaultencoding('utf-8')


# 转发URL
def trans_url(request, url):
    s = ""
    try:
        # 解码两遍URL
        logging.debug(request.get_host() + " -- " + request.get_full_path())
        python_obj = JSONDecoder().decode(url)
        url = urllib.unquote(python_obj['url'])
        url = url.replace("tnbhh.cn", "lai4.com.cn")
        logging.debug("trans url : " + request.method + " , " + url)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6',
            'content-type': "application/json; charset=utf-8"}
        if request.method == 'GET':
            # s = urllib2.urlopen(url).read()
            req = urllib.request.Request(url=url, headers=headers)
            # res_data = urllib2.urlopen(req)
            # s = res_data.read()
        else:
            logging.debug(request.body)
            req = urllib.request.Request(url=url, data=request.body, headers=headers)
        res_data = urllib.request.urlopen(req)
        s = res_data.read()
    except Exception as e:
        # s = ":" + url
        s = "{\"code\":-1,\"msg\":\"转发URL异常" + url + "\"}"
        logging.exception(e)
        traceback.print_exc()
    finally:
        logging.debug("resp : " + str(s))
        return HttpResponse(s)


# 给孙子演示用的
def t_car_check(request, action):
    page = 'show4grandson/' + action + '.html'
    t = get_template(page)
    s = t.render()
    return HttpResponse(s)


# 年会
def t_nh(request, action):
    page = 'nh/' + action + '.html'
    t = get_template(page)
    s = t.render()
    return HttpResponse(s)
