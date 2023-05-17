from faker import Faker


def test_0():
    faker = Faker()
    data_list = []

    # 生成 50 个在 (0, 100)区间的整数
    for i in range(50):
        data_list.append(faker.random_int(0, 100))
    print(data_list)


if __name__ == '__main__':
    test_0()
