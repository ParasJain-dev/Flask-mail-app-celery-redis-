from flask import Flask
from celery import Celery
import os
from flask_mail import Mail, Message
from auth import password


app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
print(celery)
celery.conf.update(app.config)

app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'porasjain28@gmail.com',
    MAIL_PASSWORD = password
))

mail = Mail(app)


@app.route('/get')
def sample_get():
    send_email.delay()
    return "This is a GET Request"


@app.route('/post', methods=['POST'])
def sample_post():
    return "This is a POST Request"


@celery.task
def send_email():
    with app.app_context():
        msg = Message("Winter is Here!!!",
                      sender="parasjain@moengage.com",
                      recipients=["parasjain@moengage.com"])
        msg.body = "Finally baarish is here!!!!"
        msg.html = "<b>Finally baarish is here!!!!</b>"
        mail.send(msg)


@app.route('/post', methods=['POST'])
def sample_posted():
    return "This is a test POST Request"
