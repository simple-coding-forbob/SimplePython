from elasticsearch import Elasticsearch

# ES 서버에 연결 (기본: http://localhost:9200)
es = Elasticsearch("http://localhost:9200")

# 연결 확인
if es.ping():
    print("✅ Elasticsearch 연결 성공")
else:
    print("❌ 연결 실패")

# 1) 문서 색인 (인덱스명: books, 문서 ID: 1)
doc = {
    "title": "파이썬 완벽 가이드",
    "author": "홍길동",
    "year": 2024
}
# es.index(index="인덱스명", id=기본키, document=행데이터)
es.index(index="books", id=1, document=doc)

# 2) 검색
query = {
    "query": {
        "match": {
            "title": "파이썬"
        }
    }
}

result = es.search(index="books", body=query)
for hit in result['hits']['hits']:
    print(hit["_source"])
