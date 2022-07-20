from datetime import date
from webapp.db import db

from flask import render_template
from flask_login import current_user

from sqlalchemy import func, nullslast
from sqlalchemy.sql import or_

import requests

from webapp.tasks.forms import \
    AddTaskForm, TelegramSprintsForm, AddTaskComment

from webapp.tasks.models import Tasks, TaskComments
from webapp.user.models import User


def render_tasks(tasks_filter, title):
    tasks_list = Tasks.query.filter(
        Tasks.user_id == current_user.id,
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
        avatar=get_avatar(current_user.username),
        title=title,
        tasks_list=tasks_list,
        medimum_count=medimum_count,
        low_count=low_count,
        total_count=total_count,
        form=add_task_form
    )


def render_telegram_sprints(tasks_filter):
    tasks_list = Tasks.query.filter(
        Tasks.user_id == current_user.id,
        Tasks.completed == False,
        Tasks.telegram == True,
        tasks_filter
    ).order_by(Tasks.due.asc(), Tasks.id.asc())

    add_task_form = AddTaskForm()
    telegram_sprints_form = TelegramSprintsForm()

    total_count = tasks_list.count()

    users = User.query.filter(
        User.id == current_user.id, User.telegram_username != None
    )
    telegram = users[0].telegram_username if users.count() > 0 else ''

    return render_template(
        'tasks/telegram-sprints.html',
        page="tasks",
        title="Telegram sprints",
        avatar=get_avatar(current_user.username),
        tasks_list=tasks_list,
        total_count=total_count,
        form=add_task_form,
        telegram_form=telegram_sprints_form,
        tg_username=telegram,
    )


def render_shared():
    tasks_list = Tasks.query.filter(
        Tasks.completed == False,
        Tasks.shared == True,
        or_(func.date(Tasks.due) >= date.today(), Tasks.due == None)
    ).order_by(
        nullslast(Tasks.created_time.desc()), Tasks.due.asc(), Tasks.id.asc()
    )

    add_task_form = AddTaskForm()

    return render_template(
        'tasks/shared.html',
        page="tasks",
        title="Shared",
        avatar=get_avatar(current_user.username),
        tasks_list=tasks_list,
        total_count=tasks_list.count(),
        form=add_task_form,
    )


def render_task(task_id):
    task = Tasks.query.filter(
         Tasks.id == task_id
    ).first()

    comments = TaskComments.query.filter(
        TaskComments.task_id == task_id
    ).order_by(TaskComments.submitted_time.asc()).all()

    add_task_form = AddTaskForm()
    add_task_comment_form = AddTaskComment(task_id=task_id)

    return render_template(
        'tasks/comments.html',
        page="task-comments",
        title="Comments",
        avatar=get_avatar(current_user.username),
        form=add_task_form,
        add_task_comment_form=add_task_comment_form,
        task=task,
        comments=comments
    )


def change_sprint_status(id, status):
    task = Tasks.query.filter(Tasks.id == id).first()
    task.telegram = status
    db.session.commit()
    return "Done"


def change_shared(id, status):
    task = Tasks.query.filter(Tasks.id == id).first()
    task.shared = status
    db.session.commit()
    return "Done"


def get_avatar(username):
    username = current_user.username
    try:
        avatar = requests.get(
            f'https://avatars.dicebear.com/api/jdenticon/{username}.svg',
            {'size': '30'}
        ).text
    except:
        avatar = None
    return avatar
