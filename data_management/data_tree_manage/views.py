import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

from data_management.data_tree_manage.models import DataTreeNode
from utils.formatTransformer.request_and_response import camel_to_snake, snake_to_camel


def index(request):
    """
    数据树管理首页
    :param request:
    :return:
    """
    nodes = DataTreeNode.objects.all()
    # 找出服务器组节点
    server_group_nodes = nodes.filter(node_type='server_group')
    # 根据nodes中数据的parent_code构建树形结构
    list = []
    # 为nodes中数据添加children属性
    for i in nodes:
        list.append({
            'oid': i.oid,
            'node_type': i.node_type,
            'name': i.name,
            'parent_oid': i.parent_oid,
            'children': []
        })

    # tree_data = build_tree(list)

    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': list,
    })


def get_tree_node(request):
    """
    获取树节点
    :param request:
    :return:
    """
    # 获取请求参数
    oid = request.GET.get('oid', None)

    # # 返回 响应状态码 500，响应消息 error，响应数据 请求参数错误
    # if oid is None:
    #     return JsonResponse({
    #         'msg': '请求参数错误',
    #     }, status=500)
    # else:
    #     return JsonResponse({
    #         'msg': '请求参数错误',
    #     }, status=500)

    if oid is None:
        return JsonResponse({
            'code': 500,
            'msg': 'error',
            'data': '请求参数错误',
        })
    else:
        nodes = DataTreeNode.objects.filter(parent_oid=oid)
        # 根据nodes中数据的parent_code构建树形结构
        _list = []
        # 为nodes中数据添加children属性
        for i in nodes:
            _list.append({
                'oid': i.oid,
                'nodeType': i.node_type,
                'name': i.name,
                'parentOid': i.parent_oid,
                'children': []
            })

        print('_list:', _list)
        return JsonResponse({
            'code': 200,
            'msg': 'success',
            'data': _list,
        })


@csrf_exempt
def create_tree_node(request):
    """
    创建树节点
    :param request:
    :return:
    """
    if request.method == 'POST':
        node_data = json.loads(request.body.decode('utf-8'))

        # 请求参数预处理
        for key in node_data.keys():
            node_data[camel_to_snake(key)] = node_data.pop(key)
        if node_data['node_type'] == 'server_group':
            node_data['parent_oid'] = 0

        # 存储节点数据
        try:
            result = DataTreeNode.objects.create(**node_data)
            data = {
                'oid': result.oid,
                'node_type': result.node_type,
                'name': result.name,
                'parent_oid': result.parent_oid,
            }
            return JsonResponse({
                'code': 200,
                'msg': 'success',
                'data': data,
            })
        except Exception as e:
            print('创建节点失败：', e)
            return JsonResponse({
                'code': 500,
                'msg': 'e',
                'data': '创建节点失败',
            })
    else:
        return JsonResponse({
            'code': 500,
            'msg': 'error',
            'data': '请求方式错误',
        })


def build_tree(nodes):
    tree = []
    for node in nodes:
        if node['parent_oid'] == "":
            tree.append(node)
        else:
            for item in nodes:
                if item['oid'] == node['parent_oid']:
                    item['children'].append(node)

    return tree


def get_data_type(request):
    """
    获取数据类型
    :return:
    """
    cursor = connection.cursor()
    cursor.execute(
        "SELECT* FROM    (SELECT        pg_catalog.format_type(t.oid,NULL) AS typname,        CASE WHEN typelem > 0 THEN typelem ELSE t.oid END as elemoid,        typlen, typtype, t.oid, nspname,        (SELECT COUNT(1) FROM pg_catalog.pg_type t2 WHERE t2.typname = t.typname) > 1 AS isdup,        CASE WHEN t.typcollation != 0 THEN TRUE ELSE FALSE END AS is_collatable    FROM        pg_catalog.pg_type t    JOIN        pg_catalog.pg_namespace nsp ON typnamespace=nsp.oid    WHERE        (NOT (typname = 'unknown' AND nspname = 'pg_catalog'))     AND        typisdefined AND typtype IN ('b', 'c', 'd', 'e', 'r') AND NOT EXISTS (SELECT 1 FROM pg_catalog.pg_class WHERE relnamespace=typnamespace AND relname = typname AND relkind != 'c') AND (typname NOT LIKE '_%' OR NOT EXISTS (SELECT 1 FROM pg_catalog.pg_class WHERE relnamespace=typnamespace AND relname = substring(typname FROM 2)::name AND relkind != 'c')) AND nsp.nspname != 'information_schema' UNION SELECT 'smallserial', 0, 2, 'b', 0, 'pg_catalog', false, false UNION SELECT 'bigserial', 0, 8, 'b', 0, 'pg_catalog', false, false UNION SELECT 'serial', 0, 4, 'b', 0, 'pg_catalog', false, false) AS dummy ORDER BY nspname <> 'pg_catalog', nspname <> 'public', nspname, 1")
    rows = cursor.fetchall()
    response_data = []
    for item in rows:
        obj = {
            'typeName': item[0],
            'elemoid': item[1],
            'typlen': item[2],
            'typtype': item[3],
            'oid': item[4],
            'nspname': item[5],
            'isdup': item[6],
            'is_collatable': item[7],
        }
        response_data.append(obj)

    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': response_data,
    })
