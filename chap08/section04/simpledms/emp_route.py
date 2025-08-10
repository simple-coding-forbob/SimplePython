from flask import Blueprint, request, jsonify, Response
from config import db
from emp import Emp  # Employee ORM 클래스

bp = Blueprint("employee", __name__)

# LIKE 검색 (ename 기준)
@bp.route("/emp/search", methods=["GET"])
def search_employees():
    keyword = request.args.get("keyword", "")
    like_pattern = f"%{keyword}%"
    sql = "SELECT * FROM TB_EMP WHERE ename LIKE :pattern ORDER BY eno"
    result = db.engine.execute(sql, {"pattern": like_pattern})
    emps = [{"eno": row[0], "ename": row[1], "job": row[2], "salary": row[3], "dno": row[4]} for row in result]
    return jsonify(emps)

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

    seq_sql = "SELECT EMPLOYEE_SEQ.NEXTVAL FROM DUAL"
    seq_result = db.engine.execute(seq_sql)
    eno = seq_result.fetchone()[0]

    emp = Emp(eno=eno, ename=ename, job=job, salary=salary, dno=dno)
    db.session.add(emp)
    db.session.commit()
    return Response(status=201)

# UPDATE (쿼리스트링 eno)
@bp.route("/emp", methods=["PUT"])
def update():
    eno = request.args.get("eno", type=int)
    if eno is None:
        return jsonify({"error": "eno query parameter is required"}), 400

    data = request.json
    ename = data.get("ename")
    job = data.get("job")
    salary = data.get("salary")
    dno = data.get("dno")

    emp = Emp.query.get(eno)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404

    if ename is not None:
        emp.ename = ename
    if job is not None:
        emp.job = job
    if salary is not None:
        emp.salary = salary
    if dno is not None:
        emp.dno = dno

    db.session.commit()
    return Response(status=200)

# DELETE (쿼리스트링 eno)
@bp.route("/emp", methods=["DELETE"])
def delete():
    eno = request.args.get("eno", type=int)
    if eno is None:
        return jsonify({"error": "eno query parameter is required"}), 400

    emp = Emp.query.get(eno)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404
    db.session.delete(emp)
    db.session.commit()
    return Response(status=200)
