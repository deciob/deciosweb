import os

from flask import Flask
from flask import render_template


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import home
    app.register_blueprint(home.bp)

    from . import articles
    app.register_blueprint(articles.bp)

    from . import visualisations
    app.register_blueprint(visualisations.bp)

    return app
