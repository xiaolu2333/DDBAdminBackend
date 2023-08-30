"""
 @Author: DFL
 @Email: xxx@xxx.com
 @FileName: processes.py.py
 @DateTime: 2023/8/30 12:32
 @SoftWare: PyCharm
"""
from subprocess import PIPE, Popen


# noinspection PyTypeChecker
class BatchProcess:
    def __init__(self, cmd, *args, **kwargs):
        self._cmd = cmd
        self._args = args
        self._kwargs = kwargs
        self._stdin = None  # 标准输入 键盘
        self._stdout = PIPE  # -1 标准输出（演示器、终端) 保存到管道中以便进行操作
        self._stderr = PIPE  # 标准错误，保存到管道
        self._shell = True
        self._stime = self._etime = None

    def run(self):
        proc = Popen(
            self._cmd,
            self._stdin,
            self._stdout,
            self._stderr,
            self._shell
        )
        out_info, err_info = proc.communicate()
        return out_info.decode('gbk'), err_info.decode('gbk')
