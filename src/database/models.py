from flask import jsonify
from flask_migrate import Migrate
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
    migrate = Migrate(app, db) 
'''
Movie_Link
'''

movie_items = db.Table('movie_items',
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
    db.Column('actor_id', db.Integer, db.ForeignKey('actor.id'), primary_key=True)
)



'''
Movies
'''

class Movie(db.Model):
    __tablename = 'movie'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(String)    
    actors = db.relationship('Actor', secondary=movie_items,
      backref=db.backref('movies', lazy=True))

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date        

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def insert_full(self):        
        print(self.actors)
    
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

    def full_format(self):

        actor_list = []
        for actor in self.actors:
            actor_list.append(actor.format())

        return {
        'id': self.id,
        'title': self.title,
        'release_date': self.release_date,
        'actors': actor_list
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
    
