from flask import Flask, render_template
from flask_migrate import Migrate
from webapp.db import db
from webapp.forms import LoginForm
from webapp.news.views import blueprint as news_blueprint
from webapp.tasks.views import blueprint as tasks_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(news_blueprint)
    app.register_blueprint(tasks_blueprint)

    @app.route('/login')
    def login():
        title = 'Autorization'
        login_form = LoginForm()
        return render_template('login.html', form=login_form)

    return app
