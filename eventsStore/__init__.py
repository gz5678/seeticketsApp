import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("../config.py")

    db.init_app(app)
    from eventsStore.models import Products, Events, association_table

    with app.app_context():
        db.create_all()

    return app