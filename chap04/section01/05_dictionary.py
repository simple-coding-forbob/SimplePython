a={"name":"홍길동", "age":20}
print(a)

# 키로 표시하기: 1번째 방법, 없으면 에러 발생
print(a["age"])
# 2번째 방법: get("키",기본값) ,없으면 None 으로 표시
# print(a.get("age", 0))

# 값 수정하기
a["age"]=25
print(a)

# 새 키:값 추가하기
a["job"]="개발자"
print(a)

# 키:값 삭제하기
del a["job"]
print(a)