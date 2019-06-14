# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from django.db import models

# Create your models here.
from django.utils import timezone

from tutils.t_global_data import TGlobalData


class Tag(models.Model):
    """
    标签
    """
    pic_url = models.FileField('图片', upload_to=TGlobalData.STATIC_RECV_PATH, default="", blank=True)  # 图片
    title = models.CharField('标题', max_length=128, default="", blank=True)  # 标题
    desc = models.CharField('说明', max_length=256, default="", blank=True)  # 说明
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段
    parent_tag_id = models.ForeignKey('self', null=True, on_delete=models.CASCADE, blank=True)

    def __unicode__(self):
        return str(self.id) + "." + self.title


class Video(models.Model):
    """
    视频内容
    """
    title = models.CharField('标题', max_length=128, default="", blank=True)  # 标题
    pic_url = models.FileField('图片', upload_to=TGlobalData.STATIC_RECV_PATH, default="", blank=True)  # 图片
    video_url = models.CharField('视频地址', max_length=1024, default="", blank=True)  # 视频地址
    desc = models.CharField('描述', max_length=1024, default="", blank=True)  # 描述
    tags = models.ManyToManyField(Tag)  # 标签
    play_count = models.IntegerField('播放记录', default=0)  # 播放记录
    avg_point = models.FloatField('平均分', default=0)  # 平均分
    upload_time = models.DateTimeField('保存日期', default=timezone.now)  # 时间
    recommend = models.IntegerField('推荐', default=0)  # 推荐，分越高，越推荐
    cost_time = models.IntegerField('时长(秒)', default=0)  # 视频时长
    keywords = models.CharField('关键字(用英文状态下逗号分隔)', max_length=1024, default="", blank=True)  # 关键字
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段

    def __unicode__(self):
        return str(self.id) + "." + self.title


class People(models.Model):
    """
    人员信息
    """
    SEX_CHOICES = (
        (0, '未录入'),
        (1, '男'),
        (2, '女'),
    )
    name = models.CharField('姓名', max_length=64, default="", blank=True)  # 姓名
    pwd = models.CharField('密码', max_length=64, default="", blank=True)  # 密码
    sex = models.IntegerField('性别', choices=SEX_CHOICES, default=0)
    phone = models.CharField('手机号', max_length=64, default="", blank=True)  # 手机号
    wx_name = models.CharField('微信名称', max_length=128, default="", blank=True)  # 微信名称
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段

    def __unicode__(self):
        return self.wx_name


class Video_Record(models.Model):
    """
    播放记录
    """
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    people_id = models.ForeignKey(People, on_delete=models.CASCADE)
    watch_time = models.DateTimeField('观看时间', default=timezone.now)  # 时间
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段

    def __unicode__(self):
        try:
            s = str(self.watch_time)  # "Video_Record" , Video.objects.filter(id=self.video_id_id).first()
            # s = Video.objects.filter(id=self.video_id_id).first()
        except Exception as e:
            logging.error(str(e))
            s = "vr get db err"
        return s


class Video_Score(models.Model):
    """
    评分
    """
    GOOD_CHOICES = (
        (0, '未录入'),
        (1, '赞'),
        (2, 'low'),
    )
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    people_id = models.ForeignKey(People, on_delete=models.CASCADE)
    score = models.FloatField('评分', default=-1)  # 评分
    good = models.IntegerField('点赞', choices=GOOD_CHOICES, default=0)
    # comment = models.CharField('评论', max_length=1024, default="", blank=True)
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段

    def __unicode__(self):
        try:
            s = People.objects.filter(id=self.video_id).first()
        except Exception as e:
            logging.error(str(e))
            s = "get db err"
        return s


class People_Favorite(models.Model):
    """
    收藏
    """
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    people_id = models.ForeignKey(People, on_delete=models.CASCADE)
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段

    def __unicode__(self):
        try:
            s = self.video_id.title  # People.objects.filter(id=self.video_id).first()
        except Exception as e:
            logging.error(str(e))
            s = "get db err"
        return s


# 视频评论
class Video_Comment(models.Model):
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    people_id = models.ForeignKey(People, on_delete=models.CASCADE)
    comment = models.CharField('评论', max_length=1024, default="", blank=True)
    parent_comment_id = models.ForeignKey('self', null=True,on_delete=models.CASCADE, blank=True)
    comment_time = models.DateTimeField('评论时间', default=timezone.now)  # 时间
    is_top = models.IntegerField('置顶', default=0)
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段

    def __unicode__(self):
        try:
            s = self.video_id.title + " : " + self.comment
        except Exception as e:
            logging.error(str(e))
            s = "get db err"
        return s


# 新年寄语
class Xnjy(models.Model):
    people_id = models.ForeignKey(People,on_delete=models.CASCADE)
    school = models.CharField('学校', max_length=1024, default="", blank=True)
    jy = models.CharField('寄语', max_length=1024, default="", blank=True)
    lx_time = models.CharField('留学时间', max_length=64, default="", blank=True)
    comment_time = models.DateTimeField('留学时间(备用)', default=timezone.now)  # 时间
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段

    def __unicode__(self):
        try:
            s = self.people_id.name + " : " + self.school
        except Exception as e:
            logging.error(str(e))
            s = "get db err"
        return s

# TODO 人员级别


# TODO 视频分类等级

# TODO 视频等级
