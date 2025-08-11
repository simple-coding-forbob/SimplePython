# 배열 == 리스트
a=[1,2,3]
b=[]
# for i in a:
#     b.append(i)
# print(b)
b=[i for i in a]
print(b)

# 인덱스번호를 이용해서 표시하기
# len(배열): 길이
c=[2,3,4]
# d=[]
# for i in range(len(c)):
#     d.append(c[i])
d=[c[i] for i in range(len(c))]
print(d)


