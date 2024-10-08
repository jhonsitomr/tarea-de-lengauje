class Student:

    id: str
    name: str

    def __init__(self, i: str, n: str):

        self.id = i
        self.name = n

class Library:

    students: list[Student] = []

    def add(self, student: Student):

        self.students.append(student)

    def remove(self, student: Student):

        self.students.remove(student)

    def bulk(self) -> list[Student]:

        return self.students
