from teacher import Teacher
from student import Student
from driver import Driver
from cook import Cook

pete = Teacher("Pete", 124, "09/12/1990")
pete.teach()
gus = Student("Gus", 123, "09/12/1995", pete)
mar = Student("Marmot", 125, "01/02/1998", pete)
don = Student("Don", 126, "01/04/1996", pete)
gus.learn()
gus.sleep()

joe = Cook("Joe", 199, "1/1/1989", "picanha")
joe.favfood()