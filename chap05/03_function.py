# 수학모듈 모두 가져오기: 예) math.floor(), math.ceil()
# import math
# 수학모듈 중 floor, ceil 만 가져오기
# 예) floor(), ceil() 바로 사용 가능합니다.
from math import floor,ceil

a=[1,2,3]
print(max(a))
# 최소값
print(min(a))
# 합계
print(sum(a))

# 내림
print(floor(3.14))
# 반올림: round(실수, 반올림자리수)
print(round(3.14, 2))
# 올림
print(ceil(3.14))

