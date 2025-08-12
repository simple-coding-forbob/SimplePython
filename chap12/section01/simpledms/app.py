from flask import Flask
from dept_route import bp as dept
from emp_route import bp as emp

app = Flask(__name__)

# 라우트 등록
app.register_blueprint(dept)
app.register_blueprint(emp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
