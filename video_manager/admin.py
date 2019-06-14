# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
#
from video_manager.models import *

admin.site.register(Tag)
admin.site.register(Video)
admin.site.register(People)
admin.site.register(Xnjy)
# admin.site.register(Video_Record)
admin.site.register(Video_Score)
admin.site.register(Video_Comment)

