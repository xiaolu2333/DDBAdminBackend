from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    """
    注册中心-数据库注册页
    :param request:
    :return:
    """

    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': '数据库注册页',
    })


def create_domain_database(request):
    """
    创建域内数据库
    :param request:
    :return:
    """
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': '创建域内数据库',
    })


def create_cross_domain_database(request):
    """
    创建跨域数据库
    :param request:
    :return:
    """
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': '创建跨域数据库',
    })


def publish_database(request):
    """
    发布数据库
    :param request:
    :return:
    """
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': '发布数据库',
    })


def authorize_db_user(request):
    """
    数据库用户授权
    :param request:
    :return:
    """
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': '数据库用户授权',
    })


def init_center_database(request):
    """
    初始化注册中心数据库
    :param request:
    :return:
    """
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': '初始化注册中心数据库',
    })


def register_db(request):
    """
    注册数据库
    :param request:
    :return:
    """
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': '注册数据库',
    })


def logout_db(request):
    """
    注销数据库
    :param request:
    :return:
    """
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': '注销数据库',
    })


def delete_db(request):
    """
    删除数据库
    :param request:
    :return:
    """
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': '删除数据库',
    })


def manage_db_register(request):
    """
    数据库注册管
    :param request:
    :return:
    """
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': '数据库注册管理',
    })


def manage_db_logout(request):
    """
    数据库注销管理
    :param request:
    :return:
    """
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': '数据库注销管理',
    })


def share_db_table(request):
    """
    共享数据库表
    :param request:
    :return:
    """
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': '共享数据库表',
    })


def authorize_db_table(request):
    """
    数据库表授权
    :param request:
    :return:
    """
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': '数据库表授权',
    })


def configure_db_hba(request):
    """
    配置数据库hba文件
    :param request:
    :return:
    """
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': '配置数据库hba文件',
    })


def configure_db_conf(request):
    """
    配置数据库conf文件
    :param request:
    :return:
    """
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': '配置数据库conf文件',
    })


def configure_db_bouncer(request):
    """
    配置数据库连接池
    :param request:
    :return:
    """
    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': '配置数据库连接池',
    })
