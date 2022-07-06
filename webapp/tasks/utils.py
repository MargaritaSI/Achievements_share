from flask import render_template
from webapp.tasks.models import Tasks
from webapp.tasks.forms import AddTaskForm


def call_template(tasks_list, title):
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
