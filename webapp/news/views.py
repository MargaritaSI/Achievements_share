from flask import Blueprint, current_app, render_template
from sqlalchemy.exc import OperationalError
from webapp.weatherhere import weather_by_city
from webapp.news.models import News

blueprint = Blueprint("news", __name__)


@blueprint.route("/")
def index():
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    try:
        news_list = News.query.filter(News.disabled == False)
        news_list = news_list.order_by(News.published.desc())
        news_list = news_list.limit(10).all()
    except OperationalError:
        news_list = ("Unable to load news",)

    return render_template(
        'news/news.html',
        weather_text=weather,
        news_list=news_list,
        page="news"
    )
