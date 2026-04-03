from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, EmailField, SubmitField, StringField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    remember_me = BooleanField(label="Remember Me")
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(min=5,max=18)])
    email = EmailField(label="Email", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField(label="Repeat Password", validators=[DataRequired(), EqualTo('password', message="Passwords must match")])
    submit = SubmitField('Register')

class CreateCompetitionForm(FlaskForm):
    competition_name = StringField(label="Competition Name", validators=[DataRequired(), Length(min=1, max=20)])
    private = BooleanField(label="Private?")
    submit = SubmitField("Create")

