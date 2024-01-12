from faker import Faker


# 将数据写入到CSV文件中
def test_0():
    faker = Faker(locale='zh_CN')
    user_info_list = []

    # 500000条数据为 69948 KB
    # 2000000条数据为 1.57 GB
    for i in range(300000):
        user_name = faker.name()
        # 用用户名的拼音作为 user_code
        user_code = "code_" + str(i)
        sex = faker.random_element(elements=('男', '女'))
        age = faker.random_int(min=1, max=100)
        email = faker.email()
        phone = faker.phone_number()
        is_staff = faker.boolean(chance_of_getting_true=50)
        is_superuser = faker.boolean(chance_of_getting_true=50)
        is_active = faker.boolean(chance_of_getting_true=50)
        last_login = faker.date_time_between(start_date='-1y', end_date='now')
        groups = faker.random_int(min=1, max=100)
        user_permissions = faker.random_int(min=1, max=100)
        typing_extensions = faker.random_int(min=1, max=100)
        address = faker.address()
        nikename1 = faker.name()
        nikename2 = faker.name()
        nikename3 = faker.name()
        nikename4 = faker.name()
        nikename5 = faker.name()
        nikename6 = faker.name()
        nikename7 = faker.name()
        nikename8 = faker.name()
        nikename9 = faker.name()
        nikename10 = faker.name()
        job = faker.job()
        work_address = faker.address()
        work_phone = faker.phone_number()
        work_email = faker.email()
        work_postcode = faker.postcode()
        work_fax = faker.phone_number()
        work_remark = faker.text(max_nb_chars=20)
        home_address = faker.address()
        home_phone = faker.phone_number()
        home_email = faker.email()
        home_postcode = faker.postcode()
        home_fax = faker.phone_number()
        home_remark = faker.text(max_nb_chars=20)
        school = faker.company()
        major = faker.job()
        education = faker.random_element(elements=('博士', '硕士', '本科', '大专', '高中', '初中', '小学'))
        graduation_time = faker.date_time_between(start_date='-1y', end_date='now')
        work_experience = faker.text(max_nb_chars=20)
        family_info = faker.text(max_nb_chars=20)
        # password = faker.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
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
                "用户名": user_name,
                "usercode": user_code,
                "sex": sex,
                "age": age,
                "email": email,
                "phone": phone,
                "is_staff": is_staff,
                "is_superuser": is_superuser,
                "is_active": is_active,
                "last_login": last_login,
                "groups": groups,
                "user_permissions": user_permissions,
                "typing_extensions": typing_extensions,
                "address": address,
                "nikename1": nikename1,
                "nikename2": nikename2,
                "nikename3": nikename3,
                "nikename4": nikename4,
                "nikename5": nikename5,
                "nikename6": nikename6,
                "nikename7": nikename7,
                "nikename8": nikename8,
                "nikename9": nikename9,
                "nikename10": nikename10,
                "job": job,
                "work_address": work_address,
                "work_phone": work_phone,
                "work_email": work_email,
                "work_postcode": work_postcode,
                "work_fax": work_fax,
                "work_remark": work_remark,
                "home_address": home_address,
                "home_phone": home_phone,
                "home_email": home_email,
                "home_postcode": home_postcode,
                "home_fax": home_fax,
                "home_remark": home_remark,
                "school": school,
                "major": major,
                "education": education,
                "graduation_time": graduation_time,
                "work_experience": work_experience,
                "family_info": family_info,
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
    with open('user_info_big.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['用户名',
                      'usercode',
                      "sex",
                      "age",
                      "email",
                      "phone",
                      "is_staff",
                      "is_superuser",
                      "is_active",
                      "last_login",
                      "groups",
                      "user_permissions",
                      "typing_extensions",
                      "address",
                      "nikename1",
                      "nikename2",
                      "nikename3",
                      "nikename4",
                      "nikename5",
                      "nikename6",
                      "nikename7",
                      "nikename8",
                      "nikename9",
                      "nikename10",
                      "job",
                      "work_address",
                      "work_phone",
                      "work_email",
                      "work_postcode",
                      "work_fax",
                      "work_remark",
                      "home_address",
                      "home_phone",
                      "home_email",
                      "home_postcode",
                      "home_fax",
                      "home_remark",
                      "school",
                      "major",
                      "education",
                      "graduation_time",
                      "work_experience",
                      "family_info",
                      "secretlevel",
                      "enabled",
                      "sortNum",
                      "remark",
                      "create_time",
                      "update_time",
                      ]

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


# 将数据写入到Excel文件中
def test_2():
    faker = Faker(locale='zh_CN')
    user_info = {
        'user_name': [],
        'user_code': [],
        'sex': [],
        'age':[],
        'email': [],
        'phone': [],
        'is_staff': [],
    }

    # 300000条数据为 14366 KB
    # 1000000条数据为  KB
    for i in range(1000000):
        user_name = faker.name()
        # 用用户名的拼音作为 user_code
        user_code = "code_" + str(i)
        sex = faker.random_element(elements=('男', '女'))
        age = faker.random_int(min=1, max=100)
        email = faker.email()
        phone = faker.phone_number()
        is_staff = faker.boolean(chance_of_getting_true=50)
        user_info['user_name'].append(user_name)
        user_info['user_code'].append(user_code)
        user_info['sex'].append(sex)
        user_info['age'].append(age)
        user_info['email'].append(email)
        user_info['phone'].append(phone)
        user_info['is_staff'].append(is_staff)

    # 使用pandas 将数据写入到 Excel 文件中
    import pandas as pd
    df = pd.DataFrame(user_info)
    df.to_excel('user_info.xlsx', index=False)


if __name__ == '__main__':
    # test_0()
    # test_1()
    test_2()
