import json

from django.core.paginator import Paginator
from django.db import IntegrityError
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from framework.departments.models import Department
from framework.organizations.models import Organization


def get_department_list(request):
    """
    获取部门列表
    :return: 部门列表树形结构
    """
    if request.method == 'GET':
        org_id = request.GET.get('orgId', None)
        if org_id:
            org = Organization.objects.get(id=int(org_id))
            if org is not None:
                return_data = []
                query_data = Department.objects.filter(org_id=org)

                # 构造返回数据
                for i in range(len(query_data)):
                    item = {
                        'id': query_data[i].id,
                        'name': query_data[i].name,
                        'code': query_data[i].code,
                        'parentCode': query_data[i].parent_code,
                        'enabled': query_data[i].enabled,
                        'createTime': query_data[i].create_time,
                        'updateTime': query_data[i].update_time,
                        'org': query_data[i].org_id.id,
                        # 'data': DjangoJSONEncoder().encode(model_to_dict(org)),
                    }
                    return_data.append(item)

                return JsonResponse({
                    'code': 200,
                    'msg': 'success',
                    'dataList': return_data,
                }, safe=False)
            else:
                return JsonResponse({
                    'code': 500,
                    'msg': 'error',
                    'data': 'org does not exist',
                })
        else:
            return JsonResponse({
                'code': 500,
                'msg': 'error',
                'data': 'orgId is required',
            })
    else:
        return JsonResponse({
            'code': 500,
            'msg': 'error',
            'data': 'request method is not allowed',
        })


def get_department_detail(request):
    # 获取请求参数 id
    id = request.GET.get('id', None)
    if id is not None:
        # 获取指定 id 的数据
        query_data = Department.objects.filter(id=int(id)).values()[0]
        return_data = {
            'id': query_data['id'],
            'name': query_data['name'],
            'code': query_data['code'],
            'parentCode': query_data['parent_code'],
            'enabled': query_data['enabled'],
            'orgId': query_data['org_id_id'],
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
        data = json.loads(request.body.decode('utf-8'))
        # 数据预处理
        data['parent_code'] = data.pop('parentCode')
        data['org_id'] = data.pop('orgId')

        # 根据 org_id 获取组织机构
        organization = Organization.objects.get(id=data['org_id'])
        department = Department(org_id=organization, name=data['name'], code=data['code'],
                                parent_code=data['parent_code'], enabled=data['enabled'])

        print('department:', department)

        try:
            # 将数据插入到数据库
            department.save()

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
