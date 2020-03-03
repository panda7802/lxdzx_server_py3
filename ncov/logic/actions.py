from django.db import connection
from django.template.loader import get_template

from ncov.models import ZoneInfo


def get_confirmed(json_obj):
    max = json_obj['limit']
    sql = "select c.name as '省',\
       b.name as '市',\
       a.confirmedNum as '确诊人数',\
       a.curesNum as '治愈人数',\
       a.deathsNum as '死亡人数',\
        ROUND(ifnull((a.curesNum+0.0)/a.confirmedNum,0)*100 ,2) as '治愈率',\
        ROUND(ifnull((a.deathsNum+0.0)/a.confirmedNum,0)*100 ,2) as '死亡率'\
        from ncov_cnovinfo a,ncov_zoneinfo b ,ncov_zoneinfo c\
        where a.cid = b.mid\
        and b.pid = c.mid\
        order by 确诊人数 desc \
        limit %d" % max
    print(sql)
    cursor_data = connection.cursor()
    cursor_data.execute(sql)
    # raw = cursor_data.fetchone()  # 返回结果行游标直读向前，读取一条
    datas = cursor_data.fetchall()  # 读取所有
    if None is datas:
        return "EMPTY"

    # 省名
    # pro_names = []
    # 市名
    city_names = []
    # 确诊数
    confirmed_num = []
    print(datas)
    for item in datas:
        print(item)
        # pro_names.append(item[0])
        city_names.append(item[1])
        confirmed_num.append(item[2])
    show_data = {'type': '确诊数', "city_names": city_names, "confirmedNum": confirmed_num}
    print(show_data)
    t = get_template('ncov/get_confirmed.html')
    s = t.render(show_data)
    return s


def get_pro_his(json_obj):
    """
    获取省份历史
    :param json_obj:
    :return:
    """
    max = json_obj['limit']
    # pros = "'32','31'"
    pros = ""
    for i in range(10, 99):
        # 去掉湖北
        if i == 42:
            continue
        pros = "%s'%d'," % (pros, i)
    pros = pros[:len(pros) - 1]
    print(pros)
    sql = '''
        select c.name,
           (a.confirmedNum - b.confirmedNum) as '新增确诊',
           (a.curesNum - b.curesNum) as '新增治愈',
           (a.deathsNum - b.deathsNum) as '新增死亡',
           a.s_date,
           a.*
    from ncov_cnovhisinfo a,
         ncov_cnovhisinfo b,
         ncov_zoneinfo c
    where date(a.s_date, 'start of day', '-1 days') = b.s_date
      and a.pid = b.pid
      and a.pid = c.mid
      and a.pid in (%s)
      and b.s_date >= (select min(s_date) from ncov_cnovhisinfo where pid in (%s) group by pid  order by s_date desc limit 1)
    order by a.pid, a.s_date
    ''' % (pros, pros)
    print(sql)
    cursor_data = connection.cursor()
    cursor_data.execute(sql)
    # raw = cursor_data.fetchone()  # 返回结果行游标直读向前，读取一条
    datas = cursor_data.fetchall()  # 读取所有
    if None is datas:
        return "EMPTY"

    # 市名
    pro_names = []

    s_dates = []
    print(datas)
    res = []
    last_pro_name = ""
    res_item = {'pro_name': '', "confirmedNum": [], "curesNum": [],
                "deathsNum": [], "s_dates": []}
    s_dates = []
    for item in datas:
        # print(item)
        if not s_dates.__contains__(item[4]):
            s_dates.append(item[4])
        # 发现新的省则加一项
        if last_pro_name != item[0]:
            res_item = {'pro_name': item[0], "confirmedNum": [], "curesNum": [],
                        "deathsNum": [], "s_dates": []}
            res.append(res_item)

        pro_names.append(item[0])
        res_item['confirmedNum'].append(item[1])
        res_item['curesNum'].append(item[2])
        res_item['deathsNum'].append(item[3])
        res_item['s_dates'].append(item[4])
        last_pro_name = item[0]
    show_data = {'type': '新增数', 'res': res, "s_dates": s_dates}
    print(show_data)
    t = get_template('ncov/get_add.html')
    s = t.render(show_data)
    return s


def get_single_pro_his(json_obj):
    """
    获取单个省份历史变化
    :param json_obj:
    :return:
    """
    pros = json_obj['pro']
    # pros = "'32','31'"
    sql = '''
        select c.name,
           (a.confirmedNum - b.confirmedNum) as '新增确诊',
           (a.curesNum - b.curesNum) as '新增治愈',
           (a.deathsNum - b.deathsNum) as '新增死亡',
           a.s_date,
           a.*
    from ncov_cnovhisinfo a,
         ncov_cnovhisinfo b,
         ncov_zoneinfo c
    where date(a.s_date, 'start of day', '-1 days') = b.s_date
      and a.pid = b.pid
      and a.pid = c.mid
      and a.pid in (%s)
      and b.s_date >= (select min(s_date) from ncov_cnovhisinfo where pid in (%s) group by pid  order by s_date desc limit 1)
    order by a.pid, a.s_date
    ''' % (pros, pros)
    print(sql)
    cursor_data = connection.cursor()
    cursor_data.execute(sql)
    # raw = cursor_data.fetchone()  # 返回结果行游标直读向前，读取一条
    datas = cursor_data.fetchall()  # 读取所有
    if None is datas:
        return "EMPTY"

    # 市名
    pro_names = []

    s_dates = []
    print(datas)
    res = []
    last_pro_name = ""
    res_item = {'pro_name': '', "confirmedNum": [], "curesNum": [],
                "deathsNum": [], "s_dates": []}
    s_dates = []
    for item in datas:
        # print(item)
        if not s_dates.__contains__(item[4]):
            s_dates.append(item[4])
        # 发现新的省则加一项
        if last_pro_name != item[0]:
            res_item = {'pro_name': item[0], "confirmedNum": [], "curesNum": [],
                        "deathsNum": [], "s_dates": []}
            res.append(res_item)

        pro_names.append(item[0])
        res_item['confirmedNum'].append(item[1])
        res_item['curesNum'].append(item[2])
        res_item['deathsNum'].append(item[3])
        res_item['s_dates'].append(item[4])
        last_pro_name = item[0]
    show_data = {'type': '新增数', 'res': res, "s_dates": s_dates}
    print(show_data)
    t = get_template('ncov/get_single_add.html')
    s = t.render(show_data)
    return s


def get_pros():
    """
        获取单个省份历史变化
        :param json_obj:
        :return:
        """
    pros = ZoneInfo.objects.filter(pid=0).order_by('mid')
    show_data = {'pros': pros}
    # for item in pros:
    #     print(item.mid)
    t = get_template('ncov/pros.html')
    s = t.render(show_data)
    return s


def get_tj():
    """
    排行榜
    :param json_obj:
    :return:
    """
    sql = '''
    select distinct
       c.name                                                                        as '上级地名',
       a.name                                                                        as '地名',
       a.people                                                                      as '人口',
       b.confirmedNum                                                                as '确诊',
       b.curesNum                                                                    as '治愈',
       b.deathsNum                                                                   as '死亡',
       CAST(round(ifnull((b.confirmedNum + 0.0) / a.people, 0) * 10000, 5) AS FLoat) as '确诊率(万分之)',
       CAST(round(ifnull((b.curesNum + 0.0) / b.confirmedNum, 0) * 100, 2) AS FLoat)  as '治愈率(%)',
       CAST(round(ifnull((b.deathsNum + 0.0) / b.confirmedNum, 0) * 100, 2) AS FLoat) as '死亡率(%)',
       a.name in ('南京','天门')     as '关注'
from ncov_zoneinfo a,
     ncov_cnovinfo b,
     ncov_zoneinfo c
where a.mid = b.cid
  and a.pid = c.mid
        '''
    print(sql)
    cursor_data = connection.cursor()
    cursor_data.execute(sql)
    # raw = cursor_data.fetchone()  # 返回结果行游标直读向前，读取一条
    datas = cursor_data.fetchall()  # 读取所有
    if None is datas:
        return "EMPTY"

    # 市名
    pro_names = []

    # print(datas)
    res = []
    for item in datas:
        res_item = {'p_name': item[0], "zone_name": [], "confirmedNum": [], "curesNum": [], "deathsNum": [],
                    "confirmedRate": [], "curesRate": [], "deathsRate": [], 'zone_name': item[1],
                    'confirmedNum': item[3], 'curesNum': item[4], 'deathsNum': item[5], 'confirmedRate': item[6],
                    'curesRate': item[7], 'deathsRate': item[8]}
        res.append(res_item)
        # print(res_item)
    show_data = {'type': '统计', 'res': res}
    print(show_data)
    t = get_template('ncov/get_tj.html')
    s = t.render(show_data)
    return s
