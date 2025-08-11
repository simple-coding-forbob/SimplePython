from flask import Blueprint, request, jsonify
import logging
import rec

# __name__ : 현재 파일의 이름
book = Blueprint("book", __name__)

# ✅ READ (한 개 조회)
@book.route('/recommend', methods=['GET'])
def get():
    user = request.args.get('user')  # 쿼리스트링에서 user 받아오기

    if not user:
        return jsonify({"에러": "유저가 없습니다."}), 400

    try:
        recommend= rec.recommend(user)
        return jsonify({"user": user, "recommend": recommend})
    except Exception as e:
        logging.error(e)
