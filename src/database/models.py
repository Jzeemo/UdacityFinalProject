from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.sql.sqltypes import DateTime

#Database Config
database_name = "agency"
database_path = "postgresql://{}/{}".format('postgres:123@localhost:5432', database_name)

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Movies
'''

class Movie(db.Model):
    __tablename = 'movie'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(String)    

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'title': self.title,
        'release_date': self.release_date
        }


'''
Actor
'''

class Actor(db.Model):
    __tablename = 'actor'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)    
    gender = Column(String)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'name': self.name,
        'gender': self.gender,
        'age': self.age
        }
