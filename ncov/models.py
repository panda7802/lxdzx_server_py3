import logging

from django.db import models


# Create your models here.
class ZoneInfo(models.Model):
    """
    区域信息
    """
    name = models.CharField('名称', max_length=1023)
    mid = models.CharField('本平台序号', max_length=64, default='0')
    pid = models.CharField('父节点序号', max_length=64, default='0')
    upd_time = models.CharField('数据时间', max_length=128, default='2020-02-01')
    desc = models.CharField('描述', max_length=1023)
    bak = models.CharField('备份', max_length=1023)

    def __unicode__(self):
        try:
            s = self.name
        except Exception as e:
            logging.error(str(e))
            s = "get db err"
        return s


class CnovInfo(models.Model):
    """
    Cnov信息
    """
    cid = models.CharField('区域序号', max_length=64, default='0')
    confirmedNum = models.IntegerField('确诊人数', default=0)
    curesNum = models.IntegerField('治愈人数', default=0)
    deathsNum = models.IntegerField('死亡人数', default=0)
    maybeNum = models.IntegerField('疑似', default=0)
    bak = models.CharField('备份', max_length=1023)

    def __unicode__(self):
        try:
            s = self.name
        except Exception as e:
            logging.error(str(e))
            s = "get db err"
        return s
