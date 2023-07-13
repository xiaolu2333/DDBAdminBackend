import json

from django.http import JsonResponse


def get_erd_data(request):
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
        "schema": "public",
        "key": "Record1",
        "fields": [
            {"name": "field1", "info": "date", "color": "#F7B84B", "figure": "Ellipse", 'icon': '主键'},
            {"name": "field2", "info": "boolean", "color": "#F25022", "figure": "Ellipse", 'icon': '外键'},
            {"name": "fieldThree", "info": "inet", "color": "#00BCF2", 'icon': '外键'},
        ],
        "loc": "0 0"
    }
    Record2 = {
        "schema": "public",
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
        "schema": "public",
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
        {"from": "Record1", "fromPort": "fieldThree", "to": "Record2", "toPort": "fieldA"},
        {"from": "Record1", "fromPort": "field2", "to": "Record3", "toPort": "fieldD"},
        {"from": "Record4", "fromPort": "fieRecord4-1111111111111111", "to": "Record3", "toPort": "fieldB"}
    ]
    data['linkDataArray'] = link_data

    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': data,
    })


def get_tree_data(request):
    """
    获取树形数据
    :param request:
    :return:
    """
    data = [
        {
            "id": 1,
            "server_group_name": "tsg1",
            "server_name": "",
            "db_name": "",
            "node_type": "server_group",
            "name": "tsg1",
            "code": "tsg1",
            "parent_code": "",
            "label": "tsg1",
            "children": [
                {
                    "id": 2,
                    "server_group_name": "tsg1",
                    "server_name": "ts1",
                    "db_name": "",
                    "node_type": "server",
                    "name": "ts1",
                    "code": "ts1",
                    "parent_code": "tsg1",
                    "label": "ts1",
                    "children": [
                        {
                            "id": 3,
                            "server_group_name": "tsg1",
                            "server_name": "ts1",
                            "db_name": "tdb1",
                            "node_type": "db",
                            "name": "tdb1",
                            "code": "tdb1",
                            "parent_code": "ts1",
                            "label": "tdb1",
                            "children": [
                                {
                                    "id": 6,
                                    "server_group_name": "tsg1",
                                    "server_name": "ts1",
                                    "db_name": "tdb1",
                                    "node_type": "table",
                                    "name": "tt1",
                                    "code": "tt1",
                                    "parent_code": "tdb1",
                                    "label": "tt1",
                                    "children": [],
                                    "data": {
                                        "schema": "public",
                                        "key": "tdb1",
                                        "fields": [
                                            {"name": "field1", "info": "date", "color": "#F7B84B", "figure": "Ellipse",
                                             'icon': '主键'},
                                            {"name": "field2", "info": "boolean", "color": "#F25022",
                                             "figure": "Ellipse",
                                             'icon': '外键'},
                                            {"name": "fieldThree", "info": "inet", "color": "#00BCF2", 'icon': '字段'},
                                        ],
                                        "loc": "0 0"
                                    }
                                },
                                {
                                    "id": 7,
                                    "server_group_name": "tsg1",
                                    "server_name": "ts1",
                                    "db_name": "tdb1",
                                    "node_type": "table",
                                    "name": "tt2",
                                    "code": "tt2",
                                    "parent_code": "tdb1",
                                    "label": "tt2",
                                    "children": [],
                                    "data": {
                                        "schema": "public",
                                        "key": "Record2",
                                        "fields": [
                                            {"name": "fieldA", "info": "integer", "color": "#FFB900",
                                             "figure": "Diamond", 'icon': '主键'},
                                            {"name": "fieldB", "info": "integer", "color": "#F25022",
                                             "figure": "Rectangle", 'icon': '字段'},
                                            {"name": "fieldC", "info": "char var", "color": "#7FBA00",
                                             "figure": "Diamond", 'icon': '字段'},
                                            {"name": "fieldD", "info": "char var", "color": "#00BCF2",
                                             "figure": "Rectangle", 'icon': '字段'}
                                        ],
                                        "loc": "280 0"
                                    }
                                },
                                {
                                    "id": 8,
                                    "server_group_name": "tsg1",
                                    "server_name": "ts1",
                                    "db_name": "tdb1",
                                    "node_type": "table",
                                    "name": "tt3",
                                    "code": "tt3",
                                    "parent_code": "tdb1",
                                    "label": "tt3",
                                    "children": [],
                                    "data": {
                                        "schema": "public",
                                        "key": "Record3",
                                        "fields": [
                                            {"name": "fieldA", "info": "char var", "color": "#FFB900",
                                             "figure": "Diamond", 'icon': '主键'},
                                            {"name": "fieldB", "info": "char var", "color": "#F25022",
                                             "figure": "Rectangle", 'icon': '字段'},
                                            {"name": "fieldD", "info": "real", "color": "#00BCF2",
                                             "figure": "Rectangle", 'icon': '字段'}
                                        ],
                                        "loc": "280 0"
                                    }
                                }
                            ]
                        },
                        {
                            "id": 4,
                            "server_group_name": "tsg1",
                            "server_name": "ts1",
                            "db_name": "tdb2",
                            "node_type": "db",
                            "name": "tdb2",
                            "code": "tdb2",
                            "parent_code": "ts1",
                            "label": "tdb2",
                            "children": [],

                        },
                        {
                            "id": 5,
                            "server_group_name": "tsg1",
                            "server_name": "ts1",
                            "db_name": "tdb3",
                            "node_type": "db",
                            "name": "tdb3",
                            "code": "tdb3",
                            "parent_code": "ts1",
                            "label": "tdb3",
                            "children": [],
                        }
                    ]
                }
            ]
        }
    ]
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': data,
    })
