import json

from django.http import JsonResponse


def index(request):
    """
    获取ERD信息
    :param request:
    :return:
    """
    data = {
        'nodeDataArray': [],
        'linkDataArray': []
    }

    products = {
        'key': "Products",
        'items': [
            {'name': "ProductID", 'iskey': True, 'figure': "Decision", 'color': 'red'},
            {'name': "ProductName", 'iskey': False, 'figure': "Hexagon", 'color': 'blue'},
            {'name': "SupplierID", 'iskey': False, 'figure': "Decision", 'color': "purple"},
            {'name': "CategoryID", 'iskey': False, 'figure': "Decision", 'color': "purple"}
        ]
    }
    data['nodeDataArray'].append(products)

    suppliers = {
        'key': "Suppliers",
        'items': [
            {'name': "SupplierID", 'iskey': True, 'figure': "Decision", 'color': 'red'},
            {'name': "CompanyName", 'iskey': False, 'figure': "Hexagon", 'color': 'blue'},
            {'name': "ContactName", 'iskey': False, 'figure': "Hexagon", 'color': 'blue'},
            {'name': "Address", 'iskey': False, 'figure': "Hexagon", 'color': 'blue'}
        ]
    }
    data['nodeDataArray'].append(suppliers)

    categories = {
        'key': "Categories",
        'items': [
            {'name': "CategoryID", 'iskey': True, 'figure': "Decision", 'color': 'red'},
            {'name': "CategoryName", 'iskey': False, 'figure': "Hexagon", 'color': 'blue'},
            {'name': "Description", 'iskey': False, 'figure': "Hexagon", 'color': 'blue'},
            {'name': "Picture", 'iskey': False, 'figure': "TriangleUp", 'color': 'pink'}
        ]
    }
    data['nodeDataArray'].append(categories)

    order_details = {
        'key': 'Order Details',
        'items': [
            {'name': 'OrderID', 'iskey': True, 'figure': "Decision", 'color': 'red'},
            {'name': 'ProductID', 'iskey': True, 'figure': "Decision", 'color': 'red'},
            {'name': 'UnitPrice', 'iskey': False, 'figure': "Circle", 'color': 'green'},
            {'name': 'Quantity', 'iskey': False, 'figure': "Circle", 'color': 'green'},
            {'name': 'Discount', 'iskey': False, 'figure': "Circle", 'color': 'green'},
        ]
    }
    data['nodeDataArray'].append(order_details)

    link_data = [
        {'from': "Products", 'to': "Suppliers", 'text': "ProductID M", 'toText': "SupplierID 1"},
        # {'from': "Products", 'to': "Categories", 'text': "ProductID M", 'toText': "CategoryID 1"},
        {'from': "Order Details", 'to': "Products", 'text': "ProductID M", 'toText': "ProductID 1"}
    ]
    data['linkDataArray'] = link_data

    return JsonResponse({
        'code': 200,
        'msg': 'success',
        'data': data,
    })
