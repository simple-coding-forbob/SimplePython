from flask import Blueprint, request, jsonify, Response
from config import db
from dept import Dept

# __name__ : 현재 파일의 이름
bp = Blueprint("dept", __name__)

# LIKE 검색 (dname 기준, SQL 직접 실행)
@bp.route("/dept/search", methods=["GET"])
def select_all():
    keyword = request.args.get("keyword", "")
    like_pattern = f"%{keyword}%"

    sql = "SELECT * FROM TB_DEPT WHERE dname LIKE :pattern"
    result = db.engine.execute(sql, {"pattern": like_pattern})

    depts = [{"dno": row[0], "dname": row[1], "loc": row[2]} for row in result]
    return jsonify(depts)

# CREATE
@bp.route("/dept", methods=["POST"])
def insert():
    data = request.json
    dname = data.get("dname")
    loc = data.get("loc")

    if not dname or not loc:
        return jsonify({"error": "dname and loc are required"}), 400

    # 시퀀스 활용하여 dno 수동 할당
    seq_sql = "SELECT DEPARTMENT_SEQ.NEXTVAL FROM DUAL"
    seq_result = db.engine.execute(seq_sql)
    dno = seq_result.fetchone()[0]

    dept = Dept(dno=dno, dname=dname, loc=loc)
    db.session.add(dept)
    db.session.commit()
    return Response(status=201)

# UPDATE
@bp.route("/dept", methods=["PUT"])
def update():
    dno = request.args.get("dno", type=int)
    if dno is None:
        return jsonify({"error": "dno query parameter is required"}), 400

    data = request.json
    dname = data.get("dname")
    loc = data.get("loc")

    dept = Dept.query.get(dno)
    if not dept:
        return jsonify({"error": "Dept not found"}), 404

    if dname is not None:
        dept.dname = dname
    if loc is not None:
        dept.loc = loc

    db.session.commit()
    return Response(status=200)

# DELETE
@bp.route("/dept", methods=["DELETE"])
def delete():
    dno = request.args.get("dno", type=int)
    if dno is None:
        return jsonify({"error": "dno query parameter is required"}), 400

    dept = Dept.query.get(dno)
    if not dept:
        return jsonify({"error": "Dept not found"}), 404
    db.session.delete(dept)
    db.session.commit()
    return Response(status=200)
