from fnotifier.core import db
from fnotifier import ma
from marshmallow import post_load


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000))

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return '<Feedback %r>' % self.description


class FeedbackSchema(ma.Schema):
    class Meta:
        fields = ('id', 'description')

    @post_load
    def make_object(self, data):
        return Feedback(**data)


feedback_schema = FeedbackSchema()
