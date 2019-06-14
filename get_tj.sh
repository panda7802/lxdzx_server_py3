#!/bin/bash


sqlite3 /home/ubuntu/lxdzx_server/db.sqlite3  "SELECT
  b.title,
  Max(cast(a.play AS INT)),
  (Max(cast(a.play AS INT)) - min(cast(a.play AS INT))) AS addNum,
  datetime(b.created, 'unixepoch', 'localtime') as createTime
FROM get_web_data_videodetail a, get_web_data_videolist b
WHERE a.video_id = b.id and createTime>'2018-09-28'--and a.video_id in (1,2,3)
GROUP BY video_id
ORDER BY addNum
  DESC;"
