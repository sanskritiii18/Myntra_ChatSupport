from http.client import responses
from pyexpat.errors import messages
import string
from werkzeug.security import generate_password_hash, check_password_hash
from flask import render_template, redirect,url_for,request
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

    if not check_password_hash(user.password, password):
        return render_template(
            "login.html",
            error="Wrong password"
        )

    token = create_token(user.id)
    response = redirect(url_for("frontend.home"))

    # store JWT in browser cookie
    response.set_cookie("token", token)

    return response

def logout_user():
    token = request.cookies.get("token")
    response = redirect(url_for("frontend.home"))
    response.delete_cookie("token",token)
    return response

def sign_user(name,username,email,phone_number ,password,birth_of_date):

    existing_user = Users.query.filter(
        or_(Users.email == email, Users.phone_number == phone_number, Users.user_name == username)).first()
    if existing_user:
        return render_template("login.html", error="User already exists")


    # Password strength validation
    if len(password) < 8:
        return render_template(
            "signin.html",
            error="Weak password, minimum 8 characters"
        )


    elif not any(char.isupper() for char in password):

        return render_template(

            "signin.html",

            error="Password must contain at least one uppercase letter"

        )


    elif not any(char.islower() for char in password):

        return render_template(

            "signin.html",

            error="Password must contain at least one lowercase letter"

        )


    elif not any(char.isdigit() for char in password):

        return render_template(

            "signin.html",

            error="Password must contain at least one number"

        )


    elif not any(char in string.punctuation for char in password):

        return render_template(

            "signin.html",

            error="Password must contain at least one special character"

        )


    else:

        message = "Strong Password"

    hashed_password = generate_password_hash(password)
    new_user= Users(
        name = name,
        user_name = username,
        email = email,
        phone_number = phone_number,
        password = hashed_password,
        birth_of_date = birth_of_date
    )

    db.session.add(new_user)
    db.session.commit()

    return render_template(
        "login.html",
        success="Account created successfully",
        password_strength=message
    )
