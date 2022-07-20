from flask import Blueprint, current_app, render_template
from flask_login import current_user, login_required
from sqlalchemy.exc import OperationalError
from webapp.weatherhere import weather_by_city
from webapp.news.models import News
from webapp.tasks.utils import get_avatar

blueprint = Blueprint("news", __name__)


@blueprint.route("/")
@login_required
def index():
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    try:
        news_list = News.query.filter(News.disabled == False)
        news_list = news_list.order_by(News.published.desc())
        news_list = news_list.limit(10).all()
    except OperationalError:
        news_list = ("Unable to load news",)

    if current_user.is_authenticated:
        avatar = get_avatar(current_user.username)
    else:
        avatar = None

    return render_template(
        'news/news.html',
        avatar=avatar,
        weather_text=weather,
        news_list=news_list,
        page="news"
    )
