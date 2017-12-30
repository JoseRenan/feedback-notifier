from flask import Flask
from fnotifier import db, ma


def create_app(package_name, settings_override=None):
    """A factory method to generates and configures a :class:`Flask` app based
    on default settings or on the given settings.

    :param package_name: application package name
    :param settings_override: a dictionary of settings to override
    :return app: :class:`Flask` application instance configured with common
    functionality for the platform
    """

    app = Flask(package_name, instance_relative_config=True)
    app.config.from_object('fnotifier.config')
    app.config.from_object(settings_override)
    with app.app_context():
        db.init_app(app)
        ma.init_app(app)
        _register_blueprints(app)
        db.create_all()

    return app


def _register_blueprints(app):
    """An method that register all the application's blueprints
    on a given :class:`Flask` application instance.

    :param app: :class:`Flask` application instance
    """
    from fnotifier.feedback.routes import feedback
    app.register_blueprint(feedback)
