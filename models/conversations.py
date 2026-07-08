from database import db
from datetime import datetime

class Conversations(db.Model):
    __tablename__="conversations"

    id= db.Column(db.Integer,primary_key =True)
    created_at = db.Column(db.Datetime,default=datetime.utcnow)