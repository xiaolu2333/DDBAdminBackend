"""
 @Author: DFL
 @Email: xxx@xxx.com
 @FileName: computer_properties.py
 @DateTime: 2023/10/10 9:51
 @SoftWare: PyCharm
 @Description: 读取计算机的一些属性
"""

import psutil

class ComputerProperties:
    """
    读取计算机的一些属性
    """
    def __init__(self):
        pass

    def get_cpu_info(self):
        """
        获取cpu信息
        :return:
        """
        cpu_count = psutil.cpu_count()
        cpu_usage = psutil.cpu_percent()
        return cpu_count, cpu_usage

    def get_mem_info(self):
        """
        获取内存信息
        :return:
        """
        mem = psutil.virtual_memory()
        mem_total = mem.total
        mem_used = mem.used
        mem_percent = mem.percent
        return mem_total, mem_used, mem_percent

    def get_disk_info(self):
        """
        获取磁盘信息
        :return:
        """
        disk = psutil.disk_usage('/')
        disk_total = disk.total
        disk_used = disk.used
        disk_percent = disk.percent
        return disk_total, disk_used, disk_percent

    def get_net_info(self):
        """
        获取网络信息
        :return:
        """
        net_io = psutil.net_io_counters()
        net_bytes_sent = net_io.bytes_sent
        net_bytes_recv = net_io.bytes_recv
        return net_bytes_sent, net_bytes_recv


if __name__ == '__main__':
    cp = ComputerProperties()
    cpu_count, cpu_usage = cp.get_cpu_info()
    mem_total, mem_used, mem_percent = cp.get_mem_info()
    disk_total, disk_used, disk_percent = cp.get_disk_info()
    net_bytes_sent, net_bytes_recv = cp.get_net_info()

    # 打印信息
    print(f"CPU 总数: {cpu_count}")
    print(f"CPU 使用率: {cpu_usage}%")
    print(f"内存总量: {mem_total / 1024 / 1024}MB")
    print(f"内存使用量: {mem_used / 1024 / 1024}MB")
    print(f"内存使用率: {mem_percent}%")
    print(f"磁盘总量: {disk_total / 1024 / 1024 / 1024}GB")
    print(f"磁盘使用量: {disk_used / 1024 / 1024 / 1024}GB")
    print(f"磁盘使用率: {disk_percent}%")
    print(f"发送数据: {net_bytes_sent / 1024 / 1024}MB")
    print(f"接收数据: {net_bytes_recv / 1024 / 1024}MB")
