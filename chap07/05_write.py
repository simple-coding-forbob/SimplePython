# wb : 이진 파일 쓰기
with open("output/sample.bin", "wb") as f:
    # utf-8 글자를 바이트로 변환해서 쓰기
    f.write("안녕\n".encode("utf-8"))
    f.write("홍길동\n".encode("utf-8"))

