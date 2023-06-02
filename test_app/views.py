import json
import os

from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse
from django.utils.encoding import escape_uri_path
from django.views.decorators.csrf import csrf_exempt
from utils.fake_data import fake_user, fake_time, fake_text_content
from test_app.models import TestData
from utils.fake_data.fake_user import test_1


def index(request):
    """
    vex-table局部更新的测试数据
    :param request:
    :return:
    """
    # 将数据插入到数据库中
    # from faker import Faker
    # faker = Faker(locale='zh_CN')
    # user_info_list = []
    #
    # for i in range(500):
    #     name = faker.name()
    #     # 随机生成一个整数
    #     status = faker.random_int(min=0, max=99999)
    #     user_info_list.append(
    #         {
    #             "name": name,
    #             "status": status,
    #         }
    #     )
    #
    # TestData.objects.bulk_create(
    #     [TestData(name=i['name'], status=i['status']) for i in user_info_list]
    # )
    # return HttpResponse('ok')

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
    print('data_list:', data_list)
    # 返回json数据
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'dataList': data_list,
    }, safe=False)


@csrf_exempt
def handle_direct_update(request):
    """
    vex-table局部更新之直接更新
    :param request:
    :return:
    """
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
    """
    vex-table局部更新之保存更新
    :param request:
    :return:
    """
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))['data']
        try:
            # 更新数据
            TestData.objects.filter(id=int(data['id'])).update(**data)
            d = TestData.objects.get(id=int(data['id']))
            # 转为json格式
            d = {
                "id": d.id,
                "name": d.name,
                "status": d.status,
            }
            return JsonResponse({
                'code': 200,
                'msg': 'success',
                'data': d
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
    """
    测试分页功能
    :param request:
    :return:
    """
    if request.method == 'GET':
        # 获取所有数据
        all_data = TestData.objects.all()
        # 设置每页显示的数据条数
        page_index = int(request.GET.get('pageIndex', 1))
        # 获取当前页码，如果没有传递，则默认为第一页
        page_size = int(request.GET.get('pageSize', 10))
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


def scroll_pagination_data(request):
    """
    测试滚动加载功能
    :param request:
    :return:
    """
    if request.method == 'GET':
        # 获取所有数据
        all_data = TestData.objects.all()
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
                "user": query_data[i]['name'],
                "operation": fake_text_content.test_0(),
                "time": fake_time.test_0()
            }
            print(item)
            return_data.append(item)

        # 如果 len(query_data) < page_size，则表示还有数据，否则表示没有数据了
        has_more = True

        return JsonResponse({
            'code': 200,
            'msg': 'success',
            'dataList': return_data,
            'hasMore': has_more,
        }, safe=False)


def use_echarts_line_chart(request):
    """
    echarts 折线图数据
    :param request:
    :return:
    """
    # 生成12个随机整数
    import random
    data = [random.randint(0, 100) for _ in range(12)]
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': data,
    }, safe=False)


def create_test_data():
    fake_data = test_1()
    # 将 fake_data 中的数据存入sqlite数据库
    for data in fake_data:
        TestData.objects.create(**data)


# 上传文件
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        print('request.FILES:', request.FILES)
        # 获取文件对象
        file = request.FILES.get('file')
        print("{0}".format(file.name))
        # 将文件大小转为 KB，保留两位小数
        print('文件大小 %.2f kb' % (file.size / 1024))
        print('文件类型 {}'.format(file.content_type))
        # 保存文件，通过文件对象的 chunks() 方法，一块一块的保存，防止文件过大，导致内存溢出
        with open(file.name, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
        return JsonResponse({
            'code': 200,
            'msg': 'success',
            'data': '上传成功',
        })
    else:
        return JsonResponse({
            'code': 500,
            'msg': 'error',
            'data': '请求方式错误',
        })


def file_iterator(file_name, chunk_size=512):
    """
    文件生成器,防止文件过大，导致内存溢出
    :param file_path: 文件名
    :param chunk_size: 块大小
    :return: 生成器
    """
    from DDBAdminBackend.settings import BASE_DIR
    path = os.path.join(BASE_DIR, file_name)
    # 读取大文件
    with open('user_info.csv', mode='rb') as f:
        while True:
            file = f.read(chunk_size)
            if file:
                yield file
            else:
                break


# 下载文件
def download_file(request):
    if request.method == 'GET':
        filename = 'user_info.csv'
        try:
            response = StreamingHttpResponse(file_iterator(filename))
            # 增加headers
            response['Content-Type'] = 'application/octet-stream'
            response['Access-Control-Expose-Headers'] = "Content-Disposition, Content-Type"
            response['Content-Disposition'] = "attachment; filename={}".format(escape_uri_path(filename))
            return response
        except Exception:
            return JsonResponse({
                'code': 500,
                'msg': 'error',
                'data': '下载失败',
            })
    else:
        return JsonResponse({
            'code': 500,
            'msg': 'error',
            'data': '请求方式错误',
        })


@csrf_exempt
def upload_form_file(request):
    if request.method == 'POST':
        # 获取表单数据
        print('request.POST:', request.POST)

        # print('request.FILES:', request.FILES)
        # # 获取文件对象
        # file = request.FILES.get('file')
        # print("{0}".format(file.name))
        # # 将文件大小转为 KB，保留两位小数
        # print('文件大小 %.2f kb' % (file.size / 1024))
        # print('文件类型 {}'.format(file.content_type))
        # # 保存文件，通过文件对象的 chunks() 方法，一块一块的保存，防止文件过大，导致内存溢出
        # with open(file.name, 'wb') as f:
        #     for chunk in file.chunks():
        #         f.write(chunk)
        return JsonResponse({
            'code': 200,
            'msg': 'success',
            'data': '上传成功',
        })


def download_form_file(request):
    pass


if '__main__' == __name__:
    create_test_data()
