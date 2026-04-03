from flask import Flask
from Website.config import Config

app = Flask(__name__, template_folder='templates')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config.from_object(Config)

