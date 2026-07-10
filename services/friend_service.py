from flask import render_template
from sqlalchemy.testing.exclusions import succeeds_if
from sqlalchemy.testing.suite.test_reflection import users

from models.friend import Friend
from models.user import Users
from routes.frontend_routes import get_current_user
from database import db
from sqlalchemy import or_, and_, false


def search_users(query):
    current_user = get_current_user()
    if query == current_user.user_name or query == current_user.email:
        return None

    search_term = f"%{query}%"

    result = Users.query.filter(
        or_(
            Users.user_name.ilike(search_term),
            Users.email.ilike(search_term)
        )
    ).all()
    print(result)
    return result




def send_friend_request(friend_id):
    current_user = get_current_user()
    if current_user is None:
        return "no current user"
    if current_user.id == friend_id:
        return "cannot_add_self"
    check_user = Users.query.filter_by(id=friend_id).first()
    if not check_user:
        return "friend_not_found"
    sender_id = current_user.id
    receiver_id = check_user.id
    user_id = min(sender_id,receiver_id)
    friend_user_id = max(sender_id,receiver_id)

    existing_friendship = Friend.query.filter(
        and_(
            Friend.user_id == user_id,
            Friend.friend_user_id == friend_user_id
        )
    ).first()
    if existing_friendship:
        return "already_exists"


    new_friendship = Friend(
        user_id=user_id,
        friend_user_id=friend_user_id,
        request_by=current_user.id,
        status="pending"
    )

    db.session.add(new_friendship)
    db.session.commit()


    return "success"



def accept_friend_request(request_id):
    find_friendship = Friend.query.filter_by(id=request_id).first()
    if find_friendship and find_friendship.status == "pending":
        find_friendship.status = "accepted"
        db.session.commit()
        return True
    else:
        return "friendship_not_found"



def decline_friend_request(request_id):
    find_friendship = Friend.query.filter_by(id=request_id).first()
    if find_friendship and find_friendship.status == "pending":
        db.session.delete(find_friendship)
        db.session.commit()
        return True
    else:
        return "friendship_not_found"




def get_friend_list():
    current_user = get_current_user()
    friend = Friend.query.all()
    return_friends_list = []
    for fr in friend:
        if fr not in friend:
            return #no friends yet
        if fr.user_id == current_user.id:
            return_friends_list.append(fr.friend_user_id)
        elif fr.friend_user_id == current_user.id:
            return_friends_list.append(fr.user_id)



def get_pending_requests():
    current_user = get_current_user()
    result = Friend.query.filter(
        or_(
            Friend.user_id == current_user.id,
            Friend.friend_user_id == current_user.id
        )
    ).all()
    pending_request=[]
    for friendship in result:
        if friendship.request_by != current_user.id and friendship.status == "pending":
            pending_request.append(friendship)

    return pending_request







