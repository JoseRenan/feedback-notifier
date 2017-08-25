from flask import Flask
from fnotifier.core import db
import pymysql


def create_app(package_name, settings_override=None):
    """Returns a :class:`Flask` application instance configured with common
    functionality for the platform.
    :param package_name: application package name
    :param settings_override: a dictionary of settings to override
    """

    app = Flask(package_name, instance_relative_config=True)
    app.config.from_object('fnotifier.settings')
    app.config.from_object(settings_override)
    db.init_app(app)

    return app
