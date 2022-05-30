from flask import Flask
#from weatherhere import weather_by_city

app = Flask(__name__)

@app.route("/")  # браузер запросил главную страницу
def index():  # обработчик гл страницы идет на сервер в файл weather и возвр погоду
    return 'Hello you'
    # weather = weather_by_city("Amsterdam,Netherlands")
    # if weather:  # проверка строка существует
    #     return f"Now {weather['temp_C']}, feels like {weather['FeelsLikeC']}"
    # else:
    #     return f"weather service currently is unavailable"

if __name__ == "__main__":
    app.run(debug=True)