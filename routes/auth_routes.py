
from flask import Blueprint, render_template,request
from auth.auth_service import login_user, sign_user

auth_bp = Blueprint("auth",__name__)


@auth_bp.route("/login",methods=["GET","POST"])
def login():
    if request.method =="POST":
        phone_number = request.form.get("mobileno")
        password = request.form.get("password")

        response= login_user(phone_number,password)

        return response

    return  render_template("login.html")


@auth_bp.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        email = request.form.get("email")
        phone_number =  request.form.get("mobileno")
        password = request.form.get("password")
        birth_of_date = request.form.get("birthdate")

        response = sign_user(name,username,email,phone_number,password,birth_of_date)
        return response

    return render_template("signin.html")

