import json

from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from framework.departments.models import Department


def get_department_list(request):
    """
    获取部门列表
    :return: 部门列表树形结构
    """
    if request.method == 'GET':
        # 获取所有数据
        all_data = Department.objects.all()
        # 设置每页显示的数据条数
        page_index = int(request.GET.get('pageIndex', 1))
        # 获取当前页码，如果没有传递，则默认为第一页
        page_size = int(request.GET.get('pageSize', 10))
        # 创建 Paginator 对象，指定每页的数据条数
        paginator = Paginator(all_data, page_size)
        # 获取指定页码的数据
        current_page = paginator.get_page(page_index)

        query_data = list(current_page.object_list.values())
        return_data = []
        # 构造返回数据
        for i in range(len(query_data)):
            item = {
                'id': query_data[i]['id'],
                'name': query_data[i]['name'],
                'code': query_data[i]['code'],
                'parentCode': query_data[i]['parent_code'],
                'enabled': query_data[i]['enabled'],
                'createTime': query_data[i]['create_time'],
                'updateTime': query_data[i]['update_time'],
            }
            return_data.append(item)

        return JsonResponse({
            'code': 200,
            'msg': 'success',
            'dataList': return_data,
        }, safe=False)


def get_department_detail(request):
    # 获取路径参数 id
    id = request.GET.get('id', None)
    if id is not None:
        # 获取指定 id 的数据
        query_data = Department.objects.filter(id=id).values()[0]
        return_data = {
            'id': query_data['id'],
            'name': query_data['name'],
            'code': query_data['code'],
            'parentCode': query_data['parent_code'],
            'enabled': query_data['enabled'],
            'createTime': query_data['create_time'],
            'updateTime': query_data['update_time'],
        }

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
def create_department(request):
    """
    创建部门
    :param request:
    :return:
    """
    if request.method == 'POST':
        print('request.body:', request.body)
        data = json.loads(request.body.decode('utf-8'))
        print('data:', data)
        # 将 data.parentCode 转换为 parent_code
        data['parent_code'] = data.pop('parentCode')
        try:
            # 数据预处理
            data['parent_code'] = data.pop('parentCode')
            data['org_id'] = data.pop('orgId')
            # 将数据插入到数据库
            Department.objects.create(**data)

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
        except IntegrityError as e:
            message = str(e).split(":")
            if message[0] == 'UNIQUE constraint failed':
                return JsonResponse({
                    'code': 500,
                    'msg': 'error',
                    'data': '部门代码已存在',
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
def update_department(request):
    # 更新部门
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print('data:', data)
        # 获取 id
        id = data.get('id', None)
        if id is not None:
            # 将 data.parentCode 转换为 parent_code
            data['parent_code'] = data.pop('parentCode')
            try:
                # 更新数据
                Department.objects.filter(id=id).update(**data)
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
def delete_department(request):
    """
    删除部门
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
                Department.objects.filter(id=id).delete()
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
