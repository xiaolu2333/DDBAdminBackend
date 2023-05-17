from faker import Faker


def test_0():
    faker = Faker()

    # 随机程程一个包含 ['导入', '导出', '创建', '删除', '修改', '查询', '注销', '连接', '断开', '申请'] 中任意一个元素的字符串
    content = faker.random_element(elements=('导入', '导出', '创建', '删除', '修改', '查询', '注销', '连接', '断开', '申请'))
    # 随机生成一句话
    slut = faker.sentence()
    content += slut

    return content
