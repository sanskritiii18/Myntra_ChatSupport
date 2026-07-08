from sqlalchemy import UniqueConstraint

from database import db
from datetime import datetime



class ConversationParticipants(db.Model):
    __tablename__ = "conversationparticipants"

    __table_args__=(
        UniqueConstraint(
            "user_id",
            "conversation_id",
            name="uq_conversation_participant"

        ),
    )

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable =False)
    conversation_id = db.Column(db.Integer,db.ForeignKey("conversations.id"),nullable=False)
    joined_at = db.Column(db.DateTime,default=datetime.utcnow)

    user = db.relationship("User")
    conversation = db.relationship("Conversations")
