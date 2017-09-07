from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
ma = Marshmallow()


class FeedbackError(Exception):
    """Base application error class."""

    def __init__(self, msg):
        self.msg = msg
