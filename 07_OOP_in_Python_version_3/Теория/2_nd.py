class Student:
    UNIVERSITY = 'BSUIR'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} ({self.age})'


class AliveStudent(Student):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks


class ExpelledStudent(Student):
    def __init__(self, name, age, reason='По приколу'):
        super().__init__(name, age)
        self.reason = reason


student_1 = AliveStudent('Alex', 20, [7, 10, 8])
student_2 = ExpelledStudent('John', 22)
print(student_1)
print(student_2)

print(Student.UNIVERSITY)
print(AliveStudent.UNIVERSITY)
print(student_1.UNIVERSITY)