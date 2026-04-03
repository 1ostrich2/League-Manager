from flask_sqlalchemy import SQLAlchemy
from flask_login.mixins import UserMixin

db = SQLAlchemy()

class user_model(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(18), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), unique=False, nullable=False)
    
    competitions = db.relationship("competition_model", backref="user_model")
    
    def get_id(self):
        return self.user_id

class competition_model(db.Model):
    competition_id = db.Column(db.Integer, primary_key=True, nullable=False)
    competition_name = db.Column(db.String(), nullable=False)
    private = db.Column(db.Boolean, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey("user_model.user_id"))
    
    teams = db.relationship("team_model", backref="competition_model")
    stages = db.relationship("stage_model", backref="competition_model")

class stage_model(db.Model):
    stage_id = db.Column(db.Integer, primary_key=True, nullable=False)
    
    competition_id = db.Column(db.Integer, db.ForeignKey("competition_model.competition_id"))
    competition_format = db.Column(db.String(), nullable=False)


class team_model(db.Model):
    team_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(18), nullable=False)
    
    competition_id = db.Column(db.Integer, db.ForeignKey("competition_model.competition_id"))