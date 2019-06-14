# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.db import models
from django.utils import timezone


# Create your models here.
class VideoNameInfos(models.Model):
    """
       平台分析
       """
    PLATFORM_SIDES = (
        (1, 'B站'),
        (2, '今日头条'),
    )
    IS_GET_DATA = (
        (0, '是'),
        (1, '否'),
    )
    platform = models.IntegerField('平台', choices=PLATFORM_SIDES, default=0)
    name = models.CharField('名称', max_length=1023)
    mid = models.CharField('本平台序号', max_length=1023, default=0)
    get_data = models.IntegerField('是否爬虫', choices=IS_GET_DATA, default=0)
    desc = models.CharField('描述', max_length=1023)

    def __unicode__(self):
        try:
            s = filter(lambda item: item[0] == self.platform, self.PLATFORM_SIDES)[0][1] + " -- " + self.name
        except Exception as e:
            logging.error(str(e))
            s = "get db err"
        return s


class PlatformStatistics(models.Model):
    vid = models.ForeignKey(VideoNameInfos,on_delete=models.CASCADE)
    clicks = models.BigIntegerField('总点击量', default=0)
    fans = models.BigIntegerField('总粉丝数', default=0)
    follows = models.BigIntegerField('关注数', default=0)
    reads = models.BigIntegerField('阅读数', default=0)
    get_time = models.DateTimeField('保存日期', default=timezone.now)
    bak = models.CharField('备注', max_length=1023)

    def __unicode__(self):
        try:
            s = filter(lambda item: item[0] == self.vid.platform, VideoNameInfos.PLATFORM_SIDES)[0][1] \
                + "-" + self.vid.name + "\t\t\t\t" + self.get_time.strftime("%Y-%m-%d %H:%M:%S")
        except Exception as e:
            logging.error(str(e))
            s = "get db err"
        return s


class VideoList(models.Model):
    """
    视频列表
    """
    title = models.CharField(max_length=255)  # 标题
    subtitle = models.CharField(max_length=255)  # 子标题
    comment = models.CharField(max_length=255)  # 评论数
    created = models.CharField(max_length=255)  # 创建时间
    video_review = models.CharField(max_length=255)  # 弹幕数
    favorites = models.CharField(max_length=255)  # 收藏量
    length = models.CharField(max_length=255)  # 长度
    play = models.CharField(max_length=255)  # 播放量
    author = models.CharField(max_length=255)  # 作者
    review = models.CharField(max_length=255)
    typeid = models.CharField(max_length=255)  # 类型
    pic = models.CharField(max_length=255)  # 图片
    description = models.CharField(max_length=255)  # 描述
    aid = models.CharField(max_length=255)  # 详细信息id
    mid = models.CharField(max_length=255)  # 当前id
    copyright = models.CharField(max_length=255)  # 版权
    hide_click = models.CharField(max_length=255)  # 不可点击
    #
    gl_title = models.CharField(max_length=255)  # 关联标题
    gl_url = models.CharField(max_length=255)  # 关联url

    def __unicode__(self):
        try:
            s = self.title
        except Exception as e:
            logging.error(str(e))
            s = "get db err"
        return s


class VideoDetail(models.Model):
    """
    视频详情
    """
    video = models.ForeignKey(VideoList,on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)  # 评论数
    video_review = models.CharField(max_length=255)  # 弹幕数
    favorites = models.CharField(max_length=255)  # 收藏量
    play = models.CharField(max_length=255)  # 播放量
    get_time = models.DateTimeField('保存日期', default=timezone.now)
    bak = models.CharField('备注内容', max_length=1023)

    def __unicode__(self):
        try:
            s = self.video.title + " : " + str(self.play)
        except Exception as e:
            logging.error(str(e))
            s = "get db err"
        return s
