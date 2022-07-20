
from datetime import date, datetime, timedelta

from flask import Blueprint, redirect, request
from flask_login import current_user, login_required

from sqlalchemy import func
from sqlalchemy.sql import or_, and_

from webapp.db import db
from webapp.user.models import User

from webapp.tasks.forms import \
    AddTaskForm, TelegramSprintsForm, AddTaskComment

from webapp.tasks.utils import \
    render_tasks, render_telegram_sprints, change_sprint_status, \
    render_shared, change_shared, render_task

from webapp.tasks.models import Tasks, TaskComments

blueprint = Blueprint('tasks', __name__, url_prefix='/tasks')


@blueprint.route('/today')
@login_required
def today():
    tasks_filter = or_(
        func.date(Tasks.due) == date.today(),
        Tasks.due == None
    )
    return render_tasks(tasks_filter, 'today')


@blueprint.route('/tomorrow')
@login_required
def tomorrow():
    tasks_filter = or_(
        func.date(Tasks.due) == date.today() + timedelta(days=1),
        Tasks.due == None
    )
    return render_tasks(tasks_filter, 'tomorrow')


@blueprint.route('/seven-days')
@login_required
def seven_days():
    tasks_filter = or_(
        and_(
            func.date(Tasks.due) <= date.today() + timedelta(days=7),
            func.date(Tasks.due) >= date.today(),
        ),
        Tasks.due == None
    )
    return render_tasks(tasks_filter, '7 days')


@blueprint.route('/telegram-sprints')
@login_required
def telegram_sprints():
    tasks_filter = or_(
        func.date(Tasks.due) >= date.today(),
        Tasks.due == None
    )
    return render_telegram_sprints(tasks_filter)


@blueprint.route('/task/<int:task_id>')
@login_required
def task(task_id):
    return render_task(task_id)


@blueprint.route('/shared')
@login_required
def shared():
    return render_shared()


@blueprint.route('/add-task', methods=['GET', 'POST'])
@login_required
def add_task():
    form = AddTaskForm()
    if request.method == 'POST':
        if form.due_time.data:
            due = datetime.combine(form.due_date.data, form.due_time.data)
        else:
            due = form.due_date.data

        new_task = Tasks(
            user_id=current_user.id,
            task=form.task.data,
            priority=form.priority.data,
            due=due if form.datetime_toggle.data else None
        )

        db.session.add(new_task)
        db.session.commit()
    return redirect(request.referrer)


@blueprint.route('/add-task-comment', methods=['GET', 'POST'])
@login_required
def add_task_comment():
    form = AddTaskComment()
    if request.method == 'POST':
        comment = TaskComments(
            user_id=current_user.id,
            comment=form.comment.data,
            task_id=form.task_id.data
        )
        db.session.add(comment)
        db.session.commit()
    return redirect(request.referrer)


@blueprint.route('/complete-task', methods=['POST'])
def complete_task():
    id = request.form['task_id']
    task = Tasks.query.filter(Tasks.id == id).first()
    task.completed = True
    task.completion_time = datetime.now()
    db.session.commit()
    return "Done"


@blueprint.route('/add-to-sprint', methods=['POST'])
def add_to_sprint():
    return change_sprint_status(request.form['task_id'], True)


@blueprint.route('/remove-from-sprint', methods=['POST'])
def remove_from_sprint():
    return change_sprint_status(request.form['task_id'], False)


@blueprint.route('/share', methods=['POST'])
def share():
    return change_shared(request.form['task_id'], True)


@blueprint.route('/stop-sharing', methods=['POST'])
def stop_sharing():
    return change_shared(request.form['task_id'], False)


@blueprint.route('/telegram-username', methods=['POST'])
def telegram_username():
    form = TelegramSprintsForm()
    task = User.query.filter(User.id == current_user.id).first()
    task.telegram_username = form.username.data
    db.session.commit()
    return redirect(request.referrer)
