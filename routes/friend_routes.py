
from flask import Blueprint , render_template,request,redirect,url_for

from services.friend_service import get_friend_list, get_pending_requests, search_users

friends_bp = Blueprint("friends",__name__)

@friends_bp.route("/friends",methods=["GET"])
def friends():
    friends = get_friend_list()
    pending_request = get_pending_requests()

    return render_template("friends.html",
                           friends = friends,pending_request=pending_request)



@friends_bp.route("/friends/search",methods =['GET'])
def search():
    query = request.args.get("query")
    if not query:
        return "Search query is required", 400
    result_search = search_users(query)
    return render_template("search_results.html",result_search = result_search)


"""
@friends_bp.route("/friends/request",methods=["POST"])
def send_friend_request():
    email = request.form.get('email')
    #search button
    friend = Users.query.filter_by(email=email)
    if not friend:
        return  render_template(
            "friends.html",
            error ="User doesnt exits")
if friend.status == "Pending":
        return error='request already sent'

    friend.status = "Pending"
   

"""









