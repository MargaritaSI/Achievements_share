from flask_wtf import FlaskForm
from webapp.user.models import User
from wtforms import BooleanField, StringField, PasswordField, \
    SubmitField  # field + bottom, BooleanField - for remember user
# auto check of login form content
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
    username = StringField(
        'User Name',
        validators=[DataRequired()],
        render_kw={'class': 'form-control'}
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()],
        render_kw={'class': 'form-control'}
    )
    remember_me = BooleanField(
        'Remember me',
        default=True,
        render_kw={'class': 'form-check-input'}
    )
    submit = SubmitField(
        'Send!',
        render_kw={'class': 'btn btn-primary'}
    )


class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    email = StringField(
        'E-mail',
        validators=[DataRequired(), Email()],
        render_kw={"class": "form-control"}
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    password2 = PasswordField(
        'Repeat password',
        validators=[DataRequired(), EqualTo('password')],
        render_kw={"class": "form-control"}
    )
    submit = SubmitField(
        'Send!',
        render_kw={"class": "btn btn-primary"}
    )

    def validate_username(self, username):
        user_count = User.query.filter_by(
            username=username.data
        ).count()
        if user_count > 0:
            raise ValidationError(
                "Username already exists"
            )

    def validate_email(self, email):
        user_count = User.query.filter_by(
            email=email.data
        ).count()
        if user_count > 0:
            raise ValidationError(
                "Username with this email already exists"
            )
