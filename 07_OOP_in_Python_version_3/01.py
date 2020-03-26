class Task1B:
    def __init__(self):
        self.x = 1


class Task1A(Task1B):
    def __init__(self):
        super().__init__()
        self.x = 2


class Task1D:
    def __init__(self):
        self.x = 3


class Task1C(Task1B, Task1D):
    def __init__(self):
        super().__init__()


class Task1E(Task1D):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    a = Task1A()
    print(a.x)
    b = Task1B()
    print(b.x)
    c = Task1C()
    print(c.x)
    d = Task1D()
    print(d.x)
    e = Task1E()
    print(e.x)


