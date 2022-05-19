from flask import render_template, request
from . import main
from .. import db
from ..models import Subscribers
from ..email import welcome_message, notification_message

@main.app_errorhandler(404)
def notfound(error):
    """
    Function to render the 404 error page
    """
    if request.method == "POST":
        new_sub = Subscribers(email = request.form.get("subscriber"))
        db.session.add(new_sub)
        db.session.commit()
<<<<<<< HEAD
        welcome_message("Thank you for subscribing to the Bishop blog", 
                        "email/welcome", new_sub.email)
    return render_template("profile/notfound.html"),404
=======
        welcome_message("Thank you for subscribing to the CM blog", 
                        "email/welcome", new_sub.email)
    return render_template("notfound.html"),404
>>>>>>> 9d79dcb6c2337f86709b7ef86f46b5f68245fc5c
