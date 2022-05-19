from flask_mail import Message
from flask import render_template
from . import mail

def welcome_message(subject,template,to,**kwargs):
<<<<<<< HEAD
    sender_email = "otienojoe14@gmail.com"
=======
    sender_email = "flasksendung@gmail.com"
>>>>>>> 9d79dcb6c2337f86709b7ef86f46b5f68245fc5c

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body = render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)

def notification_message(subject,template,to,**kwargs):
<<<<<<< HEAD
    sender_email = "otienojoe14@gmail.com"
=======
    sender_email = "flasksendung@gmail.com"
>>>>>>> 9d79dcb6c2337f86709b7ef86f46b5f68245fc5c

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body = render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)