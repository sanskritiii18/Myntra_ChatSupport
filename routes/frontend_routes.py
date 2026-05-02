import os
from crypt import methods

from flask import Blueprint, render_template



frontend_bp = Blueprint("frontend",__name__)

# homepage
@frontend_bp.route("/home",methods=["GET"])
def home():
    return render_template("home.html")


@frontend_bp.route("/mens",methods=["GET"])
def mens():
    return render_template("mens.html")


@frontend_bp.route("/products",methods=["GET"])
def products():
    return render_template("products.html")





