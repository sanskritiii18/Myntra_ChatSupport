from flask import Blueprint , render_template,request,redirect,url_for
from routes.frontend_routes import get_current_user
from services.friend_service import get_friend_list, get_pending_requests, search_users, send_friend_request, \
    accept_friend_request,decline_friend_request

friends_bp = Blueprint("friends",__name__)

@friends_bp.route("/friends",methods=["GET"])
def friends():
    current_user = get_current_user()
    if not current_user:
        return "Login first"
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



@friends_bp.route("/friends/request",methods=["POST"])
def send_friend_request_route():
    friend_id = request.form.get("friend_id")
    friend_id = int(friend_id)
    result = send_friend_request(friend_id)
    if result == "friend_not_found":
        return render_template(
            "search_results.html",
            error="User doesn't exist."
        )
    if result == "already_exists":
        return render_template(
            "search_results.html",
            error="Friend request already exists."
        )
    if result == "cannot_add_self":
        return render_template(
            "search_results.html"
        )
    return redirect(url_for("friends.friends"))



@friends_bp.route("/friends/accept",methods=["POST"])
def accept_friend_request_route():
    request_id = int(request.form.get("friendship_id"))
    result = accept_friend_request(request_id)
    if result:
        return redirect(url_for("friends.friends"))
    else:
        return "Unable to accept request"


@friends_bp.route("/friends/decline",methods=["POST"])
def decline_friend_request_route():
    request_id = int(request.form.get("friendship_id"))
    result = decline_friend_request(request_id)
    if result:
        return redirect(url_for("friends.friends"))
    else:
        return "Unable to decline request"


