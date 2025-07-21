# 1단어 입력: a
# input() : 항상 글자를 입력 받습니다.
a=input()
print(a)

# 숫자 입력: 1
# int() : 글자 -> 정수로 바꾸기
b=int(input())
print(b)

# 실수 입력: 1.2
# float() : 글자 -> 실수로 바꾸기
c=float(input())
print(c)

# 2단어 입력: a b
# 배열변수에 넣기
# "글자". split() : 공백 기준으로 분리합니다.
d=input().split()
print(d)

# 2단어 입력: a b
# e,f 각 변수에 넣기
e,f=input().split()
print(e)
print(f)

# 홍길동
# 20
# 변수를 입력 받고 화면에 표시하기
g=input()
h=int(input())
print(f"{g}은 나이가 {h}입니다.")