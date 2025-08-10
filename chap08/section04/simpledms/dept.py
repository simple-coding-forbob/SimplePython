from config import db

class Dept(db.Model):
    __tablename__ = "TB_DEPT"
    dno = db.Column(db.Integer, primary_key=True)
    dname = db.Column(db.String(250))
    loc = db.Column(db.String(250))
