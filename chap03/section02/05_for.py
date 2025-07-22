# 배열 == 리스트
a=[[1,2],[3,4]]
for i in a:
    for j in i:
        print(j)

print()

# 인덱스 번호를 이용해서 표시하기
c=[[2,3],[4,5]]
for i in range(len(c)):
    for j in range(len(c[i])):
        print(c[i][j])