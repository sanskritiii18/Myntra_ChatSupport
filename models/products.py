from database import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = "productpy"
    id = db.Column(db.Integer,primary_key=True)
    name =  db.Column(db.String(100),unique=True,nullable=False)
    description = db.Column(db.String(200))
    price = db.Column(db.Integer,nullable = False)
    discount = db.Column(db.Integer)
    brand = db.Column(db.String(100))
    category = db.Column(db.String(50))
    stock = db.Column(db.Integer)
    image_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
