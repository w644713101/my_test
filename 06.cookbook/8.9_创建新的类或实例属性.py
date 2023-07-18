class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print('into __get__')
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print('into __set__')
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        import pdb;pdb.set_trace()
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        print('into __delete__')
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    p = Point(2, 3)
    print(f'p.x is {p.x}')
    print(f'p.y = 5')
    p.y = 5
    print('p.x = 2.3')
    p.x = 2.3
