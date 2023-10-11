"""
 @Author: DFL
 @Email: xxx@xxx.com
 @FileName: manipulate_file.py
 @DateTime: 2023/10/10 10:06
 @SoftWare: PyCharm
 @Description: 文件操作
"""


# import pandas as pd


class FileManipulation:
    """
    文件操作
    """
    __file_path = None
    __encoding = None

    def __init__(self, file_path, encoding='utf-8'):
        self.__file_path = file_path
        self.__encoding = encoding

    # 读取文件内容
    def read_file(self, chunk_size=4096):
        """
        读取文件内容
        :param chunk_size: 文件块大小，单位字节，默认4096字节
        :return:
        """
        # 文件分块读取
        with open(self.__file_path, 'r', encoding=self.__encoding) as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                # 打印块序号
                print('file.tell():', file.tell())
                # Process the chunk of data
                # Example: print the chunk
                print(chunk)

    def write_file(self, file_content):
        """
        写入文件内容
        :param file_content: 文件内容
        :return:
        """
        with open(self.__file_path, 'w', encoding=self.__encoding) as f:
            f.write(file_content)

    def append_file(self, file_content):
        """
        追加文件内容
        :param file_content: 文件内容
        :return:
        """
        with open(self.__file_path, 'a', encoding=self.__encoding) as f:
            f.write(file_content)

    def parse_file(self, file_type):
        """
        通过pandas解析文件，
        :param file_type: 文件类型
        :return:
        """
        file_type_mapping = {
            'csv': pd.read_csv,
            'excel': pd.read_excel,
            'json': pd.read_json,
            'xml': pd.read_json
        }

        if file_type in file_type_mapping:
            data = file_type_mapping[file_type](self.__file_path)
        else:
            raise ValueError("Unsupported file type")

        # Process the data as per your requirements
        # Example: print the first few rows of the data
        print(data.head())

    def get_file_size(self):
        """
        读取文件大小
        :return:
        """
        import os
        file_size = os.path.getsize(self.__file_path)
        return file_size / 1024 / 1024

    def get_file_line(self):
        """
        读取文件行数
        :return:
        """
        with open(self.__file_path, 'r', encoding=self.__encoding) as f:
            file_lines = f.readlines()
        return len(file_lines)

    def get_file_list(self, dir_path):
        """
        读取文件夹下的文件
        :param dir_path: 文件夹路径
        :return:
        """
        import os
        file_list = os.listdir(dir_path)
        return file_list


if __name__ == '__main__':
    # fm = FileManipulation('user_info_big_2.csv', encoding='utf-8')
    # fm = FileManipulation('test.xml', encoding='utf-8')
    # file_size = fm.get_file_size()
    # print(str(file_size) + ' MB')
    # file_line = fm.get_file_line()
    # print(str(file_line) + ' 行')
    # fm.read_file(1024 * 1024 * 10)

    def case1(**kwargs):
        required_args = ['a']
        for arg in required_args:
            if arg not in kwargs:
                raise ValueError(f"Missing required argument: {arg}")
        # 打印参数名称
        for arg in kwargs:
            print('arg:', arg)


    def case2(**kwargs):
        required_args = [
            'a',
            'b'
        ]
        for arg in required_args:
            if arg not in kwargs:
                raise ValueError(f"Missing required argument: {arg}")
        for arg in kwargs:
            print('arg:', arg)


    def case3(**kwargs):
        required_args = [
            'a',
            'b',
            'c'
        ]
        for arg in required_args:
            if arg not in kwargs:
                raise ValueError(f"Missing required argument: {arg}")
        for arg in kwargs:
            print('arg:', arg)

    switch = {
        1: case1(a=1, b=2),
        2: case2(a='a'),
        3: case3(a="2333", b=True, c=[1, 2, 3])
    }

    switch[2]('2')
