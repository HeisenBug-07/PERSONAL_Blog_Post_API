from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='provide email'), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
