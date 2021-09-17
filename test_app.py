import json
import unittest

from flask import testing
from flask_sqlalchemy import SQLAlchemy
from werkzeug.datastructures import Headers

from app import create_app
from src.database.models import Actor, Movie, setup_db

Assistant_Token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlUzTTViVTlzZEt3SGZHRE1neHVlTyJ9.eyJpc3MiOiJodHRwczovL2x3aW5hZ2VuY3kudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMzg4MWQ5NGZlYzZkMDA2ODJhNGQ0MSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTEwMCIsImlhdCI6MTYzMTg0Mjg0NCwiZXhwIjoxNjMxOTI5MjQ0LCJhenAiOiJ3RVdjSjFWNGQ2NHFDb3Vnc3k5c1o3RTAybmtYaGREVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.l64O81DI1XdY-NQ2ebw3YxhEakjQMurhpPBbhPJTj9AaKAx8Dhnwv9hhahJxRgtCc-eN43JpTff5nCs4ZfhF6PSATy_HddZHFGPlrd_A376bTMb712IU3c2rW1ZNyd0hqeR2ACP8ya7TToCEEq1VKMeMP1ZWJ0LwyJ7wPutHQ1Vaxv-wCrKo6AfcSY5FBDc1D3bu3XsyV7MyxafL1opsAZIqhwhO3FXBnvXaUOR5rxPBfuSjXUOdqX0mk6wuVaNgeuDIHDyA-0pEZdz2uEG97wVIU51LdueY7hTaXjY9kXAYpm8M4N8MXWg5RkiCh-udLzNi2hqUb7V30pbF_R5bWg'
Producer_Token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlUzTTViVTlzZEt3SGZHRE1neHVlTyJ9.eyJpc3MiOiJodHRwczovL2x3aW5hZ2VuY3kudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMzg4MmE1NjFiZDFlMDA2ODAxZDg0YyIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTEwMCIsImlhdCI6MTYzMTg0Mjk3MSwiZXhwIjoxNjMxOTI5MzcxLCJhenAiOiJ3RVdjSjFWNGQ2NHFDb3Vnc3k5c1o3RTAybmtYaGREVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.AGAC8tw5OllJhzUhV3sC3jLp4TMdZS7lzXbyhiDtS3FItblBuLK1_3KZ1zCe3VfEE1W6B8l3kfGA_OnqaUbTEBl47k3NGk8SB3EzsDSBbZZnRtE6epE9Io2UGn8loYRr1vBhRHBNZNL-Ef_SQzwuxICvvmDxxmtBBLt55MC95syzUpK5NeQSOaEweElS8bE3N0satzcOUFcGbpegG3QTuGNwH6P6Gxve0QrG8pord6Oi2V4NqNVkXuoWSYr8EjHoqObJnIqDcLaSQ8eadSPNRrPRlK4_6oh5DsSTfPNtI-f_t2T6vo__ezlIs0TrM8HM7Rw2qtO7LGALDPk-QyOaOw'
Director_Token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlUzTTViVTlzZEt3SGZHRE1neHVlTyJ9.eyJpc3MiOiJodHRwczovL2x3aW5hZ2VuY3kudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMzg4MjgzY2JkMjcwMDA2OWY4MGM5YSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTEwMCIsImlhdCI6MTYzMTg0MjkwNiwiZXhwIjoxNjMxOTI5MzA2LCJhenAiOiJ3RVdjSjFWNGQ2NHFDb3Vnc3k5c1o3RTAybmtYaGREVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.nQTEMVC_aCXNglVdh588xKLwOj0cnPjvl8n8pxHju9fxSIxEJMw6WzaFJu6BmcTStETlv2gLlGqGTV2D44qrHwE3QmNpsXjAtnkK0vENF5b_ikKAzfDg2jD55ubIfiVOWOozD16avlq_cNy282lkkkEB5wko6eC9qnHZ-T_QzkR91YkzFCGp9JOo4-8X2zGhwpNSvthRIXyHLJ4HgsKGfdvp3td_dMNUkwOwRwS7AEEPfx-CcDG3XaUytTciA8ibZWw4Qve6-YOhF-PLhqks_rbkJMkXRYuQDVNfYmy3NTr4pjvl6hdFYvzQQY0urqv2-yw7zm_Vbpsca4wrJVFVwg'

class AssistanctTestClient(testing.FlaskClient):
    def open(self, *args, **kwargs): 
        
        api_key_headers = Headers({
            'Authorization': 'Bearer {}'.format(Assistant_Token)
        })
        headers = kwargs.pop('headers', Headers())
        headers.extend(api_key_headers)
        kwargs['headers'] = headers
        return super().open(*args, **kwargs)

class DirectorTestClient(testing.FlaskClient):
    def open(self, *args, **kwargs): 
        
        api_key_headers = Headers({
            'Authorization': 'Bearer {}'.format(Director_Token)
        })
        headers = kwargs.pop('headers', Headers())
        headers.extend(api_key_headers)
        kwargs['headers'] = headers
        return super().open(*args, **kwargs)

class ProducerTestClient(testing.FlaskClient):
    def open(self, *args, **kwargs): 
        
        api_key_headers = Headers({
            'Authorization': 'Bearer {}'.format(Producer_Token)
        })
        headers = kwargs.pop('headers', Headers())
        headers.extend(api_key_headers)
        kwargs['headers'] = headers
        return super().open(*args, **kwargs)




class AssistantTestCase(unittest.TestCase):   

    def assistant_test_client(self,app):
        app.test_client_class = AssistanctTestClient
        return app.test_client 

    def setUp(self):
        self.app = create_app()
        self.client = self.assistant_test_client(self.app)
        self.database_name = "agency_test"
        self.database_path = "postgresql://{}/{}".format('postgres:UdacityPassword@agency.cpwbbkd2g7q2.ap-southeast-1.rds.amazonaws.com:5432', self.database_name)
        setup_db(self.app, self.database_path)                 

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        self.dummy_actor = {
        'name': 'Testing Name 1',
        'age': 60,
        'gender': 'Male'        
        }

        self.dummy_movie = {
        'title': 'Testing Movie 1',
        'release_date': 'Becoz your suck',
        'actors': [2,3]
        }

    '''
    Assistance Role Test Case
    '''

    def test_get_actors(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['actors'])

    def test_get_movies(self):
        response = self.client().get('/movies')
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['movies'])
    
    def test_create_actors(self):
        response = self.client().post('/actors',json=self.dummy_actor)
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,403)
        
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not granted')

    def test_create_movies(self):
        response = self.client().post('/movies',json=self.dummy_movie)
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,403)
        
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not granted')

    def test_patch_actors(self):

        dummy_patch_actor = {
            "age":80
        }

        response = self.client().patch('/actors/2',json=dummy_patch_actor)
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,403)
        
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not granted')

    def test_patch_movies(self):

        dummy_patch_actor = {
            "title":"update"
        }

        response = self.client().patch('/movies/2',json=dummy_patch_actor)
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,403)
        
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not granted')

    def test_delete_actors(self):        

        response = self.client().delete('/actors/2')
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,403)
        
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not granted')

    def test_delete_movies(self):               

        response = self.client().delete('/movies/3')
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,403)
        
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not granted')    


class DirectorTestCase(unittest.TestCase):    

    def director_test_client(self,app):
        app.test_client_class = DirectorTestClient
        return app.test_client

    def setUp(self):
        self.app = create_app()
        self.client = self.director_test_client(self.app)
        self.database_name = "agency_test"
        self.database_path = "postgresql://{}/{}".format('postgres:UdacityPassword@agency.cpwbbkd2g7q2.ap-southeast-1.rds.amazonaws.com:5432', self.database_name)
        setup_db(self.app, self.database_path)                 

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        self.dummy_actor = {
        'name': 'Testing Name 1',
        'age': 60,
        'gender': 'Male'        
        }

        self.dummy_movie = {
        'title': 'Testing Movie 1',
        'release_date': 'Becoz your suck',
        'actors': [2,3]
        }    

    '''
    Director Role Test Case
    '''

    def test_get_actors(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['actors'])

    def test_get_movies(self):
        response = self.client().get('/movies')
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['movies'])
    
    def test_create_actors(self):
        response = self.client().post('/actors',json=self.dummy_actor)
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,200)
        
        self.assertEqual(data['actor_created'], self.dummy_actor['name'])
        self.assertEqual(data['success'], True)

    def test_create_movies(self):
        response = self.client().post('/movies',json=self.dummy_movie)
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,403)
        
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not granted')

    def test_patch_actors(self):

        actor = Actor(self.dummy_actor['name'],self.dummy_actor['age'],45)

        actor.insert()

        actor_id = actor.id        

        dummy_patch_actor = {
            "age":80
        }

        response = self.client().patch('/actors/{}'.format(actor_id),json=dummy_patch_actor)
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,200)
        
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor']['age'],80)

    def test_patch_movies(self):

        actor = Actor(self.dummy_actor['name'],self.dummy_actor['age'],45)

        movie = Movie("original movie",self.dummy_movie['release_date'])

        movie.actors.append(actor)

        movie.insert()

        movie_id = movie.id        


        dummy_patch_movie = {
            "title":"update"
        }

        response = self.client().patch('/movies/{}'.format(movie_id),json=dummy_patch_movie)
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,200)
        
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movie']['title'],"update")

    def test_delete_actors(self):        

        actor = Actor(self.dummy_actor['name'],self.dummy_actor['age'],self.dummy_actor['gender'])

        actor.insert()

        actor_id = actor.id

        actor_before = Actor.query.all()

        response = self.client().delete('/actors/{}'.format(actor_id))        

        data = json.loads(response.data)        

        self.assertEqual(response.status_code,200)
        
        self.assertEqual(data['success'], True)

        self.assertEqual(data['actors'], actor_id)

        actor_after = Actor.query.all()

        self.assertTrue(len(actor_before) - len(actor_after) == 1)

    def test_delete_movies(self):     

        actor = Actor(self.dummy_actor['name'],self.dummy_actor['age'],45)

        movie = Movie(self.dummy_movie['title'],self.dummy_movie['release_date'])

        movie.actors.append(actor)

        movie.insert()

        movie_id = movie.id   

        response = self.client().delete('/movies/{}'.format(movie_id))
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,403)
        
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not granted')


class ProducerTestCase(unittest.TestCase):    

    def producer_test_client(self,app):
        app.test_client_class = ProducerTestClient
        return app.test_client

    def setUp(self):
        self.app = create_app()
        self.client = self.producer_test_client(self.app)
        self.database_name = "agency_test"
        self.database_path = "postgresql://{}/{}".format('postgres:UdacityPassword@agency.cpwbbkd2g7q2.ap-southeast-1.rds.amazonaws.com:5432', self.database_name)
        setup_db(self.app, self.database_path)                 

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        self.dummy_actor = {
        'name': 'Testing Name 1',
        'age': 60,
        'gender': 'Male'        
        }

        self.dummy_movie = {
        'title': 'Testing Movie 1',
        'release_date': 'Becoz your suck',
        'actors': [2,3]
        }    

    '''
    Producer Role Test Case
    '''

    def test_get_actors(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['actors'])

    def test_get_movies(self):
        response = self.client().get('/movies')
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['movies'])
    
    def test_create_actors(self):        

        response = self.client().post('/actors',json=self.dummy_actor)
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,200)
        
        self.assertEqual(data['actor_created'], self.dummy_actor['name'])
        self.assertEqual(data['success'], True)

    def test_create_movies(self):

        actor = Actor(self.dummy_actor['name'],self.dummy_actor['age'],20)

        actor.insert()

        self.dummy_movie = {
        'title': 'Testing Movie 1',
        'release_date': 'Becoz your suck',
        'actors': [actor.id]
        }


        response = self.client().post('/movies',json=self.dummy_movie)
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,200)
        
        self.assertEqual(data['movie_created'], self.dummy_movie['title'])
        self.assertEqual(data['success'], True)

    def test_patch_actors(self):

        actor = Actor(self.dummy_actor['name'],self.dummy_actor['age'],45)

        actor.insert()

        actor_id = actor.id        

        dummy_patch_actor = {
            "age":80
        }

        response = self.client().patch('/actors/{}'.format(actor_id),json=dummy_patch_actor)
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,200)
        
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actor']['age'],80)

    def test_patch_movies(self):

        actor = Actor(self.dummy_actor['name'],self.dummy_actor['age'],45)

        movie = Movie("original movie",self.dummy_movie['release_date'])

        movie.actors.append(actor)

        movie.insert()

        movie_id = movie.id        


        dummy_patch_movie = {
            "title":"update"
        }

        response = self.client().patch('/movies/{}'.format(movie_id),json=dummy_patch_movie)
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,200)
        
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movie']['title'],"update")    

    def test_delete_movies(self):     

        actor = Actor(self.dummy_actor['name'],self.dummy_actor['age'],45)

        movie = Movie(self.dummy_movie['title'],self.dummy_movie['release_date'])

        movie.actors.append(actor)

        movie.insert()

        movie_id = movie.id   

        movie_before = Movie.query.all()

        response = self.client().delete('/movies/{}'.format(movie_id))
        data = json.loads(response.data)        

        self.assertEqual(response.status_code,200)
        
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movies'], movie_id)

        movie_after = Movie.query.all()

        self.assertTrue(len(movie_before) - len(movie_after) == 1)

    def test_delete_actors(self):   

        actor = Actor(self.dummy_actor['name'],self.dummy_actor['age'],self.dummy_actor['gender'])

        actor.insert()

        actor_id = actor.id

        actor_before = Actor.query.all()

        response = self.client().delete('/actors/{}'.format(actor_id))        

        data = json.loads(response.data)        

        self.assertEqual(response.status_code,200)
        
        self.assertEqual(data['success'], True)

        self.assertEqual(data['actors'], actor_id)

        actor_after = Actor.query.all()

        self.assertTrue(len(actor_before) - len(actor_after) == 1)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
