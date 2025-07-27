# requests 라이브러리 가져오기
import requests
# 뷰티풀숩 라이브러기 가져오기
from bs4 import BeautifulSoup

# 1) 웹페이지 가져오기
url = "https://www.simple-coding.com/guest-book/"
response = requests.get(url)

# 2) html 정보 파싱(메모리 올리기)
soup = BeautifulSoup(response.text, "html.parser")

# 3) a 만 가져오기
result = soup.select("a") # 결과 중 첫번째만 가져오기
# print(result)   # 디버깅 확인
for i in result:
    # i.get(속성): html 속성값
    if i.get("href")!=None:    # href 속성 있을 때만 처리 예) <a>글자</a> 이 경우 제외
        print(i.get("href"))
