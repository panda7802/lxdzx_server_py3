# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class ZF(models.Model):
    """
    祝福
    """
    name = models.CharField('姓名', max_length=128, default="", blank=False)  # 图片
    zf = models.CharField('祝福', max_length=128, default="", blank=False)  # 祝福
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段

    def __unicode__(self):
        return self.name + " : " + self.zf
