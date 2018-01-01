# Feedback Notifier

A simple API that sends feedbacks from a contact page on a website or any REST client to a configured Slack account.

## Installation

To configure the feedback notifier, you have to first create a database on MySQL and set the connection configurations on the `config.py` file.

After that, you have to [get an incoming webhook URL](https://my.slack.com/services/new/incoming-webhook/) for the Slack channel in which you want to receive notifications and reference it on the `webhook_url` variable found on the `fnotifier/util/slackutils.py` file.

Once you have gone through the previous steps, you have only got to run the following commands:
```shell
$ pip install -r requirements.txt
$ python run.py
```

Note: You should use Python 3.

## Use

To send a message to the Slack channel you have just to send a POST request to `/feedback` with this JSON content:

```json
{
	"description": "<The message or feedback>",
	"author_email": "<The email of the feedback author>",
	"author_name": "<The name of the feedback author>",
	"label": "<The label indicating what the feedback is about. It can be one of these: BUG|COMPLIMENT|SUGGESTION|COMPLAINT>"
}
```

### Thanks! =D

This a sample app made for learning purposes. If you want to suggest features or contribute, you are encouraged to create a new issue or make a PR.
