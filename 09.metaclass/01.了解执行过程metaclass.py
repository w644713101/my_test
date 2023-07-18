class MetaClass(type):

    def __new__(cls, name, bases, namespace):
        print('MetaClass.__new__ has be called')
        print(' -', name, bases, namespace)
        return super().__new__(cls, name, bases, namespace)

    def __init__(self, name, bases, namespace):
        print('MetaClass.__init__ has be called')
        print(' -', name, bases,namespace)

    def __call__(self, *args, **kwargs):
        print('MetaClass.__call__ has be called')
        print(' -', args, kwargs)
        return super().__call__(*args, **kwargs)


class TestClass(metaclass=MetaClass):
    a = 123

    def __new__(cls, *args, **kwargs):
        print("TestClass.__new__ has be called")
        print(" -", args, kwargs)
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        print("TestClass.__init__ has be called")
        print(" -", args, kwargs)

    def test(self):
        print("TestClass.test has be called")


t = TestClass(123, 12, 1)
t.test()
