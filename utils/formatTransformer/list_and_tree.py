"""
 @Author: DFL
 @Email: xxx@xxx.com
 @FileName: list_and_tree.py
 @DateTime: 2024/1/18 14:36
 @SoftWare: PyCharm
"""


def list_to_tree(list_data, container, tag):
    """
    将列表转换为树形结构
    :param list_data: 列表数据
    :param container: 容器
    :param tag: 标签
    """
    tree = []

    # 根据 parentCode 将元素放到对应的父元素的 children 中
    for i in list_data:
        if i['parentCode'] == '0':
            tree.append(i)
        else:
            for j in list_data:
                if j['code'] == i['parentCode']:
                    if 'children' not in j:
                        j['children'] = []
                    j['children'].append(i)
                    break
    return tree


def tree_to_list(tree_data, container, tag):
    """
    将树形结构转换为列表
    :param tree_data: 树形结构数据
    :param container: 容器
    :param tag: 标签
    """
    list_data = []
    for item in tree_data:
        list_data.append(item)
        if 'children' in item:
            list_data.extend(tree_to_list(item['children'], container, tag))
    return list_data
