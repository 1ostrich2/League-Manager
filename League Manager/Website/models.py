from flask_sqlalchemy import SQLAlchemy
from flask_login.mixins import UserMixin

db = SQLAlchemy()

class user_model(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(18), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), unique=False, nullable=False)
    
    def get_id(self):
        return self.user_id

