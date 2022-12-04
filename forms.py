from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class SignUpForm(FlaskForm):
    inputName = StringField()
    inputEmail = StringField()
    inputPassword = PasswordField()
    submit = SubmitField('Sign Up')