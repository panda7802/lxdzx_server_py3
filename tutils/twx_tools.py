# -*- coding: utf-8 -*-

import time
import hashlib
import urllib
from json import JSONDecoder
import logging
from tutils import t_url_tools
# import urllib2
import urllib.request as urllib2


class WX_CONST:
    g_access_token = ""
    g_jsapi_ticket = ""
    g_last_get_at_time = 0


def getAccessToken(appId, appSecret):
    s = WX_CONST.g_access_token
    #   logging.debug(time.time())
    #  logging.debug(WX_CONST.g_last_get_at_time)
    if time.time() - WX_CONST.g_last_get_at_time < 1200:
        return s
    else:
        logging.debug("重新getAccessToken");

    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=" + appId + "&secret=" + appSecret
    # print("getAccessToken : " +  url)
    temp = urllib2.urlopen(url).read()
    try:
        logging.debug("temp : " + temp)
        json_obj = JSONDecoder().decode(temp)
        s = json_obj['access_token']
        WX_CONST.g_access_token = s
        WX_CONST.g_last_get_at_time = time.time()
    except Exception as e:
        logging.exception(e)
    #   s = "5_1eJMj69V1nkvNxQ43JucLyFPVT2enc8YpDYItW_vCK7OTCxAoU2XrL8DpHI3EMx5vP1syau9iLz08kQCAwCOeViEpqvKOmzJKm8RXha17sbaGttSs3NCNcZ2nPG005gpS8wldTxSBJpxSIaqWPQeABAIBC"
    return s


def get_jsapi_ticket(accessToken):
    s = WX_CONST.g_jsapi_ticket
    #    if time.time() - WX_CONST.g_last_get_at_time < 720:
    #        return s
    #    else:
    #        logging.debug("重新getAccessToken");
    url = "https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=" + accessToken + "&type=jsapi"
    logging.debug("get_jsapi_ticket : ", url)
    temp = urllib2.urlopen(url).read()
    try:
        #    logging.debug("temp : " + temp)
        json_obj = JSONDecoder().decode(temp)
        s = json_obj['ticket']
        WX_CONST.g_jsapi_ticket = s
    except Exception as e:
        logging.exception(e)
    return s


def get_sing(url, timeStamp, nonceStr, appId='wxaa3e9bee4d1d172d', appSecret='d0a7b8b491c15da6e3670da3d142495e'):
    # def get_sing(url, timeStamp, nonceStr, appId='wx29db0e2cd630f115', appSecret='8893b55244bd1c64e25c45fde5973cda'):
    access_token = getAccessToken(appId, appSecret)
    jsapi_ticket = get_jsapi_ticket(access_token)
    #   logging.debug("accessToken : " + access_token)
    #  logging.debug("jsapi_ticket : " + jsapi_ticket)
    sign_value = "jsapi_ticket=" + jsapi_ticket + "&noncestr=" + nonceStr + "&timestamp=" + timeStamp + "&url=" + url;
    # logging.debug("微信JS-SDK权限验证的签名串：" + sign_value)
    # 这个签名.主要是给加载微信js使用.别和上面的搞混了.
    signature = hashlib.sha1(sign_value).hexdigest()
    # logging.debug("微信JS-SDK权限验证的签名：" + signature)
    s = signature
    return s
