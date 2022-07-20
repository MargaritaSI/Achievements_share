from functools import wraps # helps with creating decorators

from flask import current_app, flash, request, redirect, url_for # flash shows and redirects user if they he is not an admin
from flask_login import config, current_user # config for access to exempt_methods,

def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if request.method in config.EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif current_app.config.get('LOGIN_DISABLED'):
            return func(*args, **kwargs)
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif not current_user.is_admin:
            flash('This page is only available to admins') # if function return 'false'
            return redirect(url_for('news.index')) # 'news.index' - because of folder 'news'
        return func(*args, **kwargs) # if function return 'true' we call decorated function
    return decorated_view