from flask import Flask, request, jsonify
import logging
import a_recommend

app = Flask(__name__)

# 로그 설정
logging.basicConfig(level=logging.INFO)

# ✅ READ (한 개 조회)
@app.route('/recommend', methods=['GET'])
def get():
    user = request.args.get('user')  # 쿼리스트링에서 user 받아오기

    if not user:
        return jsonify({"에러": "유저가 없습니다."}), 400

    try:
        recommend=a_recommend.recommend(user)
        return jsonify({"user": user, "recommend": recommend})
    except Exception as e:
        logging.error(e)

if __name__ == '__main__':
    # TODO: 파이썬 내장 서버 사용(Tomcat 과 비슷)
    app.run(debug=True, host='0.0.0.0', port=5000) # 원격으로 접속 허용: python b_flask.py 실행
