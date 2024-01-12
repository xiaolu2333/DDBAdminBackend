import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


###################################### element plus 相关 ######################################
@csrf_exempt
def post_checkbox_data(request):
    """
    element plus 复选框传值
    :return:
    """
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        return JsonResponse({
            'code': 200,
            'status': 'success',
            'msg': '提交数据成功！',
            'data': data,
        }, safe=False)
    else:
        return JsonResponse({
            'code': 500,
            'msg': 'error',
            'data': '请求方式错误',
        })


def get_checkbox_data(request):
    """
    element plus 复选框取值
    :return: [{'id': int, 'label': string, 'value': string}]
    """
    if request.method == 'GET':
        response_data = [
            {'id': 1, 'label': '黄金糕', 'value': '黄金糕'},
            {'id': 2, 'label': '双皮奶', 'value': '双皮奶'},
            {'id': 3, 'label': '蚵仔煎', 'value': '蚵仔煎'},
            {'id': 4, 'label': '龙须面', 'value': '龙须面'},
            {'id': 5, 'label': '北京烤鸭', 'value': '北京烤鸭'},
            {'id': 6, 'label': '油条', 'value': '油条'}
        ]
        return JsonResponse({
            'code': 200,
            'status': 'success',
            'msg': '获取数据成功！',
            'data': response_data,
        }, safe=False)
    else:
        return JsonResponse({
            'code': 500,
            'msg': 'error',
            'data': '请求方式错误',
        })
