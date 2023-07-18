import math


class Structure1:
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure1):
    _fields = ['name', 'shares', 'price']


if __name__ == '__main__':
    s = Stock("ACME", 30, 12.1)
    print('test1 over')
    s2 = Stock("test", "11")




