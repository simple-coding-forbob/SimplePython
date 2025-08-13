# 1)
def myprint2():
    print("안녕")
myprint2()

myprint = lambda : print("안녕")
myprint()      # 출력: 16

# 2)
def myhello2(x):
    print(x)
myhello2("hello")

myhello2 = lambda x: print(x)
myhello2("hello")

# 3)
def square2(x):
    return x**2
print(square2(4))

square2 = lambda x: x**2
print(square2(4))          # 출력: 16
