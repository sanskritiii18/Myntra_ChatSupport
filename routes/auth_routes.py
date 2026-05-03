from crypt import methods

from flask import Blueprint, render_template,request
from models.user import Users
from database import db

auth_bp = Blueprint("auth",__name__)


@auth_bp.route("/login",methods=["GET","POST"])
def login():
    if request.method =="POST":
        phone_number = request.form.get("mobileno")
        password = request.form.get("password")

        user = Users.query.filter_by(phone_number=phone_number).first()

        if not user:
            return "User doesnt exist"


        if password == user.password:
            return render_template("home.html")
        else:
            return "Wrong password"



    return render_template("login.html")


@auth_bp.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        email = request.form.get("email")
        phone_number =  request.form.get("mobileno")
        password = request.form.get("password")
        birth_of_date = request.form.get("birthdate")

        new_user=Users(
            name = name,
            user_name = username,
            email=email,
            phone_number = phone_number,
            password = password,
            birth_of_date = birth_of_date

        )

        db.session.add(new_user)
        db.session.commit()
        return render_template("login.html")



    return render_template("signin.html")

