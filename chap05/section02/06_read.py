# wb : 이진 파일 쓰기
with open("../output/sample.bin", "rb") as f:
    # utf-8 글자를 바이트로 변환해서 읽기
    a=f.read().decode("utf-8")
    print(a)
