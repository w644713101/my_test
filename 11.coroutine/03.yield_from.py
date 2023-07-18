# -*- coding: utf-8 -*-
# @Time    : 2023/7/6 17:06
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : 03.yield_from.py

# 子生成器
def test(n):
    i = 0
    while i < n:
        yield i
        i += 1


# 委派生成器
"""
    两个yield from 串行执行
"""
def test_yield_from(n):
    print('test_yield_from start')
    yield from test(n)
    print("test_yield_from doing")
    yield from test(n)
    print('test_yield_from end')


for i in test_yield_from(3):
    print(i)






