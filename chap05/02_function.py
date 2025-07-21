a="a B"
# a 찾기
print(a.find("a"))
# in: 값 포함 여부 확인, 결과는 참(True)/거짓(False)가 됩니다.
print("B" in a)
# 공백으로 글자를 분리합니다.
print(a.split())
# 리스트의 값들을 글자로 붙이기
b=["a","b"]
print(" ".join(b))
# 글자를 특정글자로 바꾸기
print(a.replace("a","B"))
# 특정 글자 세기
print(a.count("B"))
#  * : 글자 반복
print("hi"*3)
