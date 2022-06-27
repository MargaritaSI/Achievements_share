import os  # path module

# specifies the full path to config.py
basedir = os.path.abspath(os.path.dirname(__file__))  # config in this folder (absolute path) -set path to file without prescribing it "manually"
WEATHER_DEFAULT_CITY = ("Amsterdam,Netherlands")  # capslock = permanet varaeble -don't change
WEATHER_API_KEY = "7ad555c0476e4f82b2c201425222405"
WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
# configuration where our database is located (if we don't have sqlite) set path to database
#POSTGRESQL_DATABASE_URI = "postgresql:///" + os.path.join( basedir, "..", "webapp.db")  # path for db/ 1 directory upper(lear_nweb) where our db/ name for db
SQLALCHEMY_TRACK_MODIFICATIONS = False # SQLalch gives signt if smth changes (big resurses)