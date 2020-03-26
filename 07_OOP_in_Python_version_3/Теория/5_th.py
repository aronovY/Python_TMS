class AmazingMixin:
    def __init__(self, *args):
        self.args = args


class A(AmazingMixin):
    def __init__(self, a, b, c):
        super.__init__(a, b, c)
        self.a = a
        self.b = b
        self.c = c


class B(AmazingMixin):
    def __init__(self, d, e, f, g):
        super.__init__(d, e, f, g)
        self.d = d
        self.e = e
        self.f = f
        self.g = g
