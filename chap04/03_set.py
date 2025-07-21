# 집합표현입니다. 중복이 제거됩니다.
a={1,2,3,3}
print(a)

# 추가
a.add(4)
print(a)

# 삭제
a.remove(4)
print(a)

b={1,2}
c={2,3}
# 합집합
print(b | c)
# 교집합
print(b & c)
# 차집합
print(b - c)