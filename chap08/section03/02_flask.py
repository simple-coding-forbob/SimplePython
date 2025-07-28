from flask import Flask, jsonify, request

app = Flask(__name__)

# 기본 라우팅
@app.route('/')
def home():
    return "Hello, this is a simple Flask API!"

# 숫자 입력받아 제곱값 반환하는 예제
@app.route('/square', methods=['POST'])
def square():
    # JSON 형식으로 데이터 받기
    data = request.get_json()
    number = data.get('number')

    if number is None:
        return jsonify({'error': 'Number is required'}), 400

    # 숫자 제곱 계산
    result = number ** 2

    # 결과 반환
    return jsonify({'number': number, 'square': result})

if __name__ == '__main__':
    app.run(debug=True)