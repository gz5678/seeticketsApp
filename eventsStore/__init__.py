import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def create_app(test_config=None):
    """
    App factory for the flask app
    :param test_config: A config we can inject for testing
    :return: The flask app
    """
    app = Flask(__name__)
    if not test_config:
        app.config.from_pyfile(os.path.join("..", "config.py"))
    else:
        app.config.from_pyfile(os.path.join("..", test_config))

    db.init_app(app)
    from eventsStore.models import Products, Events

    with app.app_context():
        db.create_all()

    from . import feeCalculator
    app.register_blueprint(feeCalculator.bp)
    app.add_url_rule('/', endpoint='chooseEvent')

    return app
