from person import Person

class Cook(Person):
    def __init__(self, name="", ID=123, birthdate ="1/1/1900", food = "lasagna"):
        Person.__init__(self, name, ID, birthdate)
        self.food = food
    def cook(self):
        print(self.name + " is cooking.")
    def create(self):
        print(self.name + " is coming up with the worst meal possible")
    def favfood(self):
        print(self.name + " is craving " + self.food)
