# 1)
def myprint():
    print("안녕")
myprint()

myprint = lambda : print("안녕")
myprint()      # 출력: 16

# 2)
def myhello(x):
    print(x)
myhello("hello")

myhello = lambda x: print(x)
myhello("hello")

# 3)
def square(x):
    return x**2
print(square(4))

square = lambda x: x**2
print(square(4))          # 출력: 16
