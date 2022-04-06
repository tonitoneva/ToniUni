from inheritance.project3i.person import Person
from inheritance.project3i.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."