from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ READ (전체 조회)
@app.route('/books', methods=['GET'])
def getAll():
    # DB가 없으므로 가라데이터 return
    books = [
        {"id": 1, "title": "파이썬 입문"},
        {"id": 2, "title": "AI 기초"}
    ]
    return jsonify(books),200

# ✅ READ (한 개 조회)
@app.route('/books/one', methods=['GET'])
def get():
    id = request.args.get('id', type=int)  # 쿼리스트링에서 id 받아오기
    return jsonify({"id": id}), 200

# ✅ CREATE (책 추가)
@app.route('/books/add', methods=['POST'])
def insert():
    data = request.json                   # json 데이터 받기
    app.logger.info(data)
    return '추가',200

# ✅ UPDATE (책 제목 수정)
@app.route('/books/edit', methods=['PUT'])
def update():
    id = request.args.get('id', type=int)  # 쿼리스트링에서 id 받아오기
    data = request.json
    app.logger.info(f"id: {id}, data: {data}")
    return '수정',200

# ✅ DELETE (책 삭제)
@app.route('/books/delete', methods=['DELETE'])
def delete_book():
    id = request.args.get('id', type=int)  # 쿼리스트링에서 id 받아오기
    app.logger.info(id)
    return '삭제',200

if __name__ == '__main__':
    # TODO: 파이썬 내장 서버 사용(Tomcat 과 비슷)
    app.run(debug=True, host='0.0.0.0', port=5000) # 원격으로 접속 허용: python b_flask.py 실행
