from flask import Flask
from emp2_route import bp as emp2
from emp_route import bp as emp

app = Flask(__name__)

# 라우트 등록
app.register_blueprint(emp)
app.register_blueprint(emp2)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
