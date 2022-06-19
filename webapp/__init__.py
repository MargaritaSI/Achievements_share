from flask import Flask, render_template
from flask_migrate import Migrate

#from webapp.model import db # what exactly db?
from webapp.weatherhere import weather_by_city
def creat_app(): # creat fabric function -creates and initializes flask application object
    app = Flask(__name__)
    app.config.from_pyfile('config.py') #take configuration file
    migrate = Migrate(app) # db?
    print('test done')

    @app.route("/")  # browser requested main page
# the view function index() prepares the data for display
    def index():  # handler of main page goes to server in a file 'weather' and returns weather
        title = 'News page'

        weather = weather_by_city("app.config['WEATHER_DEFAULT_CITY']")
        news_list = 'here will be news'
        return render_template('index.html', page_title = title, weather_text=weather, news=news_list)

    return app # return flask application
