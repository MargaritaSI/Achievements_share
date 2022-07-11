from flask import Flask, render_template
from flask_migrate import Migrate
from webapp.db import db

#from webapp.model import db # what exactly db?
from webapp.forms import LoginForm
from webapp.weatherhere import weather_by_city

def create_app(): # create fabric function -creates and initializes flask application object
    app = Flask(__name__)
    app.config.from_pyfile('config.py') #take configuration file
    db.init_app(app)

    migrate = Migrate(app, db) # db?
    print('test done')

    @app.route("/")  # browser requested main page
# the view function index() prepares the data for display
    def index():  # handler of main page goes to server in a file 'weather' and returns weather
        title = 'News page'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        print(weather)
        news_list = 'here will be news'
        return render_template('index.html', page_title = title, weather_text=weather, news=news_list)


    @app.route('/login') # show us this form
    def login():
        title = 'Autorization'
        login_form = LoginForm() # create object of Class
        return render_template('login.html', page_title = title, form = login_form) # takes a template, substitutes data there and passes it to the browser
    return app # return flask application
