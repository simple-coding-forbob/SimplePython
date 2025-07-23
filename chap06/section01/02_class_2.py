# TODO: 참고) 01, 02 합친 클래스
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hi(self):
        print("hello")

a=Person("홍길동",20)
print(a.name)
a.hi()