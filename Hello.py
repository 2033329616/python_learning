# !/usr/bin/env python3
# encoding:utf-8

'a test module'             # 任何模块代码第一个字符串视为文档注释

__author__ = 'David'        # 把作者名字写到变量中

import sys  # sys模块的argv变量，用list存储命令行的所有参数，第一个参数是py文件的名称

def hello():
    """This function can output the parameters which is got in the command line."""   # 函数的注释docstring
    args = sys.argv         # 获取命名行参数列表
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s' % args[1])
    else:
        print('Too many arguments!')
    print('sys.argv:', args)

if __name__ == '__main__':
    hello()