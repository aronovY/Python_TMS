import typing
from dataclasses import dataclass, field


@dataclass(order=True)
class Student:
    name: str = field(compare=False)
    average_mark: float
    age: int = field(default=18, repr=False, compare=False)
    subjects: typing.List[str] = field(default_factory=list, repr=False, compare=False)

    def __post_init__(self):
        self.first_letter = self.name[0] if self.name else None


student = Student('Petya', 6.9)
student1 = Student('', 8.3, 25,)
student2 = Student('John', 6.2, 19, ['Math', 'History', 'English'])
student3 = Student('Kate', 7.1, 30)
student4 = Student('Matt', 3.2, 21, ['Physic', 'Geography'])
student5 = Student('Julia', 10, 41)
print(sorted([student, student1, student2, student3, student4, student5]))
"""                 [Student(name='Matt', average_mark=3.2), 
                    Student(name='John', average_mark=6.2), 
                    Student(name='Petya', average_mark=6.9), 
                    Student(name='Kate', average_mark=7.1), 
                    Student(name='', average_mark=8.3), 
                    Student(name='Julia', average_mark=10)] 
                    """


