numbers = [1, 2, 3, 4]
# 홀수만 배열로 만들기
a = list(filter(lambda x: x % 2 == 1, numbers))
print(a)  # [2, 4]
