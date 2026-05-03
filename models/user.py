from database import db
from datetime import datetime

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(64),unique=True,nullable=False)
    user_name = db.Column(db.String(64), unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    phone_number = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(120),nullable=False)
    birth_of_date = db.Column(db.DateTime,default=datetime.utcnow)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)










