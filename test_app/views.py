import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

test_data = [
    {
        "id": 10001,
        "name": 'Test1',
        "status": 1,
    },
    {
        "id": 10002,
        "name": 'Test2',
        "status": 1,
    },
    {
        "id": 10003,
        "name": 'Test3',
        "status": 1,
    }
]


def index(request):
    # 返回json数据
    return JsonResponse(test_data, safe=False)


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
