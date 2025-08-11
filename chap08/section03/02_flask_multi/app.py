from flask import Flask
from dept_route import bp as dept
from dept2_route import bp as dept2

app = Flask(__name__)

# 라우트 등록
app.register_blueprint(dept)
app.register_blueprint(dept2)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
