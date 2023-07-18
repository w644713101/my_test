# -*- coding: utf-8 -*-
# @Time    : 2023/7/6 16:54
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : 02.producer_consumer_model.py
def consumer():
    print('[CONSUMER] start')
    r = 'start'
    while True:
        n = yield r
        if not n:
            print('n is empty')
            continue
        print(f'[CONSUMER] Consumer is consuming {n}')
        r = '200 ok'


def producer(c):
    # 启动generator
    start_value = c.send(None)
    print(start_value)
    n = 0
    while n < 3:
        n += 1
        print(f'[PRODUCER] Producer is producing {n}')
        r = c.send(n)
        print(f'[PRODUCER] Consumer return: {r}')

    # 关闭generator
    c.close()


# 创建生成器
c = consumer()
# 传入生成器
producer(c)




















