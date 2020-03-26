class A:
    x = 1

    def foo(self):
        return 1 + 2


print(type(A))

B = type('B', (), {'x': 2, 'foo': A.foo})

print(hasattr(A, 'y'))
setattr(A, 'y', 3)
print(A.y)
delattr(A, 'x')
print(A.x)