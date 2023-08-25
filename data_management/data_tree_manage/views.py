import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
    if oid is None:
        return JsonResponse({
            'code': 500,
            'msg': 'error',
            'data': '请求参数错误',
        })
    else:
        nodes = DataTreeNode.objects.filter(parent_oid=oid)
        # 根据nodes中数据的parent_code构建树形结构
        list = []
        # 为nodes中数据添加children属性
        for i in nodes:
            list.append({
                'oid': i.oid,
                'nodeType': i.node_type,
                'name': i.name,
                'parentOid': i.parent_oid,
                'children': []
            })

        print('list:', list)
        return JsonResponse({
            'code': 200,
            'msg': 'success',
            'data': list,
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
