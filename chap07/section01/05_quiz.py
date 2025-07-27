# requests 라이브러리 가져오기
from urllib.parse import urljoin

import requests
# 뷰티풀숩 라이브러기 가져오기
from bs4 import BeautifulSoup

try:
    # 1) 웹페이지 가져오기
    url = "https://www.simple-coding.com/guest-book/"
    response = requests.get(url)

    # 2) html 정보 파싱(메모리 올리기)
    soup = BeautifulSoup(response.text, "html.parser")

    # 3) a 만 모두 가져오기
    results = soup.select("img")
    # print(result)   # 디버깅 확인
    for i in results:
        # i.get(속성): html 속성값
        # i.text: 태그 사이 글자
        if i.get("src"):    # 있을 때만 처리 예) <a>글자</a> 이 경우 제외
            print(urljoin(url, i.get("src")))

except Exception as e:
    print("전체 오류 발생", e)