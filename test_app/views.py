import json
import os
import random
import time

from django.core.files.base import ContentFile
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse, FileResponse
from django.utils.encoding import escape_uri_path
from django.views.decorators.csrf import csrf_exempt

from DDBAdminBackend.settings import BASE_DIR
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

        # 文件保存路径
        file_path = os.path.join(BASE_DIR, 'static', 'uploadfiles', file.name)

        # 保存文件，通过文件对象的 chunks() 方法，一块一块的保存，防止文件过大，导致内存溢出
        with open(file_path, 'wb') as f:
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
    文件生成器，防止文件过大，导致内存溢出
    :param file_name: 文件名
    :param chunk_size: 块大小
    :return: 生成器
    """
    from DDBAdminBackend.settings import BASE_DIR
    path = os.path.join(BASE_DIR, 'static', 'uploadfiles', file_name)
    # 读取大文件
    with open(path, mode='rb') as f:
        while True:
            file = f.read(chunk_size)
            if file:
                yield file
            else:
                break


# 流下载文件
def download_file_by_stream(request):
    if request.method == 'GET':
        filename = 'Django Styleguide.pdf'
        try:
            # 方式一：使用 StreamingHttpResponse() 下载文件
            # # StreamingHttpResponse() 接收一个生成器，返回一个 StreamingHttpResponse 对象
            # response = StreamingHttpResponse(file_iterator(filename))
            # 方式二：使用 FileResponse() 下载文件
            # # FileResponse() 接收一个文件对象，返回一个 FileResponse 对象，直接将文件以小块的形式返回给客户端
            path = os.path.join(BASE_DIR, 'static', 'uploadfiles', filename)
            file = open(path, 'rb')
            # 构造 response
            response = FileResponse(file)
            # 增加headers
            response['Content-Type'] = 'application/octet-stream'  # 告诉浏览器这是一个二进制文件
            response['Access-Control-Expose-Headers'] = "Content-Disposition, Content-Type"  # 允许浏览器访问的headers
            response['Content-Disposition'] = "attachment; filename={}".format(escape_uri_path(filename))  # 下载文件的名称
            return response
        except FileNotFoundError:
            return JsonResponse({
                'code': 500,
                'msg': '文件不存在',
                'data': None,
            })
        except Exception:
            return JsonResponse({
                'code': 500,
                'msg': '下载失败',
                'data': None,
            })
    else:
        return JsonResponse({
            'code': 500,
            'msg': '请求方式错误',
            'data': None,
        })


# url 下载文件
def download_file_by_url(request):
    if request.method == 'GET':
        filename = 'Django Styleguide.pdf'
        try:
            # 读取文件
            path = os.path.join(BASE_DIR, 'static', 'uploadfiles', filename)

            return JsonResponse({
                'code': 200,
                'msg': 'success',
                'data': path
            })
        except FileNotFoundError:
            return JsonResponse({
                'code': 500,
                'msg': 'error',
                'data': '文件不存在',
            })
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
        # 获取POST请求中的数据
        post_data = request.POST
        print('post_data:', post_data)

        # 获取名字
        name = post_data.get('name', None)
        # 获取密码
        password = post_data.get('password', None)

        # 获取文件对象
        file = post_data.get('file', None)
        # 获取文件名
        file_name = request.POST.get('fileName', None)
        # 将文件保存到本地
        file_path = os.path.join(BASE_DIR, 'static', 'uploadfiles', file_name)
        file = ContentFile(file)
        # 获取文件大小 kb
        print('文件大小 %.2f kb' % (file.size / 1024))
        with open(file_path, 'w') as f:
            for chunk in file.chunks():
                f.write(chunk)

        return JsonResponse({
            'code': 200,
            'msg': 'success',
            'data': '上传成功',
        })


def download_form_file(request):
    pass


# 文件分块上传
@csrf_exempt
def upload_file_by_block(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        chunk_number = request.POST.get('chunkNumber')
        total_chunks = request.POST.get('totalChunks')
        file_name = request.POST.get('fileName')
        # 检查并创建保存文件的目录
        save_dir = os.path.join(BASE_DIR, 'static', 'uploadfiles', 'save', 'files')
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        # 保存文件块到临时文件
        temp_file_path = os.path.join(save_dir, f'{file_name}.part{chunk_number}')
        with open(temp_file_path, 'wb+') as temp_file:
            for chunk in file.chunks():
                temp_file.write(chunk)

        # 检查是否所有文件块都已上传
        if int(chunk_number) == int(total_chunks) - 1:
            # 所有文件块已上传，将它们合并成完整文件
            final_file_path = os.path.join(save_dir, file_name.split('.')[0])
            try:
                with open(final_file_path, 'ab') as final_file:
                    for i in range(int(total_chunks)):
                        temp_file_path = os.path.join(save_dir, f'{file_name}.part{i}')
                        with open(temp_file_path, 'rb') as temp_file:
                            final_file.write(temp_file.read())
                        os.remove(temp_file_path)
                # 文件合并完成后的操作
                return JsonResponse({
                    'code': 200,
                    'data': None,
                    'message': '文件分片上传完成',
                    'success': True
                })
            except FileNotFoundError as e:
                print(e)
                return JsonResponse({
                    'code': 500,
                    'data': None,
                    'message': str(e),
                    'success': False
                })
            except Exception as e:
                return JsonResponse({
                    'code': 500,
                    'data': None,
                    'message': str(e),
                    'success': False
                })
        else:
            # # 删除临时文件
            # os.remove(save_dir)
            return JsonResponse({
                'code': 200,
                'data': None,
                'message': '还有文件块未上传',
                'success': True
            })
    else:
        return JsonResponse({
            'code': 500,
            'data': None,
            'msg': '请求方式错误',
            'success': False
        })


@csrf_exempt
def upload_file_by_breakpoint(request):
    if request.method == 'POST':
        file = request.FILES['file']
        file_name = request.POST.get('filename')
        chunk_size = request.POST.get('chunkSize')
        save_dir = os.path.join(BASE_DIR, 'static', 'uploadfiles', 'save', 'files')
        content_range = request.headers.get('Content-Range')
        print('content_range:', content_range)

        # 检查并创建保存文件的目录
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        if content_range:
            start, end, total = parse_content_range_header(content_range)
            temp_file_path = os.path.join(save_dir, f'{file_name}')
            # 根据起始位置和文件大小，将文件写入指定位置
            with open(temp_file_path, 'ab') as destination:
                destination.seek(start)
                destination.write(file.read())
            if end == total:
                # 文件上传完成
                return JsonResponse({
                    'code': 200,
                    'msg': '文件全部上传成功',
                    'data': None,
                    'success': True
                })
            else:
                if total - start < int(chunk_size):
                    next_start = start + 1
                    j_res = JsonResponse({
                        'code': 308,
                        'msg': '文件部分上传成功',
                        'data': None,
                        'success': True,
                    })
                    j_res.headers['Range'] = f'bytes={next_start}-{total}'
                    return j_res
                # 返回部分内容的响应，包括下一块的起始位置
                next_start = end + 1
                j_res = JsonResponse({
                    'code': 308,
                    'msg': '文件部分上传成功',
                    'data': None,
                    'success': True,
                })
                j_res.headers['Range'] = f'bytes={next_start}-{next_start + int(chunk_size)}'
                return j_res
        else:
            # 非断点续传请求，直接保存文件
            with open(save_dir, 'wb') as destination:
                destination.write(file.read())
            return JsonResponse({
                'code': 200,
                'msg': '文件上传成功',
                'data': None,
                'success': True
            })
    else:
        return JsonResponse({
            'code': 405,
            'msg': '请求方式错误',
            'data': None,
            'success': False
        })


def parse_content_range_header(content_range):
    range_str, total_str = content_range.split('/')
    start, end = range_str.split(' ')[1].split('-')
    return int(start), int(end), int(total_str)


@csrf_exempt
def aircraft_data(request):
    if request.method == 'POST':
        # 仿真
        emulation = request.POST.get('emulation', None)
        # 轮次
        _round = request.POST.get('round', None)
        # 绘制项
        drawItem = request.POST.get('drawItem', None)

        # 50个时间
        import datetime

        # 创建一个空列表来存储时间点
        x_data = []

        # Get the current time
        current_time = datetime.datetime.now()

        # Generate 50 time points
        for i in range(50):
            time_formatted = current_time.strftime("%H:%M:%S")
            x_data.append(time_formatted)
            current_time += datetime.timedelta(minutes=1)

        # 打印生成的时间点
        for time_point in x_data:
            print(time_point)

        y_data = [random.randint(0, 100) for _ in range(50)]
        return JsonResponse({
            'code': 200,
            'msg': 'success',
            'data': {
                'xData': x_data,
                'yData': y_data,
            },
            'success': True
        })
    else:
        return JsonResponse({
            'code': 405,
            'msg': '请求方式错误',
            'data': None,
            'success': False
        })


@csrf_exempt
def interrupt_upload_request(request):
    """
    中断文件上传
    :param request:
    :return:
    """
    if request.method == 'POST':
        r = request
        # 获取POST请求中的数据
        post_data = request.POST
        files_data = request.FILES

        # 获取名字
        name = post_data.get('name', None)
        # 获取描述
        description = post_data.get('description', None)

        # 获取方案文件对象
        schemeFile = files_data.get('schemeFile', None)
        # 获取数据文件对象
        dataFiles = files_data.get('dataFiles', None)

        # 保存文件
        # 方案文件保存路径
        scheme_file_path = os.path.join(BASE_DIR, 'static/uploadfiles/save/files', schemeFile.name)
        # 保存文件
        with open(scheme_file_path, 'wb') as f:
            for chunk in schemeFile.chunks():
                f.write(chunk)

        return JsonResponse({
            'code': 200,
            'data': None,
            'msg': '上传成功',
            'success': True
        })
    else:
        return JsonResponse({
            'code': 500,
            'data': None,
            'msg': '请求方式错误',
            'success': False
        })


def interrupt_download_request(request):
    """
    中断文件下载
    :param request:
    :return:
    """
    if request.method == 'GET':
        filename = 'user_info_big.csv'
        try:
            path = os.path.join(BASE_DIR, 'static', 'uploadfiles', filename)
            file = open(path, 'rb')
            # 构造 response
            response = FileResponse(file)
            # 增加headers
            response['Content-Type'] = 'application/octet-stream'  # 告诉浏览器这是一个二进制文件
            # response['Content-Length'] =   # 告诉浏览器文件长度
            response['Access-Control-Expose-Headers'] = "Content-Disposition, Content-Type"  # 允许浏览器访问的headers
            response['Content-Disposition'] = "attachment; filename={}".format(escape_uri_path(filename))  # 下载文件的名称
            return response
        except FileNotFoundError:
            return JsonResponse({
                'code': 500,
                'msg': '文件不存在',
                'data': None,
            })
        except Exception:
            return JsonResponse({
                'code': 500,
                'msg': '下载失败',
                'data': None,
            })


if '__main__' == __name__:
    create_test_data()
