#!/usr/bin/env python
# import unittest,string,random
# from Common.variables_func import *
# class a():
#     def b(self):
#         dd=11
#         return dd
#     def c(self):
#         cc={'age':self.b()+1,"code":get_yaml_variable('code_session')}
#         print(cc)
# if __name__ == "__main__":
#    a().c()
#    numbers = list(string.digits)
#    print(random.sample(numbers, 8))
# import requests
# res=requests.post(url='https://www.easy-mock.com/mock/5d02f6d52f7e2b340a7183f8/order/v1/charging/start_charging',verify=False)
# print(res.text)

import os
#获取当前文件所在路径
# cur_path=os.path.dirname(os.path.abspath(__file__))
# print(cur_path)
# parent_path = os.path.dirname(cur_path) #获得d所在的目录,即d的父级目录
# print(parent_path)
# parent_paths  = os.path.dirname(parent_path) ##获得parent_path所在的目录即parent_path的父级目录
# print(parent_paths)

import os
a=os.getcwd()
print(a)
b=os.path.dirname(a)
print(b)
c=os.path.join(os.getcwd(),'1','Config','conf.yaml')
d=os.path.abspath('Config\conf.yaml')
print(c)
print(d)

print('{}'.format(os.getcwd()+"\Config\conf.yaml"))
print(os.path.abspath('Config\conf.yaml'))
#当使用unittest框架时建议使用下面方式读取文件
print(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'Config\conf.yaml'))