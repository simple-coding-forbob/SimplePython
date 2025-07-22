# 전체 리스트(배열) 화면에 표시하기
a = ["a", "b", "c"]
print(a)

# 1번째 값 화면에 표시하기
print(a[0])

# 리스트에 값 추가하기
a.append("d")
print(a)

# 리스트에 값 수정하기
a[0]="aa"
print(a)

# 리스트의 길이(크기) 표시하기
print(len(a))

# 리스트에 값 삭제하기
a.remove("d")
# del a[0]
print(a)
