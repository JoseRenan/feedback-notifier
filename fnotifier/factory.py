from flask import Flask
from fnotifier import db, ma


def create_app(package_name, settings_override=None):
    """
    Returns a :class:`Flask` application instance configured with common
    functionality for the platform.

    :param package_name: application package name
    :param settings_override: a dictionary of settings to override
    """

    app = Flask(package_name, instance_relative_config=True)
    app.config.from_object('fnotifier.settings')
    app.config.from_object(settings_override)
    db.init_app(app)
    ma.init_app(app)
    _register_blueprints(app)

    return app


def _register_blueprints(app):
    from fnotifier.feedback.routes import feedback
    app.register_blueprint(feedback)
