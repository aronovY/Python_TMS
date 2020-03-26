class MyClass:
    def __init__(self, x):
        self.x = x

    def first(self):
        return 1

    @classmethod
    def second(cls):
        pass

    @staticmethod
    def third():
        pass

    def get_x_plus_one(self):
        return self.x + 1

    @property
    def x_plus_one(self):
        return self.x + 1


obj = MyClass(5)
obj.first()

obj.second()
MyClass.second()

obj.third()
MyClass.third()

print(obj.get_x_plus_one())
print(obj.x_plus_one)