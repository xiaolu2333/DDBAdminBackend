import json

from django.http import JsonResponse


def index(request):
    """
    获取ERD信息
    :param request:
    :return:
    """
    data = {
        'nodeDataArray': [],
        'linkDataArray': []
    }

    Record1 = {
        "key": "Record1",
        "fields": [
            {"name": "field1", "info": "", "color": "#F7B84B", "figure": "Ellipse"},
            {"name": "field2", "info": "the second one", "color": "#F25022", "figure": "Ellipse"},
            {"name": "fieldThree", "info": "3rd", "color": "#00BCF2"}
        ],
        "loc": "0 0"
    }
    Record2 = {
        "key": "Record2",
        "fields": [
            {"name": "fieldA", "info": "", "color": "#FFB900", "figure": "Diamond"},
            {"name": "fieldB", "info": "", "color": "#F25022", "figure": "Rectangle"},
            {"name": "fieldC", "info": "", "color": "#7FBA00", "figure": "Diamond"},
            {"name": "fieldD", "info": "fourth", "color": "#00BCF2", "figure": "Rectangle"}
        ],
        "loc": "280 0"
    }
    Record3 = {
        "key": "Record3",
        "fields": [
            {"name": "fieldA", "info": "", "color": "#FFB900", "figure": "Diamond"},
            {"name": "fieldB", "info": "", "color": "#F25022", "figure": "Rectangle"},
            {"name": "fieldD", "info": "fourth", "color": "#00BCF2", "figure": "Rectangle"}
        ],
        "loc": "280 0"
    }
    data['nodeDataArray'] = [Record1, Record2, Record3]

    link_data = [
        {"from": "Record1", "fromPort": "field1", "to": "Record2", "toPort": "fieldA"},
        {"from": "Record1", "fromPort": "field2", "to": "Record3", "toPort": "fieldD"},
    ]
    data['linkDataArray'] = link_data

    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': data,
    })
