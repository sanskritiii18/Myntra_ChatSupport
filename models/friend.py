from sqlalchemy import UniqueConstraint
from database import db
from datetime import datetime

class Friend(db.Model):
    __tablename__="friends"

    __table_args__=(

        UniqueConstraint(
            "user_id",
            "friend_user_id",
            name="uq_friendship_pair"
        ),
    )

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    friend_user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    request_by = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
    status = db.Column(db.String(64),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)

    user = db.relationship("Users",foreign_keys=[user_id])
    friend_user = db.relationship("Users",foreign_keys=[friend_user_id])
    request_sender = db.relationship("Users",foreign_keys=[request_by])

