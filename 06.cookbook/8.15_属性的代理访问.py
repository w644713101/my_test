class A:
    def spam(self, x):
        print(f'into A spam {x}')

    def foo(self):
        print('into A foo')


class B1:
    """简单的代理"""
    def __init__(self):
        self._a = A()

    def spam(self, x):
        print(f'into B1 spam')
        return self._a.spam(x)

    def foo(self):
        print(f'into B1 foo')
        return self._a.foo()

    def bar(self):
        print(f'into B1 bar')


class B2:
    """使用 __getattr__ 的代理，代理方法比较多的时候"""
    def __init__(self):
        self._a = A()

    def bar(self):
        print(f'into B2 bar')

    def __getattr__(self, item):
        print('into B2 __getattr__ ')
        return getattr(self._a, item)


if __name__ == '__main__':
    t = B2()
    t.bar()
    print('-'*20)
    t.spam(20)


