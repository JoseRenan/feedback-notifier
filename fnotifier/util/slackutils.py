import slackweb
from fnotifier.feedback.models import Label


webhook_url = '<YOUR WEBKOOK URL HERE>'

def notify_feedback(feedback):
    message = _make_message(feedback)
    _send_feedback(message)


def _send_feedback(message):
    slack = slackweb.Slack(url=webhook_url)
    slack.notify(**message)


def _make_message(feedback):

    attachment = {
        'text': feedback.description,
        'author_name': feedback.author_name,
        'footer': feedback.author_email
    }

    color_and_text = _get_attachment_color_and_title(feedback.label)
    attachment = {**attachment, **color_and_text}
    return {'attachments': [attachment]}


def _get_attachment_color_and_title(label):
    if label == Label.SUGGESTION:
        return {'color': '#7FD1E4', 'title': 'Sugestão'}
    elif label == Label.BUG:
        return {'color': '#DA0000', 'title': 'Ocorrencia de bug'}
    elif label == Label.COMPLAINT:
        return {'color': '#DBAA00', 'title': 'Crítica ou reclamação'}
    elif label == Label.COMPLIMENT:
        return {'color': '#009066', 'title': 'Elogio'}
