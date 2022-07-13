from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, \
    SubmitField  # field + bottom, BooleanField - for remember user
from wtforms.validators import DataRequired  # auto check of login form content


class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired()],
                           render_kw={'class': 'form-control'})  # caption for the form
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'class': 'form-control'})
    remember_me = BooleanField('Remember me', default=True, render_kw={'class': 'form-check-input'})
    submit = SubmitField('Send!', render_kw={'class': 'btn btn-primary'})