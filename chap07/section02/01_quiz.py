# requests 라이브러리 가져오기
import requests
# 뷰티풀숩 라이브러기 가져오기
from bs4 import BeautifulSoup

# 1) 웹페이지 가져오기
url = "https://www.simple-coding.com/guest-book/"
response = requests.get(url)

# 2) title 만 가져오기
soup = BeautifulSoup(response.text, "html.parser")

result = soup.select_one("title") # 결과 중 첫번째만 가져오기

# 4) file 에 저장: title 태그 사이 글자만 저장하기: result.text
with open("../output/quiz.txt", "w", encoding="utf-8") as f:
    f.write(result.text)