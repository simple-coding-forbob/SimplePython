from config import db

class Emp(db.Model):
    __tablename__ = "TB_EMP"
    eno = db.Column(db.Integer, primary_key=True)
    ename = db.Column(db.String(50))
    job = db.Column(db.String(50))
    salary = db.Column(db.Integer)
    dno = db.Column(db.Integer)
