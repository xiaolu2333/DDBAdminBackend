import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# from framework.authentication.forms import DDBAdminUserForm, DDBAdminRoleForm

def index(request):
    test_data = [
        {
            "id": 10001,
            "name": 'Test1',
            "nickname": 'T1',
            "role": 'Develop',
            "sex": '0',
            "sex2": ['0'],
            "num1": 40,
            "age": 28,
            "address": 'Shenzhen',
            "date12": '',
            "date13": ''
        },
        {
            "id": 10002,
            "name": 'Test2',
            "nickname": 'T2',
            "role": 'Develop',
            "sex": '1',
            "sex2": ['1'],
            "num1": 40,
            "age": 28,
            "address": 'Shenzhen',
            "date12": '',
            "date13": ''
        },
        {
            "id": 10003,
            "name": 'Test3',
            "nickname": 'T3',
            "role": 'Develop',
            "sex": '0',
            "sex2": ['0'],
            "num1": 40,
            "age": 28,
            "address": 'Shenzhen',
            "date12": '',
            "date13": ''
        },
        {
            "id": 10004,
            "name": 'Test4',
            "nickname": 'T4',
            "role": 'Develop',
            "sex": '1',
            "sex2": ['1'],
            "num1": 40,
            "age": 28,
            "address": 'Shenzhen',
            "date12": '',
            "date13": ''
        }
    ]
    response = JsonResponse(test_data, safe=False)
    response["Content-Type"] = "application/json;charset=utf-8"
    # 添加 code 状态码 200
    response.status_code = 200
    return response


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_name = data.get("a", None)

        try:
            if user_name:
                # 返回json数据
                return JsonResponse({
                    'code': 200,
                    'msg': 'success',
                    'data': {
                        'user_name': user_name,
                    },
                })
            else:
                return JsonResponse({
                    'code': 500,
                    'msg': 'error',
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

