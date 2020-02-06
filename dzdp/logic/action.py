#coding=utf-8

import logging
from json import JSONDecoder

from django.template.loader import get_template

from dzdp.models import DzdpType, DzdpShop
from tutils import t_url_tools


def get_types(json_obj):
    """
    获取类型列表
    :param json_obj:
    :return:
    """
    if json_obj is None:
        parent_type_id = json_obj['pid']
    else:
        parent_type_id = 1
    # parent_type_id = json_obj['pid']
    all_types = DzdpType.objects.filter(parent_type=parent_type_id)
    if all_types.__len__() <= 0:
        s = t_url_tools.get_response_str({}, success=False, msg="类型不存在", err_code=t_url_tools.ERR_CODE_DATA)
        return s

    res = []
    for item in all_types:
        res.append({"id": item.id, "name": item.name})

    s = t_url_tools.get_response_str(res)
    return s


def get_types_view(json_obj):
    """
    获取类型列表页面
    :param json_obj:
    :return:
    """
    logging.debug(json_obj)
    if None is json_obj:
        parent_type_id = json_obj['pid']
    else:
        parent_type_id = 1
    data = JSONDecoder().decode(get_types(json_obj))['data']
    type_info = DzdpType.objects.filter(id=parent_type_id).first()
    res = {'res': data, 'len': data.__len__(), "type_name": type_info.name}
    # show_data = t_url_tools.get_response_str(res)
    t = get_template('dzdp/types.html')
    s = t.render(res)
    return s


def get_phb(json_obj):
    logging.debug(json_obj)
    type_id = json_obj['tid']
    page = json_obj['page']
    evaluation = json_obj['evaluation']
    min_price = json_obj['min_price']
    max_price = json_obj['max_price']
    # 每页多少条
    page_count = 10
    sql = 'select a.* from v_dzdpshop a, dzdp_dzdpshoptype b,dzdp_dzdptype c ' \
          ' where c.id = \'%s\' and a.id = b.shop_id  and b.type_id = c.id ' \
          ' and a.evaluation > %d' \
          ' and a.price >=  %d ' \
          ' and a.price <= % d ' \
          ' order by a.hpl desc limit %d,%d' \
          % (type_id, evaluation, min_price, max_price, page * page_count, page_count)
    logging.debug(sql)
    shops = DzdpShop.objects.raw(sql)
    #logging.debug(shops)
    #if shops.__len__() <= 0:
    #if len(shops) <= 0:
    #    s = t_url_tools.get_response_str({}, success=False, msg="商店不存在", err_code=t_url_tools.ERR_CODE_DATA)
    #    return s

    res = []
    for shop in shops:
        res.append({"name": shop.name, "price": shop.price, "evaluation": shop.evaluation, "phone": shop.phone,
                    "pic": shop.pic, "good": shop.good, "common": shop.common,
                    "bad": shop.bad, "hpl": shop.hpl, "url": shop.url})

        s = t_url_tools.get_response_str(res)
    return s


def get_phb_view(json_obj):
    type_id = json_obj['tid']
    type_info = DzdpType.objects.filter(id=type_id).first()
    type_name = ""
    if type_info is not None:
        type_name = type_info.name
    # data = JSONDecoder().decode(get_phb(json_obj))['data']
    # res = {'res': data, 'len': data.__len__(), "type_name": type_name}
    res = {"type_name": type_name}

    # show_data = t_url_tools.get_response_str(res)
    t = get_template('dzdp/shops.html')
    s = t.render(res)
    return s
