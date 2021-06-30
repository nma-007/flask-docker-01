"""Flask configuration variables."""
import os
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config:
    """Set Flask configuration from .env file."""
    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    FLASK_PORT = environ.get('FLASK_PORT')
    STATIC_FOLDER =  environ.get('static')
    TEMPLATES_FOLDER =  environ.get('templates')
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    
    # Database cfg
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True