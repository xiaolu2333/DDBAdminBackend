import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from data_management.data_tree_manage.models import DataTreeNode


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
        list.append(
            {'id': i.id, 'server_group_name': i.server_group_name, 'server_name': i.server_name, 'db_name': i.db_name,
             'node_type': i.node_type, 'name': i.name, 'code': i.code, 'parent_code': i.parent_code, 'children': []})
    print('list:', list)

    tree_data = build_tree(list)
    print(tree_data)

    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': tree_data,
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
        print('node_data:', node_data)
        # 存储节点数据
        try:
            DataTreeNode.objects.create(**node_data)
        except Exception as e:
            print('创建节点失败：', e)
            return JsonResponse({
                'code': 500,
                'msg': 'e',
                'data': '创建节点失败',
            })
        return JsonResponse({
            'code': 200,
            'msg': 'success',
            'data': node_data,
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
        if node['parent_code'] == "":
            tree.append(node)
        else:
            for item in nodes:
                if item['code'] == node['parent_code']:
                    item['children'].append(node)

    return tree
