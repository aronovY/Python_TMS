class Group:
    def __init__(self, name, number, students):
        self.name = name
        self.number = number
        self.students = students

    def get_average_mark_for_group(self):
        marks = [student.get_average_mark() for student in self.students]
        return (sum(marks) / len(marks)) if marks else None


class Student:
    def __init__(self, name, age=19, marks=[]):
        self.name = name
        self.age = age
        self.marks = marks

    def get_average_mark(self):
        return (
            round(sum(self.marks) / len(self.marks), 2) if self.marks else None
        )

    def __str__(self):
        return f'{self.name} ({self.age})'

    def __repr__(self):
        return str(self)


student_1 = Student('Alex', 29, [5, 10, 10])
student_2 = Student('Kate', 17, [8, 9, 10])
student_4 = Student('Ann', 23, [1, 10, 10])

student_6 = Student('R2D2', 123991, [10, 10, 10])

group_1 = Group('Alpha', 101, [student_1, student_2])
group_2 = Group('Beta', 102, [student_4, student_6])

print(
    group_1.students,
    group_1.number,
    round(group_1.get_average_mark_for_group(), 2)
)
print(
    group_2.students,
    group_2.number,
    round(group_2.get_average_mark_for_group(), 2)
)