from flask import current_app
import requests


def weather_by_city(name):
    weather_url = current_app.config['WEATHER_URL']
    params = {
        "appid": current_app.config['WEATHER_API_KEY'],  # key
        "q": name,
        "mode": "json",
        "units": "metric",
        "lang": "en",
    }
    weather_data = {}
    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        res = result.json()
        weather_data = res['main']
    except Exception as e:  # check if incorrectly formulated result (JSON)
        print("Server error")
    return weather_data


if __name__ == "__main__":
    weather = weather_by_city("Amsterdam,Netherlands")
    print(weather)
