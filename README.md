# Feedback Notifier

A simple API that sends feedbacks from a contact page on a website or any rest client to the configured slack.

## Installation

To configure the feedback notifier, you have to create a database on mysql and configure the connection on `config.py` file.

After that, you have to [get an incoming webhook url](https://my.slack.com/services/new/incoming-webhook/) for the channel you want receive notification on your slack and put it on `fnotifier/util/slackutils.py` file on the `webhook_url` variable.

Doing it, you have just to run the commands above:
```shell
$ pip install -r requirements.txt
$ python run.py
```

OBS: You should use python 3.

## Using

To send a message to the slack channel you have just to send a POST request to `/feedback` with the content:

```json
{
	"description": "<The message or feedback>",
	"author_email": "<The email of the feedback author>",
	"author_name": "<The name of the feedback author>",
	"label": "<The label indicating what the feedback is, it can be one of: BUG|COMPLIMENT|SUGGESTION|COMPLAINT>"
}
```

### Thanks =D

It's a sample app made with learning purpose, if you want to suggest features or contribute, create a new issue or make a PR.
