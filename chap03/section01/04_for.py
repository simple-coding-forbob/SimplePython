# 배열 == 리스트
a=[1,2,3]
for i in a:
    print(i)

print()

b="abc"
for i in b:
    print(i)

print()

# range(시작(생략),끝,간격(생략))
for i in range(0,5,1):
    print(i)

print()

for i in range(4):
    print(i)

print()

for _ in range(5):
    print("*", end="")

print()

# 인덱스번호를 이용해서 표시하기
# len(배열): 길이
d=[2,3,4]
for i in range(len(d)):
    print(d[i])


