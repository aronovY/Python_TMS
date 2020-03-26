"""Инкапсуляция"""


class Student:
    def __init__(self, name):
        self._name = name
        self.__marks = []

    def add_mark(self, mark):
        self.__marks.append(mark)

    def print_marks(self):
        print(self.__marks)

    def __str__(self):
        return f'Student {self.name}'

    def __repr__(self):
        return str(self)


# student = Student('R2D2', [10, 10, 9])
# student.marks[-1] = 10
student = Student('R2D2')
student.add_mark(10)
student.add_mark(10)
student.add_mark(9)

# student._Student__marks[-1] = 10
student.print_marks()