a={"name":"장길산", "age":30}
print(a)

# 키로 표시하기: 1번째 방법, 없으면 에러 발생
print(a["age"])

# 값 수정하기
a["age"]=35
print(a)

# 새 키:값 추가하기
a["job"]="영업사원"
print(a)

# 키:값 삭제하기
del a["job"]
print(a)