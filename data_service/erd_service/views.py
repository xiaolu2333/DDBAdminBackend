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
            {"name": "field1", "info": "date", "color": "#F7B84B", "figure": "Ellipse", 'icon': '主键'},
            {"name": "field2", "info": "boolean", "color": "#F25022", "figure": "Ellipse", 'icon': '外键'},
            {"name": "fieldThree", "info": "inet", "color": "#00BCF2", 'icon': '字段'},
        ],
        "loc": "0 0"
    }
    Record2 = {
        "key": "Record2",
        "fields": [
            {"name": "fieldA", "info": "integer", "color": "#FFB900", "figure": "Diamond", 'icon': '主键'},
            {"name": "fieldB", "info": "integer", "color": "#F25022", "figure": "Rectangle", 'icon': '字段'},
            {"name": "fieldC", "info": "char var", "color": "#7FBA00", "figure": "Diamond", 'icon': '字段'},
            {"name": "fieldD", "info": "char var", "color": "#00BCF2", "figure": "Rectangle", 'icon': '字段'}
        ],
        "loc": "280 0"
    }
    Record3 = {
        "key": "Record3",
        "fields": [
            {"name": "fieldA", "info": "char var", "color": "#FFB900", "figure": "Diamond", 'icon': '主键'},
            {"name": "fieldB", "info": "char var", "color": "#F25022", "figure": "Rectangle", 'icon': '字段'},
            {"name": "fieldD", "info": "real", "color": "#00BCF2", "figure": "Rectangle", 'icon': '字段'}
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
