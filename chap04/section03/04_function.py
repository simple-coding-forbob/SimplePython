# 함수 만들기
# 함수 정의
# {} 사용하지 않고 :, 들여쓰기를 사용합니다.
# 1)
def hi():
    print("hello")
# 함수 실행
hi()

# 2) 매개변수 사용: 홍길동
def hello(name):
    print(f"{name} 님")

hi("홍길동")

def add(a,b):
    return a+b

print(add(1,2))

def info():
    return "홍길동", 20

print(info()) # 튜플로 내보내기됨