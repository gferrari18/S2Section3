from person import Person
from teacher import Teacher

class Student(Person):
    def __init__(self, name="", ID=-1, birthdate="1/1/1999", teacher = Teacher()):
        Person.__init__(self, name, ID, birthdate)
        self.teacher = teacher

    def study(self):
        print(self.name + " is studying.")
    def do_homework(self, course):
        print(self.name + " is doing homework for their " + course)
    def ask_question(self):
        print("wait, what?")
    def learn(self):
        print(self.name + ' is learning from ' + self.teacher.name)
    