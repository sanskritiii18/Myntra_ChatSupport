
from flask import Blueprint, render_template,request,redirect,url_for

from auth.jwt_handler import verify_token
from models.user import Users

frontend_bp = Blueprint("frontend",__name__)

def get_current_user():

    token = request.cookies.get("token")

    if not token:
        return None

    user_id = verify_token(token)

    if not user_id:
        return None

    user = Users.query.get(user_id)

    return user
# homepage
@frontend_bp.route("/",methods=["GET"])
def home():
    return render_template("home.html")


@frontend_bp.route("/profile")
def profile():

    user = get_current_user()

    if not user:
        return redirect(url_for("auth.login"))

    return render_template(
        "profile.html",
        user=user
    )


@frontend_bp.route("/mens",methods=["GET"])
def mens():
    return render_template("mens.html")


@frontend_bp.route("/products",methods=["GET"])
def products():
    return render_template("products.html")





