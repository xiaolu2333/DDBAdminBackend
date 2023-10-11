"""
 @Author: DFL
 @Email: xxx@xxx.com
 @FileName: excut_test1.py
 @DateTime: 2023/8/30 12:21
 @SoftWare: PyCharm
 @Description: 执行cmd命令
"""

from utils.jobs.processes import BatchProcess

cmd = 'D:\\DFL\\SOFTWARES\\postgresql14\\bin\\pg_dump.exe --file "C:\\Users\\DFL\\DOCUME~1\\t1.sql" --host "172.28.79.200" --port "5432" --username "postgres" --no-password --verbose --format=c --blobs --schema "public" "test1"'

p = BatchProcess(cmd)

p.run()
