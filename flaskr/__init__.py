

from flask import Flask


def create_app():
    # create and configure the app
    app = Flask(__name__)


    from . import home
    app.register_blueprint(home.bp)

    from . import articles
    app.register_blueprint(articles.bp)

    from . import visualisations
    app.register_blueprint(visualisations.bp)

    return app
