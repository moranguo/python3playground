'''
Python调用Shell，有两种方法：os.system(cmd)或os.popen(cmd)脚本执行过程中的输出内容。实际使用时视需求情况而选择。
两者的区别是：
os.system(cmd)的返回值是脚本的退出状态码，只会有0(成功),1,2等等
os.popen(cmd)返回脚本执行的输出内容作为返回值

比如计算一个文件的md5值：

os.system(cmd):

   该方法在调用完shell脚本后，返回一个信号代码。
os.system('md5sum /root/all.sql')
7735d611ebce91ebb4c7acc4747a8b67  /root/all.sql
0      #返回的信号代码  0(成功)

os.popen(cmd):
   这种调用方式是通过管道的方式来实现，函数返回一个file-like的对象，里面的内容是脚本输出的内容（可简单理解为echo输出的内容）。使用os.popen调用脚本的情况：
如：
md5_value = os.popen('md5sum /root/all.sql')    #将结果赋值给变量
print(type(md5_value))          #查看类型
<class 'os._wrap_close'>
print(md5_value.read().split()[0])         #取值
7735d611ebce91ebb4c7acc4747a8b67
明显地，像调用”ls”这样的shell命令，应该使用popen的方法来获得内容
'''

import os
import subprocess

print(subprocess.getoutput('dir'))
print(subprocess.getstatusoutput('dir'))
