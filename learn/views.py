import json
import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from DDBAdminBackend.settings import BASE_DIR


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


###################################### vxetable 相关 ######################################
def get_general_table_header(request):
    """
    获取通用表格表头
    :param request:
    :return:
    """
    if request.method == 'GET':
        response_data = [
            {'field': 'id', 'fieldType': 'number', 'title': 'ID'},
            {'field': 'name', 'fieldType': 'text', 'title': '设备名称'},
            {'field': 'desc', 'fieldType': 'text', 'title': '设备描述'},
            {'field': 'enable', 'fieldType': 'boolean', 'title': '是否启用'},
            {'field': 'number', 'fieldType': 'number', 'title': '数量'},
            {'field': 'price', 'fieldType': 'number', 'title': '价格'},
            {'field': 'manu', 'fieldType': 'text', 'title': '厂商'},
            {'field': 'date', 'fieldType': 'date', 'title': '日期'},
            {'field': 'time', 'fieldType': 'time', 'title': '时间'},
            {'field': 'datetime', 'fieldType': 'datetime', 'title': '日期时间'},
            {'field': 'options', 'fieldType': 'select', 'title': '选项', 'options': [
                {'id': 1, 'label': '组件一', 'value': '组件一'},
                {'id': 2, 'label': '组件二', 'value': '组件二'},
            ]},
        ]
        return JsonResponse({
            'code': 200,
            'status': 'success',
            'msg': '获取数据成功！',
            'data': response_data,
        }, safe=False)


def get_general_table_data(request):
    """
    获取通用表格数据
    :return: 表格数据数组
    """
    if request.method == 'GET':
        param = request.GET
        print(param)
        # 获取排序字段
        sort_field = param.get('field', None)
        # 获取排序方式
        sort_type = param.get('order', None)

        response_data = []
        if sort_field is None:
            response_data = [
                {'id': 1, 'name': '设备一', 'desc': '设备一描述', 'enable': True, 'number': 12, 'price': 12.5,
                 'manu': '厂商一',
                 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一', '组件二']},
                {'id': 2, 'name': '设备二', 'desc': '设备二描述', 'enable': False, 'number': 12, 'price': 12.5,
                 'manu': '厂商二', 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一']},
                {'id': 3, 'name': '设备三', 'desc': '设备三描述', 'enable': True, 'number': 12, 'price': 12.5,
                 'manu': '厂商三',
                 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件二']},
                {'id': 4, 'name': '设备四', 'desc': '设备四描述', 'enable': False, 'number': 12, 'price': 12.5,
                 'manu': '厂商四', 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件二']},
                {'id': 5, 'name': '设备五', 'desc': '设备五描述', 'enable': True, 'number': 12, 'price': 12.5,
                 'manu': '厂商五',
                 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一']},
                {'id': 6, 'name': '设备六', 'desc': '设备六描述', 'enable': False, 'number': 12, 'price': 12.5,
                 'manu': '厂商六', 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一', '组件二']},
                {'id': 7, 'name': '设备七', 'desc': '设备七描述', 'enable': True, 'number': 12, 'price': 12.5,
                 'manu': '厂商七',
                 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一', '组件二']},
                {'id': 8, 'name': '设备八', 'desc': '设备八描述', 'enable': False, 'number': 12, 'price': 12.5,
                 'manu': '厂商八', 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一', '组件二']},
                {'id': 9, 'name': '设备九', 'desc': '设备九描述', 'enable': True, 'number': 12, 'price': 12.5,
                 'manu': '厂商九',
                 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一', '组件二']},
                {'id': 10, 'name': '设备十', 'desc': '设备十描述', 'enable': False, 'number': 12, 'price': 12.5,
                 'manu': '厂商十', 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一', '组件二']},
                {'id': 11, 'name': '设备十一', 'desc': '设备十一描述', 'enable': True, 'number': 12, 'price': 12.5,
                 'manu': '厂商十一', 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一', '组件二']},
                {'id': 12, 'name': '设备十二', 'desc': '设备十二描述', 'enable': False, 'number': 12, 'price': 12.5,
                 'manu': '厂商十二', 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件二']},
                {'id': 13, 'name': '设备十三', 'desc': '设备十三描述', 'enable': True, 'number': 12, 'price': 12.5,
                 'manu': '厂商十三', 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一', '组件二']},
                {'id': 14, 'name': '设备十四', 'desc': '设备十四描述', 'enable': False, 'number': 12, 'price': 12.5,
                 'manu': '厂商十四', 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一']},
            ]
        else:
            response_data = [
                {'id': 1, 'name': '设备一', 'desc': '设备一描述', 'enable': True, 'number': 12, 'price': 12.5,
                 'manu': '厂商一',
                 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一', '组件二']},
                {'id': 2, 'name': '设备二', 'desc': '设备二描述', 'enable': False, 'number': 12, 'price': 12.5,
                 'manu': '厂商二', 'date': '2021-01-02', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一']},
                {'id': 3, 'name': '设备三', 'desc': '设备三描述', 'enable': True, 'number': 12, 'price': 12.5,
                 'manu': '厂商三',
                 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件二']},
                {'id': 4, 'name': '设备四', 'desc': '设备四描述', 'enable': False, 'number': 12, 'price': 12.5,
                 'manu': '厂商四', 'date': '2021-01-03', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件二']},
                {'id': 5, 'name': '设备五', 'desc': '设备五描述', 'enable': True, 'number': 12, 'price': 12.5,
                 'manu': '厂商五',
                 'date': '2021-01-04', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一']},
                {'id': 6, 'name': '设备六', 'desc': '设备六描述', 'enable': False, 'number': 12, 'price': 12.5,
                 'manu': '厂商六', 'date': '2021-01-05', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一', '组件二']},
                {'id': 7, 'name': '设备七', 'desc': '设备七描述', 'enable': True, 'number': 12, 'price': 12.5,
                 'manu': '厂商七',
                 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一', '组件二']},
                {'id': 8, 'name': '设备八', 'desc': '设备八描述', 'enable': False, 'number': 12, 'price': 12.5,
                 'manu': '厂商八', 'date': '2021-01-06', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一', '组件二']},
                {'id': 9, 'name': '设备九', 'desc': '设备九描述', 'enable': True, 'number': 12, 'price': 12.5,
                 'manu': '厂商九',
                 'date': '2021-01-01', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一', '组件二']},
                {'id': 10, 'name': '设备十', 'desc': '设备十描述', 'enable': False, 'number': 12, 'price': 12.5,
                 'manu': '厂商十', 'date': '2021-01-07', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一', '组件二']},
                {'id': 11, 'name': '设备十一', 'desc': '设备十一描述', 'enable': True, 'number': 12, 'price': 12.5,
                 'manu': '厂商十一', 'date': '2021-01-08', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一', '组件二']},
                {'id': 12, 'name': '设备十二', 'desc': '设备十二描述', 'enable': False, 'number': 12, 'price': 12.5,
                 'manu': '厂商十二', 'date': '2021-01-11', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件二']},
                {'id': 13, 'name': '设备十三', 'desc': '设备十三描述', 'enable': True, 'number': 12, 'price': 12.5,
                 'manu': '厂商十三', 'date': '2021-01-12', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一', '组件二']},
                {'id': 14, 'name': '设备十四', 'desc': '设备十四描述', 'enable': False, 'number': 12, 'price': 12.5,
                 'manu': '厂商十四', 'date': '2021-01-21', 'time': '12:00:00', 'datetime': '2021-01-01 12:00:00',
                 'options': ['组件一']},
            ]
            # 根据排序字段和排序方式进行排序
            response_data = sorted(response_data, key=lambda x: x['id'], reverse=sort_type == 'desc')
        return JsonResponse({
            'code': 200,
            'status': 'success',
            'msg': '获取数据成功！',
            'data': response_data,
        }, safe=False)


###################################### 前后端数据交互 ######################################
# 大文件分片上传
@csrf_exempt
def upload_big_file_slice(request):
    if request.method == 'POST':
        file = request.FILES['file']

        start = request.POST.get('start')
        end = request.POST.get('end')
        total = request.POST.get('size')
        index = request.POST.get('index')
        file = request.FILES.get('file')
        hash_value = request.POST.get('hash')
        file_name = request.POST.get('fileName')

        save_dir = os.path.join(BASE_DIR, 'static', 'uploadFiles', 'temp', 'files', f'{file_name.split(".")[0]}')
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        with open(os.path.join(save_dir, f'{hash_value}-----{index}.part'), 'wb') as f:
            f.write(file.read())
        return JsonResponse({
            'code': 200,
            'status': 'success',
            'msg': '分片上传成功',
            'data': {
                'start': start,
                'end': end,
                'total': total,
                'index': index,
                'hash': hash_value,
                'fileName': file_name
            }
        })
    else:
        return JsonResponse({
            'code': 405,
            'msg': '请求方式错误',
            'data': None,
            'success': False
        })


# 合并大文件分片
@csrf_exempt
def merge_big_file_slice(request):
    if request.method == 'GET':
        file_name = request.GET.get('fileName', None)
        print(file_name)
        save_dir = os.path.join(BASE_DIR, 'static', 'uploadFiles', 'temp', 'files', f'{file_name.split(".")[0]}')
        # 文件夹存在则进行合并
        if os.path.exists(save_dir):
            # 获取文件夹下的所有文件名
            file_list = os.listdir(save_dir)
            # 根据文件名中的 -----数字.part 进行排序
            file_list.sort(key=lambda x: int(x.split('-----')[-1].split('.')[0]))

            print(file_list)
            # 创建新文件
            with open(os.path.join(BASE_DIR, 'static', 'uploadFiles', 'temp', 'files', file_name), 'wb') as f:
                # 将分片文件内容写入新文件
                for file in file_list:
                    with open(os.path.join(save_dir, file), 'rb') as f1:
                        f.write(f1.read())

            # 合并完成后删除存放分片文件的文件夹
            for file in file_list:
                os.remove(os.path.join(save_dir, file))
            os.rmdir(save_dir)

        return JsonResponse({
            'code': 200,
            'status': 'success',
            'msg': '合并分片成功',
            'data': {
                'fileName': file_name
            }
        })
    else:
        return JsonResponse({
            'code': 405,
            'msg': '请求方式错误',
            'data': None,
            'success': False
        })


###################################### http 请求相关 ######################################
def test_repeat_request(request):
    """
    测试重复请求
    :param request:
    :return:
    """
    if request.method == 'GET':
        return JsonResponse({
            'code': 200,
            'status': 'success',
            'msg': '获取数据成功！',
            'data': 'success',
        }, safe=False)
    else:
        return JsonResponse({
            'code': 500,
            'msg': 'error',
            'data': '请求方式错误',
        })
