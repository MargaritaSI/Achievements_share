from flask import render_template
from sqlalchemy import nullslast
from webapp.tasks.models import Tasks
from webapp.tasks.forms import AddTaskForm, TelegramSprintsForm
from webapp.model import User
from webapp.db import db


def render_tasks(tasks_filter, title):
    tasks_list = Tasks.query.filter(
        Tasks.completed == False,
        tasks_filter
    ).order_by(Tasks.due.asc(), Tasks.id.asc())

    add_task_form = AddTaskForm()

    medimum_count = tasks_list.filter(Tasks.priority == 2).count()
    low_count = tasks_list.filter(Tasks.priority == 3).count()
    total_count = tasks_list.count()

    return render_template(
        'tasks/tasks.html',
        page="tasks",
        title=title,
        tasks_list=tasks_list,
        medimum_count=medimum_count,
        low_count=low_count,
        total_count=total_count,
        form=add_task_form
    )


def render_telegram_sprints(tasks_filter):
    tasks_list = Tasks.query.filter(
        Tasks.completed == False,
        Tasks.telegram == True,
        tasks_filter
    ).order_by(Tasks.due.asc(), Tasks.id.asc())

    add_task_form = AddTaskForm()
    telegram_sprints_form = TelegramSprintsForm()

    total_count = tasks_list.count()

    users = User.query.filter(User.id == 123, User.telegram_username != None)
    telegram = users[0].telegram_username if users.count() > 0 else ''

    return render_template(
        'tasks/telegram-sprints.html',
        page="tasks",
        title="Telegram sprints",
        tasks_list=tasks_list,
        total_count=total_count,
        form=add_task_form,
        telegram_form=telegram_sprints_form,
        tg_username=telegram,
    )


def change_sprint_status(id, status):
    task = Tasks.query.filter(Tasks.id == id).first()
    task.telegram = status
    db.session.commit()
    return "Done"
