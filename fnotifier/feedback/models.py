import enum

from marshmallow import post_load, fields
from marshmallow_enum import EnumField

from fnotifier import db, ma


class Label(enum.IntEnum):
    BUG = 1
    COMPLIMENT = 2
    COMPLAINT = 3
    SUGGESTION = 4


class Feedback(db.Model):
    """Represents the feedback given from the user

    :param description: a string containing the message of the feedback
    :param uid: a number which is the unique identifier of the feedback
    """

    uid = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500))
    author_email = db.Column(db.String(255))
    author_name = db.Column(db.String(255))
    label = db.Column(db.Enum(Label))

    def __init__(self, description, label, author_email, author_name, uid=None):
        self.description = description
        self.label = label
        self.author_email = author_email
        self.author_name = author_name
        self.uid = uid

    def __repr__(self):
        return 'Feedback (uid=%d, label=%s, email=%s, author_name=%s, description=%s)' \
               % (self.uid, self.label, self.author_email, self.author_name, self.description)


class FeedbackSchema(ma.Schema):

    uid = fields.Int()
    description = fields.Str()
    label = EnumField(Label, by_value=True)
    author_email = fields.Str()
    author_name = fields.Str()

    @post_load
    def make_object(self, data):
        data['label'] = Label(data['label'])
        return Feedback(**data)


feedback_schema = FeedbackSchema()
