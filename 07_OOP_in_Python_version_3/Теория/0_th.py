# y = x * (3 if x > 0 else 2)

class Student:
    def __init__(self, name, age=19, marks=[]):
        self.name = name
        self.age = age
        self.marks = marks

    def get_average_mark(self):
        return (
            round(sum(self.marks) / len(self.marks), 2) if self.marks else None
        )


student_1 = Student('Alex', marks=[5, 10, 10])
student_2 = Student('Kate', 17, [8, 9, 10])

print(f'{student_1.name} - {student_1.get_average_mark()}')
print(f'{student_2.name} - {student_2.get_average_mark()}')

print(Student.get_average_mark(student_1))

# print(f'Студент 1 - {student_1.name}, {student_1.age}, {student_1.marks}')
# print(f'Студент 2 - {student_2.name}, {student_2.age}, {student_2.marks}')

