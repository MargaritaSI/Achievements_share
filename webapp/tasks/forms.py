from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import (
    DateField, SelectField, SubmitField, TextAreaField, TimeField
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
