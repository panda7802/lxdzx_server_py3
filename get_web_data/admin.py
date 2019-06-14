# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from get_web_data.models import VideoList, PlatformStatistics, VideoNameInfos, VideoDetail

admin.site.register(VideoList)
admin.site.register(VideoNameInfos)
admin.site.register(PlatformStatistics)
admin.site.register(VideoDetail)
