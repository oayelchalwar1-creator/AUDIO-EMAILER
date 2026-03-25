from flask import Blueprint, render_template, request
from services.email_service import fetch_emails
from services.audio_service import speak_text

email_bp = Blueprint("email", __name__)

@email_bp.route("/inbox")
def inbox():
    emails = fetch_emails()
    return render_template("inbox.html", emails=emails)


@email_bp.route("/speak", methods=["POST"])
def speak():
    content = request.form["content"]
    speak_text(content)
    return "Speaking..."