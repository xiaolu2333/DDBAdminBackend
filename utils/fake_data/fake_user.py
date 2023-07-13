from faker import Faker


def test_0():
    faker = Faker(locale='zh_CN')
    user_info_list = []

    # 500000条数据为 69948 KB
    for i in range(5000000):
        user_name = faker.name()
        # 用用户名的拼音作为 user_code
        user_code = "code_" + str(i)
        password = faker.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
        # 随机从 绝密、机密、秘密、内部、公开 中选一个
        secret_level = faker.random_element(elements=('绝密', '机密', '秘密', '内部', '公开'))
        # 随机生成 True 或 False
        enabled = faker.boolean(chance_of_getting_true=50)
        sortNum = faker.random_int(min=1, max=100)
        remark = faker.text(max_nb_chars=20)
        create_time = faker.date_time_between(start_date='-1y', end_date='now')
        update_time = faker.date_time_between(start_date='-1y', end_date='now')
        user_info_list.append(
            {
                "username": user_name,
                "usercode": user_code,
                "password": password,
                "secretlevel": secret_level,
                "enabled": enabled,
                "sortNum": sortNum,
                "remark": remark,
                "create_time": create_time,
                "update_time": update_time,
            }
        )

    # 将数据写入到CSV文件中
    import csv
    with open('user_info.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['username', 'usercode', 'password', 'secretlevel', 'enabled',
                      'sortNum', 'remark', 'create_time', 'update_time']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(user_info_list)

    return user_info_list


def test_1():
    faker = Faker(locale='zh_CN')
    data_list = []

    # 生成 100 条数据
    for i in range(100):
        name = faker.name()
        # 随机整数
        status = faker.random_int(min=0, max=100)
        data_list.append(
            {
                "name": name,
                "status": status,
            }
        )

    return data_list


if __name__ == '__main__':
    test_0()
    # test_1()
