from crypt import methods

from flask import Blueprint, render_template

auth_bp = Blueprint("auth",__name__)


@auth_bp.route("/login",methods=["GET"])
def login():
    return render_template("login.html")


@auth_bp.route("/signin",methods=["POST"])
def login():
    return render_template("login.html")

@auth_bp.route("/signin", methods=["GET"])
def signin():
    return render_template("signin.html")



