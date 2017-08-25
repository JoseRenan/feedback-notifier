from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class FeedbackError(Exception):
    """Base application error class."""

    def __init__(self, msg):
        self.msg = msg
