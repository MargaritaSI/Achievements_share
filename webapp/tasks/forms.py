from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import (
    BooleanField, DateField, SelectField, StringField,
    SubmitField, TextAreaField, TimeField,
)
from wtforms.validators import DataRequired

PRIORITY_CHOICES = [('1', 'High'), ('2', 'Medium'), ('3', 'Low')]


class AddTaskForm(FlaskForm):
    task = TextAreaField(
        'What do you want to do?',
        validators=[DataRequired()],
        render_kw={"class": "form-control", "rows": "3"}
    )
    priority = SelectField(
        'Priority',
        choices=PRIORITY_CHOICES,
        validators=[DataRequired()],
        render_kw={"class": "form-select", "id": "selectPriority"}
    )
    datetime_toggle = BooleanField(
        'Date and time',
        render_kw={
            "class": "form-check-input",
            "id": "datetime-toggle",
            "role": "switch"
        }
    )
    due_date = DateField(
        "Date",
        default=datetime.today,
        render_kw={"type": "date", "class": "form-control"}
    )
    due_time = TimeField(
        'Time',
        default=datetime.now,
        render_kw={"type": "time", "class": "form-control", "id": "timeInput"}
    )
    submit = SubmitField(
        'Add task',
        render_kw={"class": "btn btn-primary"}
    )


class TelegramSprintsForm(FlaskForm):
    username = StringField(
        'Your telegram username',
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "id": "username",
            "placeholder": "Username",
            "aria-label": "Username",
            "aria-describedby": "basic-addon1"
        }
    )
    submit = SubmitField(
        'Save',
        render_kw={"class": "btn btn-primary"}
    )
