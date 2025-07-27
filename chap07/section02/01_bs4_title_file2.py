# requests 라이브러리 가져오기
import json

import requests
# 뷰티풀숩 라이브러기 가져오기
from bs4 import BeautifulSoup

# 1) 웹페이지 가져오기
url = "https://www.simple-coding.com/"
response = requests.get(url)

# 2) html 정보 파싱(메모리 올리기)
soup = BeautifulSoup(response.text, "html.parser")

# 3) title 만 가져오기
result = soup.select_one("title") # 결과 중 첫번째만 가져오기

# 4) JSON으로 저장
data=[]
data.append({
    "title": result.text.strip()
})
# json.dump : Python    객체를 JSON 형식으로 파일에 저장
# ensure_ascii=False	한글이 \uXXXX로 깨지지 않게 저장
# indent=2	            보기 좋게 들여쓰기 (예쁘게 저장)
with open("../output/sample.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

