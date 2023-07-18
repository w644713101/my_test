class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print('into People property')
        return self._name

    @name.setter
    def name(self, value):
        print('into People name.setter')
        self._name = value

    @name.deleter
    def name(self):
        print('into People name.deleter')

    def get2(self):
        return self._name


class SubPerson(Person):
    @property
    def name(self):
        print('into SubPerson property.name')
        return super().name

    @name.setter
    def name(self, value):
        print('into SubPerson name.setter')
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('into SubPerson name.deleter')
        super(SubPerson, SubPerson).name.__delete__(self)


class SubPerson2(Person):
    @Person.name.setter
    def name(self, value):
        print('into SubPerson2 Person.name.setter')
        super(SubPerson2, SubPerson2).name.__set__(self, value)


if __name__ == '__main__':
    # s = SubPerson('test')
    s = SubPerson2('test')
    print('-'*50)
    print(s.name)
    print('-'*50)
    s.name = 'test2'
    import pdb;pdb.set_trace()

