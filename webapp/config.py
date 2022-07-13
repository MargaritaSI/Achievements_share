from datetime import timedelta # Duration of saving the authorization status

import os  # path module

# specifies the full path to config.py
basedir = os.path.abspath(os.path.dirname(__file__))  # config in this folder (absolute path) -set path to file without prescribing it "manually"
WEATHER_DEFAULT_CITY = ("Amsterdam,Netherlands")  # capslock = permanent variable -don't change
WEATHER_API_KEY = "f5d8e93bc61a8a642755f7a29885cf5b" # new key
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather" # new url without variables

# configuration where our database is located (if we don't have sqlite) set path to database
SQLALCHEMY_DATABASE_URI = "postgresql://ihrdrkcc:b2mIYt4Nbfb63ML80X3LmmBnF_VXOUvF@abul.db.elephantsql.com/ihrdrkcc"  # path for db/ 1 directory upper(lear_nweb) where our db/ name for db
SQLALCHEMY_TRACK_MODIFICATIONS = False # SQLalch gives signt if smth changes (big resurses)

SECRET_KEY = 'OISDH.jh-hkjds'

REMEMBER_COOKIE_DURATION= timedelta(days=5)