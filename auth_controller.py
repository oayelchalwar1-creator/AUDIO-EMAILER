from flask import Blueprint, render_template, request, redirect
from models.user_model import User
from models import db
import bcrypt

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def login_page():
    return render_template("login.html")


@auth_bp.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    user = User.query.filter_by(email=email).first()

    if user and bcrypt.checkpw(password.encode(), user.password.encode()):
        return redirect("/inbox")

    return "Invalid Login"