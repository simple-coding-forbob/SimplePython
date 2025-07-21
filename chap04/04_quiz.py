a={"name":"장길산", "age":30}
print(a)

# 키로 표시하기: 1번째 방법, 없으면 에러 발생
print(a["age"])
# 2번째 방법: get("키",기본값) ,없으면 None 으로 표시
print(a.get("age", 0))

# 값 수정하기
a["age"]=35
print(a)

# 새 키:값 추가하기
a["job"]="영업사원"
print(a)

# 키:값 삭제하기
del a["job"]
print(a)

#