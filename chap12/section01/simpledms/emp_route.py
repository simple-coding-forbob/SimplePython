from flask import Blueprint, request, jsonify, Response
from elasticsearch import Elasticsearch
import time

# ES 연결
# ES 연결
es = Elasticsearch(
    ["https://localhost:9200"],
    basic_auth=("elastic", "=U5oxindf+JStU2U25mT"),
    verify_certs=False
)
INDEX_NAME = "employee"

bp = Blueprint("emp", __name__)

# LIKE 검색 (ename 기준)
@bp.route("/emp/search", methods=["GET"])
def search_employees():
    keyword = request.args.get("keyword", "")
    body = search_keyword(keyword)
    result = es.search(index=INDEX_NAME, body=body)
    return jsonify(make_emp(result))

def search_keyword(keyword: str):
    # 검색어에 맞는 Elasticsearch 쿼리 생성
    query = {"match_all": {}} if not keyword else {"match_phrase": {"ename": keyword}}
    return {"query": query}

def make_emp(result):
    return [
        {
            "eno": hit["_source"].get("eno"),
            "ename": hit["_source"].get("ename"),
            "job": hit["_source"].get("job"),
            "salary": hit["_source"].get("salary"),
            "dno": hit["_source"].get("dno"),
        }
        for hit in result["hits"]["hits"]
    ]

# 참고)
# CREATE
@bp.route("/emp", methods=["POST"])
def insert():
    data = request.json
    ename = data.get("ename")
    job = data.get("job")
    salary = data.get("salary")
    dno = data.get("dno")

    if not ename or not job or salary is None or dno is None:
        return jsonify({"error": "ename, job, salary, dno are required"}), 400

    # eno를 유일한 값 넣기: 시간 정수부분 넣기
    eno = int(time.time())

    doc = {
        "eno": eno,
        "ename": ename,
        "job": job,
        "salary": salary,
        "dno": dno
    }
    es.index(index=INDEX_NAME, id=eno, document=doc)
    return Response(status=201)

# UPDATE (쿼리스트링 eno)
@bp.route("/emp", methods=["PUT"])
def update():
    eno = request.args.get("eno")
    if not eno:
        return jsonify({"error": "eno query parameter is required"}), 400

    if not es.exists(index=INDEX_NAME, id=eno):
        return jsonify({"error": "Employee not found"}), 404

    data = request.json
    es.update(index=INDEX_NAME, id=eno, doc={"doc": data})
    return Response(status=200)

# DELETE (쿼리스트링 eno)
@bp.route("/emp", methods=["DELETE"])
def delete():
    eno = request.args.get("eno")
    if not eno:
        return jsonify({"error": "eno query parameter is required"}), 400

    if not es.exists(index=INDEX_NAME, id=eno):
        return jsonify({"error": "Employee not found"}), 404

    es.delete(index=INDEX_NAME, id=eno)
    return Response(status=200)
