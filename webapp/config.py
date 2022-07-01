import os  # path module

# specifies the full path to config.py
basedir = os.path.abspath(os.path.dirname(__file__))  # config in this folder (absolute path) -set path to file without prescribing it "manually"

SQLALCHEMY_TRACK_MODIFICATIONS = False # SQLalch gives signt if smth changes (big resurses)
SQLALCHEMY_DATABASE_URI = "postgresql://ihrdrkcc:b2mIYt4Nbfb63ML80X3LmmBnF_VXOUvF@abul.db.elephantsql.com/ihrdrkcc"
SECRET_KEY = "ffdsfsdkjfslkdjfsdlkfjsdlfkj"
WEATHER_DEFAULT_CITY = ("Amsterdam,Netherlands")  # capslock = permanet varaeble -don't change
WEATHER_API_KEY = "99d6a36178a5438a939193913222706"
WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"