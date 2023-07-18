# -*- coding: utf-8 -*-
# @Time    : 2023/7/6 16:45
# @Author  : wzh
# @Email   : 644713101@qq.com
# @File    : 01.yield.py


def test():
    print('generator start')
    n = 1
    while True:
        yield_expression_value = yield n
        print(f'yield_expression_value = {n}')
        n += 1


# 1.创建generator对象
generator = test()
print(type(generator))

print('-'*50)

# 2.启动generator
"""
    __next__()方法: 作用是启动或者恢复generator的执行，相当于send(None)

"""
next_result = generator.__next__()
print(f'next_result = {next_result}')

print('-'*50)

# 3.发送值给yield表达式
"""
    send(value)方法：作用是发送值给yield表达式。启动generator则是调用send(None)
"""
send_result = generator.send(6666)
print(f'send_result = {send_result}')


"""
执行结果的说明：
    ①创建generator对象：包含yield表达式的函数将不再是一个函数，调用之后将会返回generator对象
    
    ②启动generator：使用生成器之前需要先调用__next__或者send(None)，否则将报错。
        启动generator后，代码将执行到yield出现的位置，也就是执行到yield n，然后将n传递到generator.__next__()这行的返回值。
        （注意，生成器执行到yield n后将暂停在这里，直到下一次生成器被启动）
        
    ③发送值给yield表达式：调用send方法可以发送值给yield表达式，同时恢复生成器的执行。生成器从上次中断的位置继续向下执行，
        然后遇到下一个yield，生成器再次暂停，切换到主函数打印出send_result。

理解这个demo的关键是：
    生成器启动或恢复执行一次，将会在yield处暂停。
    上面的第②步仅仅执行到了yield n，并没有执行到赋值语句，
    到了第③步，生成器恢复执行才给yield_expression_value赋值。
"""

