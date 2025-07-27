# requests 라이브러리 가져오기
import json
import requests
# 뷰티풀숩 라이브러기 가져오기
from bs4 import BeautifulSoup

# 파일로 쓰기 함수로 만들고 실행하기
# 파이썬은 위에 정의해야함: 위에서 부터 밑으로 정확히 실행됨
def write(name, result):
    with open(name, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

# 1) 웹페이지 가져오기
url = "https://www.simple-coding.com/guest-book/"
response = requests.get(url)

# 2) html 정보 파싱(메모리 올리기)
soup = BeautifulSoup(response.text, "html.parser")

# 3) title 만 가져오기
res = soup.select_one("title") # 결과 중 첫번째만 가져오기

# 4) file 에 저장: title 태그 사이 글자만 저장하기: result.text
data=[]
data.append({
    "title": res.text.strip()
})
write("../output/quiz2.json",data)

