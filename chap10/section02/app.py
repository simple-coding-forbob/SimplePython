from flask import Flask
from book_rec import book

app = Flask(__name__)

# 라우트 등록
app.register_blueprint(book)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
