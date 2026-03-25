from flask import Blueprint, render_template, request, redirect, session
from app import db
from models.preference_model import Preference
from models.user_model import User

preferences_blueprint = Blueprint("preferences", __name__)


@preferences_blueprint.route("/preferences")
def preferences_page():

    email = session.get("email")

    if not email:
        return redirect("/")

    user = User.query.filter_by(email=email).first()

    pref = Preference.query.filter_by(user_id=user.id).first()

    return render_template(
        "preferences.html",
        pref=pref
    )


@preferences_blueprint.route("/preferences/save", methods=["POST"])
def save_preferences():

    email = session.get("email")
    user = User.query.filter_by(email=email).first()

    voice = request.form["voice"]
    speed = request.form["speed"]
    pause = request.form["pause"]
    theme = request.form["theme"]

    pref = Preference.query.filter_by(user_id=user.id).first()

    if pref is None:
        pref = Preference(
            user_id=user.id,
            voice=voice,
            speed=speed,
            pause=pause,
            theme=theme
        )
        db.session.add(pref)

    else:
        pref.voice = voice
        pref.speed = speed
        pref.pause = pause
        pref.theme = theme

    db.session.commit()

    return redirect("/inbox")