import re


def camel_to_snake(name):
    """
    驼峰命名转为蛇形命名
    :param name:
    :return:
    """
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)  # 将驼峰命名转为蛇形命名
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)  # 将驼峰命名转为蛇形命名
    return name.lower()


def snake_to_camel(name):
    """
    蛇形命名转为驼峰命名
    :param name:
    :return:
    """
    name = name.title().replace('_', '')  # 将蛇形命名转为驼峰命名
    return name[0].lower() + name[1:]


if __name__ == '__main__':
    before = 'createTime'
    print('before:', before)
    after = camel_to_snake(before)
    print('after:', after)
    before = 'create_time'
    print('before:', before)
    after = snake_to_camel(before)
    print('after:', after)
