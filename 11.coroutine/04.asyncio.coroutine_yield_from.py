# -*- coding: utf-8 -*-
# @Time    : 2023/7/6 17:28
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : 04.asyncio.coroutine_yield_from.py
import asyncio


@asyncio.coroutine
def compute(x, y):
    print(f'compute {x} + {y}')
    yield from asyncio.sleep(1.0)
    return x + y


@asyncio.coroutine
def print_sum(x, y):
    result = yield from compute(x, y)
    print(f'{x} + {y} = {result}')


loop = asyncio.get_event_loop()
print('start')
# 中断调用，直到协程执行结束
loop.run_until_complete(print_sum(1,2))
print('end')
loop.close()










