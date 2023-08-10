import datetime
import json

from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from framework.resources.models import Menu
from utils.formatTransformer.request_and_response import snake_to_camel, camel_to_snake


def get_menu_list(request):
    """
    获取菜单列表
    :return: 菜单列表
    """
    if request.method == 'GET':
        try:
            # 获取所有数据
            query_data = Menu.objects.all()

            return_data = []
            # 构造返回数据
            for i in query_data:
                item = {
                    'id': i.id,
                    'name': i.name,
                    'path': i.path,
                    'pageType': i.page_type,
                    'menuType': i.menu_type,
                    'authType': i.auth_type,
                    'component': i.component,
                    'icon': i.icon,
                    'parentId': i.parent_id,
                    'enable': i.enable,
                    'sort': i.sort,
                    'createTime': i.create_time,
                    'updateTime': i.update_time,
                    'children': [],
                }
                return_data.append(item)
            print('return_data:', return_data)
            return JsonResponse({
                'code': 200,
                'msg': 'success',
                'dataList': return_data,
            }, safe=False)
        except Exception as e:
            return JsonResponse({
                'code': 500,
                'msg': 'error',
                'data': str(e),
            })
    else:
        return JsonResponse({
            'code': 500,
            'msg': 'error',
            'data': '请求方式错误',
        })


def get_menu_detail(request):
    # 获取路径参数 id
    _id = request.GET.get('id', None)
    if _id is not None:
        # 获取指定 id 的数据
        query_data = Menu.objects.filter(id=_id).values()[0]

        # 将 query_data 的属性转为驼峰命名，并构造返回数据
        return_data = {}
        for k, v in query_data.items():
            # 将k转为驼峰命名
            key_name = snake_to_camel(k)
            return_data[key_name] = v

        return JsonResponse({
            'code': 200,
            'msg': 'success',
            'data': return_data,
        }, safe=False)
    else:
        return JsonResponse({
            'code': 500,
            'msg': 'error',
            'data': 'id is required',
        })


@csrf_exempt
def create_menu(request):
    """
    创建菜单
    :param request:
    :return:
    """
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print('data:', data)
        data['createTime'] = datetime.datetime.now()
        data['updateTime'] = datetime.datetime.now()
        new_data = {}

        for k, v in data.items():
            # 将k转为驼峰命名
            key_name = camel_to_snake(k)
            new_data[key_name] = v

        print('new_data after transform:', new_data)
        try:
            # 将数据插入到数据库
            Menu.objects.create(**new_data)

            return JsonResponse({
                'code': 200,
                'msg': 'success',
                'data': new_data
            })
        except Exception as e:
            return JsonResponse({
                'code': 500,
                'msg': 'error',
                'data': str(e),
            })
        except IntegrityError as e:
            message = str(e).split(":")
            if message[0] == 'UNIQUE constraint failed':
                return JsonResponse({
                    'code': 500,
                    'msg': 'error',
                    'data': '菜单代码已存在',
                })
            return JsonResponse({
                'code': 500,
                'msg': 'error',
                'data': str(e),
            })
    else:
        return JsonResponse({
            'code': 500,
            'msg': 'error',
            'data': '请求方式错误',
        })


@csrf_exempt
def update_menu(request):
    # 更新菜单
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print('data:', data)
        # 获取 id
        id = data.get('id', None)
        if id is not None:
            data['updateTime'] = datetime.datetime.now()
            new_data = {}

            for k, v in data.items():
                # 将k转为驼峰命名
                key_name = camel_to_snake(k)
                new_data[key_name] = v

            print('new_data after transform:', new_data)

            try:
                # 更新数据
                Menu.objects.filter(id=id).update(**new_data)
                return JsonResponse({
                    'code': 200,
                    'msg': 'success',
                    'data': data
                })
            except Exception as e:
                return JsonResponse({
                    'code': 500,
                    'msg': 'error',
                    'data': str(e),
                })
        else:
            return JsonResponse({
                'code': 500,
                'msg': 'error',
                'data': 'id is required',
            })
    else:
        return JsonResponse({
            'code': 500,
            'msg': 'error',
            'data': '请求方式错误',
        })


@csrf_exempt
def delete_menu(request):
    """
    删除菜单
    :param request:
    :return:
    """
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print('data:', data)
        # 获取路径参数 id
        id = data.get('id', None)
        if id is not None:
            try:
                # 删除指定 id 的数据
                Menu.objects.filter(id=id).delete()
                return JsonResponse({
                    'code': 200,
                    'msg': 'success',
                    'data': data
                })
            except Exception as e:
                return JsonResponse({
                    'code': 500,
                    'msg': 'error',
                    'data': str(e),
                })
        else:
            return JsonResponse({
                'code': 500,
                'msg': 'error',
                'data': 'id is required',
            })
    else:
        return JsonResponse({
            'code': 500,
            'msg': 'error',
            'data': '请求方式错误',
        })
