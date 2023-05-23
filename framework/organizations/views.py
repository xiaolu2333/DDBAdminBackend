import json

from django.core.paginator import Paginator
from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from framework.organizations.models import Organization


def get_organization(request):
    """
    获取机构列表
    :return: 机构列表树形结构
    """
    if request.method == 'GET':
        # 获取所有数据
        all_data = Organization.objects.all()
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


@csrf_exempt
def create_organization(request):
    """
    创建机构
    :param request:
    :return:
    """
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print('data:', data)
        # 将 data.parentCode 转换为 parent_code
        data['parent_code'] = data.pop('parentCode')
        try:
            # 将数据插入到数据库
            Organization.objects.create(**data)

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
                    'data': '机构代码已存在',
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
