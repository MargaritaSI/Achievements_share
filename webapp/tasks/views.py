
from datetime import date, datetime, timedelta
from flask import Blueprint, redirect, request
from sqlalchemy import func
from sqlalchemy.sql import or_, and_
from webapp.db import db
from webapp.tasks.forms import AddTaskForm
from webapp.tasks.utils import render_tasks
from webapp.tasks.models import Tasks

blueprint = Blueprint('tasks', __name__, url_prefix='/tasks')


@blueprint.route('/today')
def today():
    tasks_filter = or_(
        func.date(Tasks.due) == date.today(),
        Tasks.due == None
    )
    return render_tasks(tasks_filter, 'today')


@blueprint.route('/tomorrow')
def tomorrow():
    tasks_filter = or_(
        func.date(Tasks.due) == date.today() + timedelta(days=1),
        Tasks.due == None
    )
    return render_tasks(tasks_filter, 'tomorrow')


@blueprint.route('/seven-days')
def seven_days():
    tasks_filter = or_(
        and_(
            func.date(Tasks.due) <= date.today() + timedelta(days=7),
            func.date(Tasks.due) >= date.today(),
        ),
        Tasks.due == None
    )
    return render_tasks(tasks_filter, '7 days')


@blueprint.route('/add-task', methods=['GET', 'POST'])
def add_task():
    form = AddTaskForm()
    if request.method == 'POST':
        if form.due_time.data:
            due = datetime.combine(form.due_date.data, form.due_time.data)
        else:
            due = form.due_date.data

        new_task = Tasks(
            user_id=123,
            task=form.task.data,
            priority=form.priority.data,
            due=due if form.datetime_toggle.data else None
        )

        db.session.add(new_task)
        db.session.commit()
    return redirect(request.referrer)


@blueprint.route('/complete-task', methods=['POST'])
def complete_task():
    id = request.form['task_id']
    task = Tasks.query.filter(Tasks.id == id).first()
    task.completed = True
    db.session.commit()
    return "Done"
