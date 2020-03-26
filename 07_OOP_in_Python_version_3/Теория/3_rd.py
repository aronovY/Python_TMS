class Student:
    def __init__(self, name, age=19, marks=[]):
        self.name = name
        self.age = age
        self.marks = marks

    def get_average_mark(self):
        return (
            round(sum(self.marks) / len(self.marks), 2) if self.marks else None
        )

    def add_mark(self, mark):
        self.marks.append(mark)

    def __str__(self):
        return f'{self.name} ({self.age})'

    def __repr__(self):
        return str(self)

    def __gt__(self, other):
        return self.get_average_mark() > other.get_average_mark()

    def __ge__(self, other):
        return self.get_average_mark() >= other.get_average_mark()

    def __eq__(self, other):
        return self.get_average_mark() == other.get_average_mark()

    def __bool__(self):
        return self.get_average_mark() >= 8

    def __call__(self, *args, **kwargs):
        print(self)

    def __len__(self):
        return len(self.marks)

    def __add__(self, other):
        return Student(
            f'{self.name}{other.name}', self.age + other.age, self.marks + other.marks
        )


student_1 = Student('Alex', 23, [7, 5, 10])
student_2 = Student('Kate', 21, [9, 4, 10])

# student_1.add_mark(15)
# # print(f'{student_1 if student_1 >= student_2 else student_2}')
#
# # print(f'{student_2}{" не" if not student_2 else ""} молодец')
#
# print(student_1.get_average_mark())
#
# print(len(student_1))

student_3 = student_1 + student_2
print(student_3, student_3.marks, student_3.get_average_mark())