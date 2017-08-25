from . models import feedback_schema, Feedback
from flask import Flask, request
from fnotifier import app
from fnotifier.core import db


@app.route('/feedback/', methods=['POST'])
def create_feedback():
    feedback = feedback_schema.make_object(request.get_json())
    db.session.add(feedback)
    db.session.commit()
    return feedback_schema.jsonify(feedback), 200, {'Content-Type': 'application/json'}


@app.route('/feedback/', methods=['GET'])
def get_feedbacks():
    return feedback_schema.jsonify(Feedback.query.all(), many=True), 201, {'Content-Type': 'application/json'}
