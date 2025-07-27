# requests 라이브러리 가져오기
import requests
# 뷰티풀숩 라이브러기 가져오기
from bs4 import BeautifulSoup
import json

def write(name, result):
    with open(name, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

# 1) 웹페이지 가져오기
url = "https://www.simple-coding.com/"
response = requests.get(url)

# 2) html 정보 파싱(메모리 올리기)
soup = BeautifulSoup(response.text, "html.parser")

# 3) a 만 모두 가져오기
results = soup.select("a")
# print(result)   # 디버깅 확인

# 저장할 리스트
data = []

for i in results:
    # i.get(속성): html 속성값
    # i.text: 태그 사이 글자
    if i.get("href")!=None:    # 있을 때만 처리 예) <a>글자</a> 이 경우 제외
        data.append({
            "href": i.get("href").strip(),
            "text": i.text.strip()
        })
# 4) file 에 저장: title 태그 사이 글자만 저장하기:
write("../output/sample3.json", data)