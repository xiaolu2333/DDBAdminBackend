import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils.fake_data.fake_user import *
from test_app.models import TestData


def index(request):
    # 从数据库中获取50条数据
    data = TestData.objects.all()[:20]
    # 将 QuerySet 数据添加到 list 中
    data_list = []
    for i in data:
        data_list.append(
            {
                "id": i.id,
                "name": i.name,
                "status": i.status,
            }
        )

    # 返回json数据
    return JsonResponse(data_list, safe=False)


@csrf_exempt
def handle_direct_update(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print('data:', data)

        # 生成一个随机整数
        import random
        data['status'] = random.randint(0, 99999)
        try:
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
            'data': '请求方式错误',
        })


@csrf_exempt
def handle_save_the_update(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print('data:', data)
        try:
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
            'data': '请求方式错误',
        })


def pagination_data(request):
    if request.method == 'GET':
        # 获取所有数据
        all_data = TestData.objects.all()
        # 设置每页显示的数据条数
        page_index = int(request.GET.get('pageIndex', 1))
        # 获取当前页码，如果没有传递，则默认为第一页
        page_size = int(request.GET.get('pageSize', 20))
        # 创建 Paginator 对象，指定每页的数据条数
        paginator = Paginator(all_data, page_size)
        # 获取指定页码的数据
        current_page = paginator.get_page(page_index)
        # 获取页面总数
        total_page = paginator.count // page_size + 1

        return JsonResponse({
            'code': 200,
            'msg': 'success',
            'dataList': list(current_page.object_list.values()),
            'pageIndex': page_index,
            'pageSize': page_size,
            'totalRow': paginator.count,
            'totalPage': total_page,
        }, safe=False)


def create_test_data():
    fake_data = test_1()
    # 将 fake_data 中的数据存入sqlite数据库
    for data in fake_data:
        TestData.objects.create(**data)


if '__main__' == __name__:
    create_test_data()
