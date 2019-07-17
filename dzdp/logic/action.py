from json import JSONDecoder

from django.template.loader import get_template

from dzdp.models import DzdpType
from tutils import t_url_tools


def get_types(json_obj):
    parent_type_id = json_obj['pid']
    all_types = DzdpType.objects.filter(parent_type=parent_type_id)
    if all_types.__len__() <= 0:
        s = t_url_tools.get_response_str({}, success=False, msg="视频不存在", err_code=t_url_tools.ERR_CODE_DATA)
        return s

    res = []
    for item in all_types:
        res.append({"name": item.name})

    s = t_url_tools.get_response_str(res)
    return s


def get_types_view(json_obj):
    parent_type_id = json_obj['pid']
    data = JSONDecoder().decode(get_types(json_obj))['data']
    type_info = DzdpType.objects.filter(id=parent_type_id).first()
    res = {'res': data, 'len': data.__len__(), "type_name": type_info.name}
    # show_data = t_url_tools.get_response_str(res)
    t = get_template('dzdp/types.html')
    s = t.render(res)
    return s
