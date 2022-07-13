from flask import Flask, render_template
from flask_login import LoginManager # LoginManager -managing login process
from flask_migrate import Migrate

from webapp.db import db
from webapp.admin.views import blueprint as admin_blueprint # for connect blueprint with application
#from webapp.forms import LoginForm
from webapp.news.views import blueprint as news_blueprint
from webapp.tasks.views import blueprint as tasks_blueprint
from webapp.user.models import User  # link model with flask
from webapp.user.views import blueprint as user_blueprint # for connect blueprint with application
from webapp.weatherhere import weather_by_city


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()  #
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'  # this is how will called function def 'login'
    app.register_blueprint(user_blueprint)  # regisrtation blueprint for connection with application
    app.register_blueprint(admin_blueprint)  # regisrtation blueprint
    app.register_blueprint(news_blueprint)
    app.register_blueprint(tasks_blueprint)

    @login_manager.user_loader  # every time on open page login_manager takes cookes user_id and send it to 'load_user'
    def load_user(user_id):  # take user with id
        return User.query.get(user_id)  # ask database with id_user - object user for work

    return app
