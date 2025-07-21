# 집합표현입니다. 중복이 제거됩니다.
a={"a","a","b"}
print(a)

# 추가
a.add("c")
print(a)

# 삭제
a.remove("c")
print(a)

a={"c","d"}
b={"d","e"}
# 합집합
print(a | b)
# 교집합
print(a & b)
# 차집합
print(a - b)