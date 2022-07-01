from flask import Flask, render_template
from flask_migrate import Migrate

from sqlalchemy.exc import OperationalError

from webapp.db import db
from webapp.forms import LoginForm
from webapp.weatherhere import weather_by_city
from webapp.model import News


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route("/")
    def index():
        title = 'Achievement share'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        try:
            news_list = News.query.filter(News.disabled == False)
            news_list = news_list.order_by(News.published.desc())
            news_list = news_list.limit(10).all()
        except OperationalError:
            news_list = ("Unable to load news",)

        return render_template(
            'news/news.html',
            page_title=title,
            weather_text=weather,
            news_list=news_list,
            page="news"
        )

    @app.route('/login')
    def login():
        title = 'Autorization'
        login_form = LoginForm()
        return render_template(
            'login.html', page_title=title, form=login_form
        )

    @app.route('/tasks')
    def tasks():
        title = 'Achievement share'
        return render_template(
            'tasks/tasks.html', page_title=title, page="tasks"
        )

    return app
