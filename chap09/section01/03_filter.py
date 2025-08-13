numbers = [1, 2, 3, 4]
# 짝수만 배열로 만들기
a = list(filter(lambda x: x % 2 == 0, numbers))
print(a)  # [2, 4]
