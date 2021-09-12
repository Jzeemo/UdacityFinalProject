import json
import unittest
from flask import testing
from werkzeug.datastructures import Headers
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from src.database.models import setup_db, Actor, Movie


Assistant_Token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlUzTTViVTlzZEt3SGZHRE1neHVlTyJ9.eyJpc3MiOiJodHRwczovL2x3aW5hZ2VuY3kudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMzg4MWQ5NGZlYzZkMDA2ODJhNGQ0MSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTEwMCIsImlhdCI6MTYzMTM1NjkzMCwiZXhwIjoxNjMxNDQzMzMwLCJhenAiOiJ3RVdjSjFWNGQ2NHFDb3Vnc3k5c1o3RTAybmtYaGREVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.qbP7cZTvpknLl0ifoDjJ9TBIQTl94gXIXf21lc6Flxe52E7_0IBUwo6USRLIo3jfGaytSaUUISfaEOYVa3qV0tezsed-sSlvHxSeED_9d5hAQeklnKWe_7YLdp4WWxB1hqpWPKt6OfkjBPfx9wWfvCB52PJsmsXCEr6mShdBzacHO5Pkz7PachFAG7D06bjkdacgpjksUSFXuRQDYfn4N7c7MZDukWcGOyg4jt48ODz55c8oZFGp4ClWrsL11HVLkzvhwCjPk9JOIs945RU5BaLffjD_plCexxiwpPM6NRS6KzOvA578IboXFCyxIatUFCP0XZCx7GdwH1-X3tu3Hg'
Producer_Token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlUzTTViVTlzZEt3SGZHRE1neHVlTyJ9.eyJpc3MiOiJodHRwczovL2x3aW5hZ2VuY3kudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMzg4MmE1NjFiZDFlMDA2ODAxZDg0YyIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTEwMCIsImlhdCI6MTYzMTM2MDI4MCwiZXhwIjoxNjMxNDQ2NjgwLCJhenAiOiJ3RVdjSjFWNGQ2NHFDb3Vnc3k5c1o3RTAybmtYaGREVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.c3nciVkjED8bDwTiMSYcv_XWsdZQLFo5kW70oa6WsCGCg4naKhIE8H-ntiwQ5Yh8vlMw0XXD9iBrYuOwO-RDz07Jyfkt9sEz2TqqNiat3m4E1yr1SEKUXkzpEYd50yDyNU_n1pi_ldRYmYUMhfrbcKkwZUhRxOOsVcqRPJC9UBwwT_0rl737SGuzlWq5VTYzcmdVw3_Gwxhf7JwoRI8GJ3XaYmr_-JmbqqlCU6VJHcIjyvNvwcSgKvg5wwx573D6gbeGyrDjujiCYxE5co337GaxqVdZp5tyJK5TJ6919gr1R51vqq-AG6TnpS_822haIHTFxHf_DAX9TuL3C9k4EQ'
Director_Token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlUzTTViVTlzZEt3SGZHRE1neHVlTyJ9.eyJpc3MiOiJodHRwczovL2x3aW5hZ2VuY3kudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMzg4MjgzY2JkMjcwMDA2OWY4MGM5YSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTEwMCIsImlhdCI6MTYzMTM2MDM0MywiZXhwIjoxNjMxNDQ2NzQzLCJhenAiOiJ3RVdjSjFWNGQ2NHFDb3Vnc3k5c1o3RTAybmtYaGREVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.EOs7D4qq1r91mQ4fscrC6SCJxx3nbfCi3nFhakvFYl39uqcFo9lk8Nl2HZwy5CKnzlKxjBiixZVUhbIZL_se4ZiWy6ukfzlLSlY5_6tUG72vGYbeoT3Jg3lbEj9DYfvTx4WH2PpTMLomQy1NgOwip4mkGvSUxQJaqlK9miDTv2UcIoAvhFgSTE-DSwRJ8vobTjfms-UstXiXBQ9z7acEJ5JaapXb1q32xkzjiWp2-hKMqXV6k6ASzbWGrrXsBHzfKu1Jmi8Kx3jEUmXk5LuSQioLS4YwmRstpO06mcybtDGdf1JD6xRNHYI75LMnrhL5JJXyAvfuFVOPLG_vASyazw'

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