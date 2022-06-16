from flask import Flask
#from weatherhere import weather_by_city

def creat_app(): # creat fabric function -creates and initializes flask application object
    app = Flask(__name__)


@app.route("/")  # browser requested main page
# the view function index() prepares the data for display
def index():  # handler of main page goes to server in a file 'weather' and returns weather
    return 'Hello user!'
    # weather = weather_by_city("Amsterdam,Netherlands")
    # if weather:  # check if string exists
    #     return f"Now {weather['temp_C']}, feels like {weather['FeelsLikeC']}"
    # else:
    #     return f"weather service currently is unavailable"

    return app # return flask application