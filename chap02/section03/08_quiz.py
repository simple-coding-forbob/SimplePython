# 글자 -> 정수
a="2"
print(int(a))

# 글자 -> 실수
b="2.2"
print(float(b))

# 글자 -> 참/거짓
c=""
print(bool(c))

# 숫자(정수,실수) -> 글자
d=2
print("일은 " + str(d))
e=2.2
print("실수는 "+str(e))

# f-string 표시법: {} 로 자료형 변환 없이 변수를 사용할 수 있습니다.
h="장길산"
i=30
print(f"{h}은 나이가 {i}세 입니다.")