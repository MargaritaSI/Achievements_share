from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base # in declarate format(comfort but a little bit slow)
from sqlalchemy.orm import sessionmaker, scoped_session # creat session for DB

# url create a connection engine username:/password/@hostname/:port/DB name
engine = create_engine('postgresql://ihrdrkcc:b2mIYt4Nbfb63ML80X3LmmBnF_VXOUvF@abul.db.elephantsql.com/ihrdrkcc')
db_session = scoped_session(sessionmaker(bind=engine)) # creat session (can send requests and take results) + what DB we want to connect

Base = declarative_base() # all models will be inherited from Base and can interact with sqlalchemy/ DB
Base.query = db_session.query_property() # we can make requests using Base.query without db_session