from models import db

class Preferences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    voice = db.Column(db.String(50))
    speed = db.Column(db.Integer)