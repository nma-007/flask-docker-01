"""Initialize Flask app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.api import api

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    app.register_blueprint(api)
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    with app.app_context():
        from . import routes, models #import py definitions inside folder app

        db.create_all()  # Create database tables for our data models
        
        return app