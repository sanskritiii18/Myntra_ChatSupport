from enum import unique

from database import db

class Users(db.Model):
    id = db.Column(db.Integer ,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    user_name = db.Column(db.String(64), unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    Phone_number = db.Column(db.Integer(10), unique=True)
    password = db.Column(db.String(120),nullable=False)
    birth_of_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)










