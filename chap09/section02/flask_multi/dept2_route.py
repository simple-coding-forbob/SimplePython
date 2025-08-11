from flask import Blueprint, jsonify

# __name__ : 현재 파일의 이름
dept2 = Blueprint("dept2", __name__)

# ✅ READ (전체 조회)
@dept2.route('/dept2', methods=['GET'])
def getAll():
    # DB가 없으므로 가라데이터 return
    depts = [
        {"dno": 10, "dname": "개발부2"},
        {"dno": 20, "dname": "영업부2"}
    ]
    return jsonify(depts),200
