from flask import render_template, redirect,url_for
from auth.jwt_handler import create_token
from models.user import Users
from database import db
from sqlalchemy import or_

def login_user(phone_number ,password):
    user = Users.query.filter_by(phone_number=phone_number).first()

    if not user:
        return render_template(
            "login.html",
            error="User doesn't exist"
        )

    if password != user.password:
        return render_template("login.html", error="Wrong password")

    token = create_token(user.id)
    response = redirect(url_for("frontend.home"))

    # store JWT in browser cookie
    response.set_cookie("token", token)

    return response


def sign_user(name,username,email,phone_number ,password,birth_of_date):
    new_user= Users(
        name = name,
        user_name = username,
        email = email,
        phone_number = phone_number,
        password = password,
        birth_of_date = birth_of_date
    )
    existing_user = Users.query.filter(or_(Users.email==email,Users.phone_number == phone_number,Users.user_name==username)).first()
    if existing_user:
        return render_template("login.html",error="User already exists")

    db.session.add(new_user)
    db.session.commit()
    return render_template("login.html")
