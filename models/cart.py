from database import db
from datetime import datetime

class Cart(db.Model):
    __tablename__ = "cart"
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.ForeignKey("users.id"),nullable=False)
    total = db.Column(db.Integer)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow)

class CartItems(db.Model):
    __tablename__ = "cart_items"
    id = db.Column(db.Integer,primary_key=True)
    cart_id = db.Column(db.ForeignKey("cart.id"))
    product_id = db.Column(db.ForeignKey("product.id"))
    quantity = db.Column(db.Integer,nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,default=datetime.utcnow)