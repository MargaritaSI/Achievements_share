from sqlalchemy import Column, Integer, String # for creat model

from db import Base, engine

class User(Base): # model=python class
    __tablename__ = 'users' # creat spreadsheet

    id = Column(Integer, primary_key=True) # creat columns
    username = Column(String)
    privilege = Column(String)
    urgency = Column(String)
    password = Column(String(4)) # with integers?
    todo_list = Column(String)
    name_business = Column(String)
    done = Column(String)
    not_done = Column(String)
    data_business = Column(Integer)
    email = Column(String(120), unique = True) # max len string + unic email


    def __repr__(self): # method called when we display user instance in command line
        return f'User {self.id}, {self.username}, {self.privilege}, {self.urgency}, {self.password}, {self.todo_list},' \
               f'{self.name_business}, {self.not_done}, {self.done}, {self.data_business}, {self.email}' # we can see id + name.. of user for our understanding

if __name__== '__main__': # if we call it directly then we create a table
    Base.metadata.create_all(bind=engine)  # creates a corresponding table in the database