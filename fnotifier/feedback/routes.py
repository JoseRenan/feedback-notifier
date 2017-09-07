from . models import feedback_schema, Feedback
from flask import request, Blueprint
from fnotifier.util import response
from fnotifier.core import db


feedback = Blueprint('feedback', __name__, url_prefix='/feedback')


@feedback.route('/', methods=['POST'])
def create_feedback():
    received_feedback = feedback_schema.make_object(request.get_json())
    db.session.add(received_feedback)
    db.session.commit()
    return response.response_json_ok(feedback_schema.jsonify(received_feedback))


@feedback.route('/', methods=['GET'])
def get_feedbacks():
    return response.response_json_ok(feedback_schema.jsonify(Feedback.query.all(), many=True))
