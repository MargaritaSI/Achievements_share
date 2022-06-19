from flask import current_app
import requests

def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": current_app.config['WEATHER_URL'],
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "en",
    }
    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        weather = result.json()
        if "data" in weather:
            if "current_condition" in weather["data"]:
                try:
                    return weather["data"]["current_condition"][0]
                except (IndexError, TypeError):
                    return False
    except (requests.RequestExeption, ValueError): # check if incorrectly formulated result (JSON)
        print("Server error")
        return False
    return False


if __name__ == "__main__":
    weather = weather_by_city("Amsterdam,Netherlands")
    print(weather)
