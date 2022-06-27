# import requests
#
# def weather_by_city(city_name):
#     weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
#     params = {
#         "key": "7ad555c0476e4f82b2c201425222405",
#         "q": city_name,
#         "format": "json",
#         "num_of_days": 1,
#         "lang": "en",
#     }
#     try:
#         result = requests.get(weather_url, params=params)
#         result.raise_for_status()
#         weather = result.json()
#         if "data" in weather:
#             if "current_condition" in weather["data"]:
#                 try:
#                     return weather["data"]["current_condition"][0]
#                 except (IndexError, TypeError):
#                     return False
#     except (requests.RequestExeption, ValueError): # check if incorrectly formulated result (JSON)
#         print("Server error")
#         return False
#     return False
#
#
# if __name__ == "__main__":
#     weather = weather_by_city("Amsterdam,Netherlands")
#     print(weather)
