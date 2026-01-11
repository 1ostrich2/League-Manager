from flask import render_template, redirect, flash, url_for
from Website.main import app
from Website.models import db, user_model
from Website.forms import LoginForm, RegisterForm
import flask_login
from flask_login import login_required, login_user, logout_user
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError

# Intitializing Bcrypt
bcrypt = Bcrypt(app)

# Initializing the database
db.init_app(app)
with app.app_context():
    db.create_all()

# Intitializing the login manager
login_manager = flask_login.LoginManager()
login_manager.login_view = '/login'
login_manager.init_app(app)

@login_manager.user_loader
def user_loader(_id):
    user = db.session.execute(db.select(user_model).filter_by(user_id=_id))
    return user

@app.route('/')
@app.route('/home')
def home():
    return render_template('public//home.html', current_user=flask_login.current_user)

@login_required
@app.route('/dashboard')
def dashboard():
    return render_template('public//dashboard.html', current_user=flask_login.current_user)

@app.route('/register', methods=["GET", "POST"])
def register():
    registerform = RegisterForm()

    if registerform.validate_on_submit():
        username = registerform.data["username"]
        email = registerform.data["email"]
        password = registerform.data["password"]

        hashed_password = bcrypt.generate_password_hash(password)
        new_user = user_model(username=username, email=email, password=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()

        except IntegrityError as error:
            if "username" in str(error.orig): #error.orig is the first line in error --- for example: "UNIQUE constraint failed user_model.username"
                flash('Username already taken', category="warning")
                return redirect(url_for('register'))
            
            if "email" in str(error.orig):
                flash('The provided email is already registered. Please login instead.', category="warning")
                return redirect(url_for('register'))

        flash('Registration succesful. Please login now.', category="success")
        return redirect(url_for('login'))

    return render_template('auth//register.html', form=registerform, current_user=flask_login.current_user)


@app.route('/login', methods=["GET", "POST"])
def login():
    loginform = LoginForm()

    if loginform.validate_on_submit():
        email = loginform.data["email"]
        password = loginform.data["password"]

        fetched_user = db.session.execute(db.select(user_model).filter_by(email=email)).scalar_one()
        
        if fetched_user:
            checkPassword = bcrypt.check_password_hash(pw_hash=fetched_user.password, password=password)
            
            if checkPassword:
                login_user(fetched_user)
                flash('Login succesful.', category="success")
                return redirect(url_for('dashboard'))

        else:
            flash('An account with this email is not yet registered. Please register first.', category="warning")
            return redirect(url_for('login'))

    return render_template('auth//login.html', form=loginform, current_user=flask_login.current_user)


@login_required
@app.route('/logout')
def logout():
    logout_user()
    print("hi")
    return redirect(url_for('home'))