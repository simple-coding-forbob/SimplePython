with open("../output/sample.txt", "r", encoding="utf-8") as f:
    # 1줄씩 읽기
    for line in f:
        print("[줄] " + line.strip()) # 줄바꿈 제거

