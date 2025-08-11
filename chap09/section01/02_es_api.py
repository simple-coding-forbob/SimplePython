import requests
from elasticsearch import Elasticsearch

# 1. 공공 API 주소와 인증키를 준비합니다.
API_URL = "https://api.odcloud.kr/api/15096713/v1/uddi:3c9fef37-f48d-4264-9b9f-b24ee240e54c"  # 공공 API 주소
API_KEY = "INH5JlH9iuKNiuZVX2tblTV7m9CqLf0rNKopVhVq8vF0LpzZNp658j7xXeucRpukCmqE+ekjfJk9g3+PWAGWZA=="  # 본인의 API 키를 여기에 넣으세요

# 2. Elasticsearch 서버에 연결합니다.
es = Elasticsearch("http://localhost:9200")  # 로컬 ES 서버 주소

# 3. API 요청에 사용할 쿼리스트링을 만듭니다.
params = {
    "serviceKey": API_KEY,  # API 인증키
    "page": 1,  # 요청할 페이지 번호
    "perPage": 5  # 한번에 가져올 데이터 개수
}

# 4. API에 GET 요청을 보냅니다.
response = requests.get(API_URL, params=params)

# 5. 서버가 성공적으로 응답했는지 확인합니다.
if response.status_code == 200:  # 200은 성공 상태 코드
    print("db 저장 시작")
    # 6. 응답에서 'data' 항목을 꺼냅니다. 없으면 [](빈리스트)가 return 됩니다.
    data = response.json().get("data", [])

    # 7. 가져온 데이터 각각을 Elasticsearch에 저장합니다.
    # es.index(index="인덱스명", document=행데이터)
    for item in data:
        es.index(index="cook-api", document=item)

    # 8. 저장 완료 메시지 출력
    print("데이터 저장 완료")
else:
    # 9. 실패 시 상태 코드 출력
    print("API 호출 실패:", response.status_code)

# ===== 직접 실행되는 부분 =====
if __name__ == "__main__":
    pass