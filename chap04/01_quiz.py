# 전체 리스트(배열) 화면에 표시하기
a = ["가", "나", "다"]
print(a)

# 1번째 값 화면에 표시하기
print(a[0])

# 리스트에 값 추가하기
a.append("라")
print(a)

# 리스트의 길이(크기) 표시하기
print(len(a))

# 슬라이싱: 0~1까지 잘라서 화면에 표시하기
print(a[0:2])

# 리스트에 값 삭제하기
a.remove("라")
del a[0]
print(a)


# 리스트 정렬, 복사본 사용(원본 훼손 없음)
b = [7,3,2,4]
c=sorted(b)
print(c) # 오름차순
d=sorted(b, reverse=True)
print(d) # 내림차순


