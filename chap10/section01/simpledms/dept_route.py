from flask import Blueprint, request, jsonify, Response
from elasticsearch import Elasticsearch
import time

# ES 연결
es = Elasticsearch(
    ["https://localhost:9200"],
    basic_auth=("elastic", "=U5oxindf+JStU2U25mT"),
    verify_certs=False
)
INDEX_NAME = "department"

bp = Blueprint("dept", __name__)

# match 검색 (dname 기준, 검색어 없으면 전체 검색)
@bp.route("/dept/search", methods=["GET"])
def select_all():
    keyword = request.args.get("keyword", "").strip()
    body = search_keyword(keyword)
    result = es.search(index=INDEX_NAME, body=body)
    return jsonify(make_dept(result))

def search_keyword(keyword: str):
    # 검색어에 맞는 Elasticsearch 쿼리 생성
    query = {"match_all": {}} if not keyword else {"match_phrase": {"dname": keyword}}
    return {"query": query}

def make_dept(result):
    # ES 검색 결과를 부서 리스트로 변환
    return [
        {
            "dno": hit["_source"].get("dno"),
            "dname": hit["_source"].get("dname"),
            "loc": hit["_source"].get("loc"),
        }
        for hit in result["hits"]["hits"]
    ]

# 참고)
# CREATE
@bp.route("/dept", methods=["POST"])
def insert():
    data = request.json
    dname = data.get("dname")
    loc = data.get("loc")

    if not dname or not loc:
        return jsonify({"error": "dname and loc are required"}), 400

    # dno는 유일한 값 넣기: 시간 정수부분 넣기
    dno = int(time.time())

    dept = {"dno": dno, "dname": dname, "loc": loc}
    es.index(index=INDEX_NAME, id=dno, document=dept)
    return Response(status=201)

# UPDATE
@bp.route("/dept", methods=["PUT"])
def update():
    dno = request.args.get("dno")
    if not dno:
        return jsonify({"error": "dno query parameter is required"}), 400

    # 기존 문서 확인
    if not es.exists(index=INDEX_NAME, id=dno):
        return jsonify({"error": "Dept not found"}), 404

    data = request.json
    es.update(index=INDEX_NAME, id=dno, doc={"doc": data})
    return Response(status=200)

# DELETE
@bp.route("/dept", methods=["DELETE"])
def delete():
    dno = request.args.get("dno")
    if not dno:
        return jsonify({"error": "dno query parameter is required"}), 400

    if not es.exists(index=INDEX_NAME, id=dno):
        return jsonify({"error": "Dept not found"}), 404

    es.delete(index=INDEX_NAME, id=dno)
    return Response(status=200)
