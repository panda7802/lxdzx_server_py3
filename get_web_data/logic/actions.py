# coding=utf-8


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import os
import traceback

import datetime

from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template

from get_web_data.models import PlatformStatistics, VideoNameInfos, VideoDetail
from tutils import t_url_tools

# 1:点击率
TJ_TYPE_CLICK = 1
# 2:粉丝数
TJ_TYPE_FANS = 2
# 3:关注数
TJ_TYPE_FOLLOW = 3
# 4:阅读数
TJ_TYPE_READ = 4

# 1:收藏
TJ_TYPE_FAVOURITE = 1
# 2:播放
TJ_TYPE_PLAY = 2
# 3:评论
TJ_TYPE_COMMENT = 3


def get_dgtj(json_obj):
    s = "[]"
    # json_obj, session_res = t_url_tools.parse_url(request, is_check_session=False)
    # if not session_res:
    #     s = t_url_tools.get_session_err_res()
    #     return
    svid = json_obj['vid']
    # svid = "2,3"
    vids = svid.split(",")
    response_data = []
    s = ""
    for vid in vids:
        item = PlatformStatistics.objects.filter(vid_id=vid).first()
        # res_item = {'name': item.vid.name}
        res_item = {'name': filter(lambda t: t[0] == item.vid.platform, VideoNameInfos.PLATFORM_SIDES)[0][1],
                    'clicks': item.clicks, 'fans': item.fans, 'follows': item.follows, 'reads': item.reads}
        response_data.append(res_item)
        # s = "平台：",res_item['name'],"点击量：" ,res_item['clicks'] ,""
        sitem = "平台 ： %s\t\t  , 点击量：%s ，粉丝数：%s，关注数:%s ，阅读数:%s  <Br/>" % \
                (res_item['name'], res_item['clicks'], res_item['fans'], res_item['follows'], res_item['reads'])
        s = s + sitem
    return s


def get_dgtj_echart(json_obj):
    s = "{}"
    # vid = json_obj['vid']
    svid = json_obj['vid']
    '''
       统计类型
       1:点击率
       2:粉丝数
       3:关注数
       4:阅读数
      '''
    tj_type = json_obj['type']

    s_start_time = json_obj['start_time']
    s_end_time = json_obj['end_time']
    vids = svid.split(",")

    # 目标平台
    obj_platforms = VideoNameInfos.objects.filter(get_data=0, id__in=vids)
    obj_platforms_names = []
    for item in obj_platforms:
        obj_platforms_names.append(
            filter(lambda platform_ids: platform_ids[0] == item.platform, VideoNameInfos.PLATFORM_SIDES)[0][1])

    # 点击量,关注数等
    start_time = datetime.datetime.strptime(s_start_time, "%Y%m%d%H%M%S")
    end_time = datetime.datetime.strptime(s_end_time, "%Y%m%d%H%M%S")
    datas = []  # 总数据
    x_times = []
    # 时间轴
    # s_times = ""
    get_time_over = False
    for index, vid in enumerate(vids):
        tmp_time = start_time
        last_num = -1
        single_data_item = {"name": obj_platforms_names[index]}
        platform_items = []  # 平台点击率、关注之类的列表

        while tmp_time <= end_time:
            x_times_item = {}
            # 时间横轴
            if not get_time_over:
                x_times_item['x_date'] = tmp_time.strftime("%m-%d")
                x_times_item['x_time'] = tmp_time.strftime("%H:%M")
                x_times.append(x_times_item)

            item = PlatformStatistics.objects.filter(get_time__gte=tmp_time, vid_id=vid).order_by("get_time").first()
            if None is item:
                break

            # 数据
            if TJ_TYPE_CLICK == tj_type:
                curr_num = item.clicks
            elif TJ_TYPE_FANS == tj_type:
                curr_num = item.fans
            elif TJ_TYPE_FOLLOW == tj_type:
                curr_num = item.follows
            elif TJ_TYPE_READ == tj_type:
                curr_num = item.reads
            else:
                curr_num = 0

            # 和上次做对比
            if last_num < 0:
                last_num = curr_num

            if curr_num > 0:  # 如果数据异常，取上一条数据
                min_num = curr_num - last_num
                last_num = curr_num
            else:
                min_num = 0
            # if last_num >= 0:
            #     min_num = item.clicks - last_num
            # print str(tmp_time) + " , " + str(item.clicks) + " , " + str(min_num)
            # data_item = {"num": last_num}
            data_item = {"num": min_num}
            platform_items.append(data_item)

            # 一小时为单位
            tmp_time = tmp_time + datetime.timedelta(days=1)

        single_data_item['platform_items'] = platform_items
        datas.append(single_data_item)
        get_time_over = True

    # 显示
    t = get_template('get_web_data/get_fans_add.html')

    # 数据
    if TJ_TYPE_CLICK == tj_type:
        s_type = "点击率"
    elif TJ_TYPE_FANS == tj_type:
        s_type = "粉丝数"
    elif TJ_TYPE_FOLLOW == tj_type:
        s_type = "关注数"
    elif TJ_TYPE_READ == tj_type:
        s_type = "阅读数"
    else:
        s_type = "未知类型"

    show_data = {'tj_type': s_type, 'obj_platforms_names': obj_platforms_names, "x_times": x_times, "datas": datas,
                 "get_time_over": get_time_over}
    # print show_data

    s = t.render(show_data)
    return s


# noinspection SqlDialectInspection
def get_bili_video_tj_echart(json_obj):
    s = "{}"
    svid = json_obj['vid']
    tj_type = json_obj['type']
    s_start_time = json_obj['start_time']
    s_end_time = json_obj['end_time']
    # vids = svid.split(",")
    count = json_obj['count']
    is_new = json_obj['is_new']
    if is_new:
        s_is_new = "create_time"
    else:
        s_is_new = "a.get_time"

    video_names = []
    video_ids = []
    # -- and a.get_time > datetime('%s')
    # 获取前10位的视频编号和名称
    s_start_time1 = s_start_time[:4] + "-" + s_start_time[4:6] + "-" + s_start_time[6:8] + " " \
                    + s_start_time[8:10] + ":" + s_start_time[10:12] + ":" + s_start_time[12:14]
    s_end_time1 = s_end_time[:4] + "-" + s_end_time[4:6] + "-" + s_end_time[6:8] + " " \
                  + s_end_time[8:10] + ":" + s_end_time[10:12] + ":" + s_end_time[12:14]
    sql = """ SELECT
  a.video_id,
  b.title,
  datetime(b.created, 'unixepoch', 'localtime')         AS create_time,
  min(a.get_time) as min_time,
  min(cast(a.play AS INT)) as min_num,
  (case when min('%s') > datetime(b.created, 'unixepoch', 'localtime')  then min(cast(a.play AS INT)) else 0 end) AS min_num1,
  Max(cast(a.play AS INT)) as max_num,
  (Max(cast(a.play AS INT)) -  ((case when min('%s') > datetime(b.created, 'unixepoch', 'localtime')  then min(cast(a.play AS INT)) else 0 end)) ) AS addNum
FROM get_web_data_videodetail a, get_web_data_videolist b
WHERE a.video_id = b.id
  and %s > datetime('%s')
  and a.get_time < datetime('%s')
GROUP BY video_id
ORDER BY addNum DESC
LIMIT %s;
    """ % (s_start_time1, s_start_time1, s_is_new, s_start_time1, s_end_time1, count)
    print(sql)

    cursor = connection.cursor()
    cursor.execute(sql)
    for item in cursor.fetchall():
        video_names.append(item[1])
        video_ids.append(item[0])

    # print video_ids
    # print video_names

    # # 目标平台
    # obj_platforms = VideoNameInfos.objects.filter(get_data=0, id__in=vids)
    # video_names = []
    # for item in obj_platforms:
    #     video_names.append(
    #         filter(lambda platform_ids: platform_ids[0] == item.platform, VideoNameInfos.PLATFORM_SIDES)[0][1])

    # 点击量,关注数等
    start_time = datetime.datetime.strptime(s_start_time, "%Y%m%d%H%M%S")
    end_time = datetime.datetime.strptime(s_end_time, "%Y%m%d%H%M%S")
    datas = []  # 总数据
    x_times = []
    # 时间轴
    # s_times = ""
    get_time_over = False
    for index, video_id in enumerate(video_ids):
        tmp_time = start_time
        single_data_item = {"name": video_names[index]}
        platform_items = []  # 平台点击率、关注之类的列表

        # print video_names[index]

        while tmp_time <= end_time:
            x_times_item = {}
            # 时间横轴
            if not get_time_over:
                x_times_item['x_date'] = tmp_time.strftime("%m-%d")
                x_times_item['x_time'] = tmp_time.strftime("%H:%M")
                x_times.append(x_times_item)

            item = VideoDetail.objects.filter(get_time__gte=tmp_time, video_id=video_id).order_by("get_time").first()
            if None is item:
                break

            # 数据
            if TJ_TYPE_FAVOURITE == tj_type:
                curr_num = int(item.favorites)
            elif TJ_TYPE_PLAY == tj_type:
                curr_num = int(item.play)
            elif TJ_TYPE_COMMENT == tj_type:
                curr_num = int(item.comment)
            else:
                curr_num = 0

            data_item = {"num": curr_num}
            platform_items.append(data_item)

            # 一天为单位
            # tmp_time = tmp_time + datetime.timedelta(days=1)
            tmp_time = tmp_time + datetime.timedelta(hours=12)

        single_data_item['platform_items'] = platform_items
        datas.append(single_data_item)
        get_time_over = True

    # 显示
    t = get_template('get_web_data/get_video_add.html')

    if TJ_TYPE_FAVOURITE == tj_type:
        s_type = "收藏"
    elif TJ_TYPE_PLAY == tj_type:
        s_type = "播放"
    elif TJ_TYPE_COMMENT == tj_type:
        s_type = "评论"
    else:
        s_type = "未知类型"

    show_data = {'tj_type': s_type, 'video_names': video_names, "x_times": x_times, "datas": datas,
                 "get_time_over": get_time_over}
    # print show_data

    s = t.render(show_data)
    return s


def get_trt_ticket():
    os.system("python3 /home/pangt/res_dir/get_tickets.py")
    f = open("/home/pangt/res_dir/res.txt")
    f.seek(0)
    res = f.read()
    # res = res.replace("\n", "<br/>")
    # print(res)

    t = get_template('get_web_data/get_trt_ticket.html')
    show_data = {'res': res}
    s = t.render(show_data)
    return s
