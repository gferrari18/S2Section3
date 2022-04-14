from person import Person

class Driver(Person):
    def __init__(self,name = "", ID = 100, birthdate = ""):
        Person.__init__(self.name,ID,birthdate)
    def drive(self):
        print(self.name + " is driving")
    def playsong(self):
        print(self.name + " is trying to find the countriest song on the radio")
