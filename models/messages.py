from database import db
from datetime import datetime

class Message(db.Model):
    __tablename__="messages"

    id = db.Column(db.Integer ,  primary_key=True)
    conversation_id = db.Column(db.Integer,db.ForeignKey("conversations.id"),nullable = False)
    sender_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable = False)
    product_id = db.Column(db.Integer,db.ForeignKey("productpy.id"))
    message_type= db.Column(db.String(64))
    text = db.Column(db.String(200))
    reaction_type =db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    sender = db.relationship("User")
    conversation = db.relationship("Conversations")
    product = db.relationship("Product")

