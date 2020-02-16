from django.db import connection
from django.template.loader import get_template


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
      and a.pid not in ('42')
    order by a.pid, a.s_date
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

    s_dates = []
    print(datas)
    res = []
    last_pro_name = ""
    res_item = {'pro_name': '', "confirmedNum": [], "curesNum": [],
                "deathsNum": [], "s_dates": []}
    # 新增确诊
    confirmed_num = []
    # 新增治愈
    curesNum = []
    # 新增死亡
    deathsNum = []
    s_dates = []
    for item in datas:
        print(item)
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
    # show_data = {'type': '新增数', "pro_names": pro_names, "confirmedNum": confirmed_num, "curesNum": curesNum,
    #              "deathsNum": deathsNum, "s_dates": s_dates}
    show_data = {'type': '新增数', 'res': res, "s_dates": s_dates}
    print(show_data)
    t = get_template('ncov/get_add.html')
    s = t.render(show_data)
    return s
