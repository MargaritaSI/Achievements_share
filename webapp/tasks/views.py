
from datetime import date, datetime, timedelta
from flask import Blueprint, redirect, request
from sqlalchemy import func
from webapp.db import db
from webapp.tasks.forms import AddTaskForm
from webapp.tasks.utils import call_template
from webapp.tasks.models import Tasks

blueprint = Blueprint('tasks', __name__, url_prefix='/tasks')


@blueprint.route('/today')
def today():
    tasks_list = Tasks.query.filter(
        Tasks.completed == False,
        func.date(Tasks.due) == date.today()
    ).order_by(Tasks.due.asc(), Tasks.id.asc())

    return call_template(tasks_list, 'today')


@blueprint.route('/tomorrow')
def tomorrow():
    tasks_list = Tasks.query.filter(
        Tasks.completed == False,
        func.date(Tasks.due) == date.today() + timedelta(days=1)
    ).order_by(Tasks.due.asc(), Tasks.id.asc())
    return call_template(tasks_list, 'tomorrow')


@blueprint.route('/seven-days')
def seven_days():
    tasks_list = Tasks.query.filter(
        Tasks.completed == False,
        func.date(Tasks.due) <= date.today() + timedelta(days=7),
        func.date(Tasks.due) >= date.today()
    ).order_by(Tasks.due.asc(), Tasks.id.asc())
    return call_template(tasks_list, '7 days')


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
            due=due
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
