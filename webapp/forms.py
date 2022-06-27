from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField # import field + bottom
from wtforms.validators import DataRequired # auto check of login form content

class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired()], render_kw = {'class': 'form-control'}) # caption for the form
    password = PasswordField('Password', validators=[DataRequired()], render_kw = {'class': 'form-control'})
    submit = SubmitField('Send!', render_kw = {'class': 'btn btn-primary'})