from flask import request, Blueprint

from . models import feedback_schema, Feedback
from fnotifier.util import response
from fnotifier.util.slackutils import notify_feedback
from fnotifier import db


feedback = Blueprint('feedback', __name__, url_prefix='/feedback')


@feedback.route('/', methods=['POST'])
def create_feedback():
    """Receives an HTTP package, via POST method, with a  JSON-like
    :class:`Feedback` in its body and saves the :class:`Feedback`
    on the database and gives an id to it.

    :return feedback: the created :class:`Feedback` instance with an id
    """

    received_feedback = feedback_schema.make_object(request.get_json())
    db.session.add(received_feedback)
    db.session.commit()
    notify_feedback(received_feedback)
    return response.response_json_ok(feedback_schema.jsonify(received_feedback))


@feedback.route('/', methods=['GET'])
def get_feedbacks():
    """Receives an HTTP package, via GET method, and generates a list with
    all saved :class:`Feedback`s.

    :return feedbacks: a list with all saved :class:`Feedback`s
    """

    return response.response_json_ok(feedback_schema.jsonify(Feedback.query.all(), many=True))
