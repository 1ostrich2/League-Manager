import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-password-1357902468'

