from inspect import isfunction


class Pep8Warrior:
    def __new__(cls, *args, **kwargs):
        # new_args = {}
        name, parents, attrs = args
        new_name = name.title().replace('_', '')
        new_attrs = {}
        for at, value in attrs.items():
            if at.startswith('__'):
                new_attrs[at] = value
            elif isfunction(value):
                new_attrs[at.lower()] = value
            elif callable(value):
                new_attrs[at.title().replace('_', '')] = value
            else:
                new_attrs[at.upper()] = value
        return type(new_name, parents, new_attrs)


class my_class(metaclass=Pep8Warrior):
    x = 10
    Y = 20

    class mYaMAZINGcLASS:
        pass

    def FuNc(self):
        return 5

    def __str__(self):
        return 'hello'


obj = my_class()
print(my_class.__name__)
print(obj)
print(obj.X)
print(obj.Y)
print(obj.func())
print([attr for attr in dir(obj) if not attr.startswith('__')])
