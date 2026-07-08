from models.friend import Friend
from models.user import Users
from routes.frontend_routes import get_current_user
from sqlalchemy import or_


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




def send_friend_request(email,username):
    pass

def accept_friend_request():
    pass

def decline_friend_request():
    pass

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



def get_pending_requests(): pass


