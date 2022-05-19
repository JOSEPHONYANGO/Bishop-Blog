from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,
                    SubmitField, SelectField)
<<<<<<< HEAD
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField("Blog title:", validators=[DataRequired()])
    post = TextAreaField("Type Away:", validators=[DataRequired()])
    submit = SubmitField("Post")

class UpdatePostForm(FlaskForm):
    title = StringField("Blog title", validators=[DataRequired()])
    post = TextAreaField("Type Away", validators=[DataRequired()])
    submit = SubmitField("Update")

class CommentForm(FlaskForm):
    comment = TextAreaField("Post Comment", validators=[DataRequired()])
=======
from wtforms.validators import Required

class PostForm(FlaskForm):
    title = StringField("Blog title:", validators=[Required()])
    post = TextAreaField("Type Away:", validators=[Required()])
    submit = SubmitField("Post")

class UpdatePostForm(FlaskForm):
    title = StringField("Blog title", validators=[Required()])
    post = TextAreaField("Type Away", validators=[Required()])
    submit = SubmitField("Update")

class CommentForm(FlaskForm):
    comment = TextAreaField("Post Comment", validators=[Required()])
>>>>>>> 9d79dcb6c2337f86709b7ef86f46b5f68245fc5c
    alias = StringField("Comment Alias")
    submit = SubmitField("Comment")

class UpdateProfile(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last Name")
    bio = TextAreaField("Bio")
    email = StringField("Email")
    submit = SubmitField("Update")