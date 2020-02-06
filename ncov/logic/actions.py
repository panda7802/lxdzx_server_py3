import cursor
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
