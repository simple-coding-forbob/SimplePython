from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# 로그 설정
logging.basicConfig(level=logging.INFO)

# ✅ READ (전체 조회)
@app.route('/quiz', methods=['GET'])
def getAll():
    # DB가 없으므로 가라데이터 return
    books = [
        {"id": 1, "title": "자바 입문"},
        {"id": 2, "title": "스프링 기초"}
    ]
    return jsonify(books),200

# ✅ READ (한 개 조회)
@app.route('/quiz/one', methods=['GET'])
def get():
    id = request.args.get('id', type=int)  # 쿼리스트링에서 id 받아오기
    return jsonify({"id": id}), 200

# ✅ CREATE (책 추가)
@app.route('/quiz/add', methods=['POST'])
def insert():
    data = request.json                   # json 데이터 받기
    app.logger.info(data)
    return '',200

# ✅ UPDATE (책 제목 수정)
@app.route('/quiz/edit', methods=['PUT'])
def update():
    id = request.args.get('id', type=int)  # 쿼리스트링에서 id 받아오기
    data = request.json
    app.logger.info(f"id: {id}, data: {data}")
    return '',200

# ✅ DELETE (책 삭제)
@app.route('/quiz/delete', methods=['DELETE'])
def delete_book():
    id = request.args.get('id', type=int)  # 쿼리스트링에서 id 받아오기
    app.logger.info(id)
    return '',200

if __name__ == '__main__':
    # TODO: 파이썬 내장 서버 사용(Tomcat 과 비슷)
    app.run(debug=True, host='0.0.0.0', port=5000) # 원격으로 접속 허용: python b_flask.py 실행
