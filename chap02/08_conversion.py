# 글자 -> 정수
a="1"
print(int(a))

# 글자 -> 실수
b="1.2"
print(float(b))

# 글자 -> 참/거짓
c="True"
print(bool(c))

# 숫자(정수,실수) -> 글자
d=1
print("일은 " + str(d))
e=1.2
print("실수는 "+str(e))

# f-string 표시법: {} 로 자료형 변환 없이 변수를 사용할 수 있습니다.
h="홍길동"
i=20
print(h + "은 나이가 " + str(i) + "세 입니다.")
print(f"{h}은 나이가 {i}세 입니다.")