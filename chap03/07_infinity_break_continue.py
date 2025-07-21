# 무한 루프,
# 0부터 1씩 증가하다가 3이면 종료하세요
i=0
while True:
    print(i)
    if(i==3):
        break
    i+=1

# 홀수만 표시하기
a=[1,2,3,4]
for i in a:
    if(i%2==0):
        continue
    print(i)