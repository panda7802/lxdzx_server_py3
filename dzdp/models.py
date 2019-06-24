from django.db import models

from django.utils import timezone


# Create your models here.
class DzdpCity(models.Model):
    """
    大众点评城市
    """
    name = models.CharField('名称', default='', blank=True, max_length=1023)
    tag = models.CharField('标签', default='', blank=True, max_length=1023)
    province = models.CharField('省份', default='', blank=True, max_length=1023)
    country = models.CharField('国家', default='', blank=True, max_length=1023)
    is_need = models.BooleanField('是否需要获取', default=False)
    bak = models.CharField('备份', default='', blank=True, max_length=1023, )

    def __str__(self):
        return "%s : %s " % (self.name, str(self.is_need))


class DzdpType(models.Model):
    """
    大众点评类型
    """
    name = models.CharField('名称', default='', blank=True, max_length=1023)
    tag = models.CharField('标签', default='', blank=True, max_length=1023)
    is_need = models.BooleanField('是否需要获取', default=False)
    # curr_page = models.IntegerField('当前爬取的页面', default=0)
    # is_max_page = models.BooleanField('是否最大页面', default=False)
    parent_type = models.ForeignKey('self', null=True, on_delete=models.CASCADE, blank=True)
    bak = models.CharField('备份', default='', blank=True, max_length=1023)

    def __str__(self):
        return "%s : %s " % (self.name, str(self.is_need))


class DzdpCityType(models.Model):
    """
    大众点评城市类型关联
    """
    type = models.ForeignKey(DzdpType, on_delete=models.CASCADE)
    city = models.ForeignKey(DzdpCity, on_delete=models.CASCADE)
    curr_page = models.IntegerField('当前爬取的页面', default=0)
    is_max_page = models.BooleanField('是否最大页面', default=False)
    bak = models.CharField('备份', default='', blank=True, max_length=1023)

    def __str__(self):
        return "%s : %s %d , %s" % (self.city.name, str(self.type.name), self.curr_page, str(self.is_max_page))


class DzdpShop(models.Model):
    """
    大众点评商店
    """
    name = models.CharField('名称', default='', blank=True, max_length=1023)
    shop_id = models.CharField('商店号', default='', blank=True, max_length=1023)
    price = models.FloatField('价格', default=0)
    pic = models.IntegerField('图片', default=0)
    good = models.IntegerField('好评', default=0)
    common = models.IntegerField('中评', default=0)
    bad = models.IntegerField('差评', default=0)
    type = models.ForeignKey(DzdpType, on_delete=models.CASCADE)
    city = models.ForeignKey(DzdpCity, on_delete=models.CASCADE)
    phone = models.CharField('电话', max_length=64)
    url = models.CharField('url', default='', blank=True, max_length=1023)
    lon = models.FloatField('经度', default=0)
    lat = models.FloatField('纬度', default=0)
    lastGetTime = models.DateTimeField('上次爬取时间', default=timezone.now)
    bak = models.CharField('备份', default='', blank=True, max_length=1023)

    def __str__(self):
        return self.name + " , " + self.type.name
