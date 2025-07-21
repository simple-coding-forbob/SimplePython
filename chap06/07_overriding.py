class Person:
    def hi(self):
        print("hello")

class Student(Person):
    def hi(self):
        print("안녕")

a=Student()
a.hi()


