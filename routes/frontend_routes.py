from flask import Blueprint, render_template,request,redirect,url_for
from models.products import Product
from utils.jwt_handler import verify_token
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
        return redirect(url_for("services.login"))

    return render_template(
        "profile.html",
        user=user
    )


@frontend_bp.route("/mens",methods=["GET"])
def mens():
    return render_template("mens.html")


@frontend_bp.route("/products",methods=["GET"])
def products():
    products = Product.query.all()
    return render_template("products.html", products=products)

@frontend_bp.route("/bag",methods=["GET"])
def bag():
    return render_template("bag.html")

@frontend_bp.route("/wishlist",methods=["GET"])
def wishlist():
    return render_template("wishlist.html")

@frontend_bp.route("/address",methods=["GET"])
def address():
    return render_template("address.html")



@frontend_bp.route("/product/<int:product_id>")
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("product_detail.html", product=product)






