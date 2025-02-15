from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    from . import blueprints

    app.register_blueprint(blueprints.home, url_prefix="/")
    app.register_blueprint(blueprints.recipes, url_prefix="/recipes")

    return app
