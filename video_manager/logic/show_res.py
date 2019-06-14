# -*- coding: utf-8 -*-

# 视频管理

from django.db.models import Q, Count
from django.http import HttpResponse
from django.template.loader import get_template

from tutils import t_url_tools
from video_manager.logic.play_ctrl import Video_Statistics_Model
from video_manager.models import Tag, Video, Video_Record


# 视频播放量
def statistics_videos(request):
    """
    播放量
    :param request:
    :return:
    """
    recs = Video_Record.objects.values_list('video_id').annotate(Count('video_id'))

    response_data = []
    for item in recs:
        video = Video.objects.filter(id=item[0]).first()
        count = item[1]
        video.play_count = count
        video.save()
        res_item = Video_Statistics_Model(video.title, count, video)  # {'video': video, "count": count}
        response_data.append(res_item)
    t = get_template('statistics.html')
    s = t.render({'res': response_data})
    return s
