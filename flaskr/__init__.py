from flask import Flask
from flask_assets import Environment, Bundle


def create_app():
    # create and configure the app
    app = Flask(__name__)
    assets = Environment(app)

    css = Bundle('css-reset.css', 'variables.css', 'main.css', output='gen/packed.css')
    assets.register('css_all', css)

    from . import home
    app.register_blueprint(home.bp)

    from . import articles
    app.register_blueprint(articles.bp)

    from . import visualisations
    app.register_blueprint(visualisations.bp)

    #import pdb; pdb.set_trace()
    #print(app.url_map)

    return app
