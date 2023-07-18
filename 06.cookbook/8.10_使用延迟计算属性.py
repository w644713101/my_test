import math


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('into Circle.area')
        return math.pi * self.radius ** 2


if __name__ == '__main__':
    t = Circle(20)
    print(t.area)
    print('-'*20)
    print(t.area)



