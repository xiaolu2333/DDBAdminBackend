from faker import Faker


def test_0():
    faker = Faker()
    # 生成一个随机时间 2020-01-01 00:00:00 ~ 2023-12-31 23:59:59
    date_time = faker.date_time_between(start_date='-3y', end_date='+3y')
    print(date_time)


if __name__ == '__main__':
    test_0()
