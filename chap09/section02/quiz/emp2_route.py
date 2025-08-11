from flask import Blueprint, jsonify

# __name__ : 현재 파일의 이름
bp = Blueprint("emp", __name__)

# ✅ READ (전체 조회)
@bp.route('/emp2', methods=['GET'])
def getAll():
    # DB가 없으므로 가라데이터 return
    emps = [
        {"eno": 8000, "ename": "홍길동2"},
        {"eno": 8001, "ename": "장길산2"}
    ]
    return jsonify(emps),200
