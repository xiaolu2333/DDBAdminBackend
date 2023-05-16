from faker import Faker


def create_fake_data():
    faker = Faker(locale='zh_CN')
    user_info_list = []

    # 生成 100 个用户
    for i in range(2):
        user_name = faker.name()
        # 用用户名的拼音作为 user_code
        user_code = faker.pystr_format(string_format='{{pystr_format:10,10}}', letters='abcdefghijklmnopqrstuvwxyz')
        password = faker.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
        # 随机从 绝密、机密、秘密、内部、公开 中选一个
        secret_level = faker.random_element(elements=('绝密', '机密', '秘密', '内部', '公开'))
        # 随机生成 True 或 False
        enabled = faker.boolean(chance_of_getting_true=50)
        locked = False
        # 随机生成 datetime
        date_time = faker.date_time_between(start_date='-1y', end_date='now')
        # 随机生成 IP 地址
        ip = faker.ipv4()
        login_history = {"ip": ip, "date_time": date_time}
        sortNum = faker.random_int(min=1, max=100)
        remark = faker.text(max_nb_chars=200)
        create_time = faker.date_time_between(start_date='-1y', end_date='now')
        update_time = faker.date_time_between(start_date='-1y', end_date='now')
        user_info_list.append(
            {
                "user_name": user_name,
                "user_code": user_code,
                "password": password,
                "secret_level": secret_level,
                "enabled": enabled,
                "locked": locked,
                "login_history": login_history,
                "sortNum": sortNum,
                "remark": remark,
                "create_time": create_time,
                "update_time": update_time,
            }
        )
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
