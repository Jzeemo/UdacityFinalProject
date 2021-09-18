# Udacity Final Project 

### Motivation

- This project is the final project of Udacity's Full Stack Web Developer Nano Degree Course and I have learned a lot of things likes how to write the testing, documentation, implementation from sketch. In this project, I developed by using the knowledge that giving from this course. 

**Casting Agency** - This project is providing the api for casting agency application that include assistant, director and producer roles. Eash of the role has their own authorization.

- Assistant Role
    - Can view actors and movies

- Director Role
    - All permissions a Casting Assistant has and…
    - Add or delete an actor from the database
    - Modify actors or movies

- Producer Role
    - All permissions a Casting Director has and…
    - Add or delete a movie from the database

### Installing Dependencies

### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

 ### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
flask db init
flask db migrate 
flask db update
```

### Running the server

```bash
$env:FLASK_APP = "app.py"
$env:FLASK_ENV="development"
flask run
```

The `--development` flag will detect file changes and restart the server automatically.

### Roles

- Assistant
    - Email : assistant@lwinagency.com
    - Password : Udacity!23
    - Token : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlUzTTViVTlzZEt3SGZHRE1neHVlTyJ9.eyJpc3MiOiJodHRwczovL2x3aW5hZ2VuY3kudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMzg4MWQ5NGZlYzZkMDA2ODJhNGQ0MSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTEwMCIsImlhdCI6MTYzMTk1NDE1MSwiZXhwIjoxNjMyMDQwNTUxLCJhenAiOiJ3RVdjSjFWNGQ2NHFDb3Vnc3k5c1o3RTAybmtYaGREVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.mtRvTL5k15WHF_H1682dkI5-r-Uz0ftkR8QYrCpT5TNiLBK7L0eGYJ688nTNEyFs2fboqao98xtJdqVOIQ7pA_oRlTGaoj8Ige1Z8tGhE48t_3UlrtOFhdkbRdE2AxHCWG3jL_Isn8dobsaG2o6eyeb_Za2R3U7SDFhD1QMBidDb55fJGtogrSPPk9nqraNNRRqLpOR54t_DIOGdessFAeKTXfGGb5W_zmwve58bBb_IJabeppnGqRPeg63DxEF5jm1GpFhN50BFmBxnzEuIPt-Hj5lXRVP0oz6YQAYn8re8JZuEEayO9TD3Axny82x9tkOW_JwHMtRzfaQByw9r-w


- Director
    - Email : director@lwinagency.com
    - Password : Udacity!23
    - Token : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlUzTTViVTlzZEt3SGZHRE1neHVlTyJ9.eyJpc3MiOiJodHRwczovL2x3aW5hZ2VuY3kudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMzg4MjgzY2JkMjcwMDA2OWY4MGM5YSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTEwMCIsImlhdCI6MTYzMTk1NDI0NiwiZXhwIjoxNjMyMDQwNjQ2LCJhenAiOiJ3RVdjSjFWNGQ2NHFDb3Vnc3k5c1o3RTAybmtYaGREVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.OpLTr3QaDFtgrbeBX_XBiOywQDslBTK-Vy9hwosx1rOWtv46C3zpgE7BZxIuVmHK43WtnSbC_o4EOqLGH3JbFTHKG4Y9Bzikpbol4i8WWYE2CgnhT3XUJjX5nWjJ9OMsI81kBX0hoWrgvD9Ctg3dyE8kONX-cG1dZMRVoAOBK0KDaAQSlfqh5rzefrsChA1cV8MkotXZ-kvUgJsRXdFXTuLFF9srm1C4fS644WpXZBdfhW2RpV06eJT-eIyy2pB4ob4gUryfQ3lsDr2gmhuA6A3p3z06p0hgtDA3LF3ir5iWXE_NjCMHV5MLZTmqmJxKYcU8Ej9K-J7qnnmNLwd5Ug

- Producer
    - Email : producer@lwinagency.com
    - Password : Udacity!23
    - Token : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlUzTTViVTlzZEt3SGZHRE1neHVlTyJ9.eyJpc3MiOiJodHRwczovL2x3aW5hZ2VuY3kudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMzg4MmE1NjFiZDFlMDA2ODAxZDg0YyIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTEwMCIsImlhdCI6MTYzMTk1NDIxMSwiZXhwIjoxNjMyMDQwNjExLCJhenAiOiJ3RVdjSjFWNGQ2NHFDb3Vnc3k5c1o3RTAybmtYaGREVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.Js7Wp3eG3IuV_VpJ-4nRgtR1frIUTi2YhfUbQ3e5o18kvZxjyvAd17uOzs7J_SGmsVuJtVDAp3T5HSn0IoX5C1JLNY_zPFcACi8mgCXaXbPg8mKX3coLKUaM2SIokIfXuAM0JmdZLAf2q1yFDiGJHx1ohQWZbxKO7OkLeI1pwOg3KAbMhI72mlIruMKd9nXUgLpU21_Oj5T_owbpxmHyD5pH6uaVVvvcN__tLTmgCEgihdEJTWiQUZ-Zay1d1AvX1sOA8FZUI9xsYmMLgEjdUZYPOLtDibgpVkAkjuPsAqq9N9TkX_GqytikogGk_VqbP-mIRp_jnp457H4uj8tpow


### Auth0 Login Url

```bash
https://lwinagency.us.auth0.com/authorize?audience=http://localhost:9100&response_type=token&client_id=wEWcJ1V4d64qCougsy9sZ7E02nkXhdDT&redirect_uri=http://localhost:9100/main
```

### Heruko Url

```bash
https://lwinagency.herokuapp.com/
```

## API Reference

### Getting Started
#### GET /movies?page=<page_number>

* Description: Returns a list movies.
* Sample: `http://localhost:5000/movies?page=1`<br>

        {
            "movies": [
                {
                    "actors": [
                        {
                            "age": 80,
                            "gender": "Male",
                            "id": 2,
                            "name": "Jack Nicholson"
                        }
                    ],
                    "id": 3,
                    "release_date": "09/2020",
                    "title": "John Wick2"
                },
                {
                    "actors": [
                        {
                            "age": 65,
                            "gender": "Male",
                            "id": 3,
                            "name": "Jack Nicholson"
                        },
                        {
                            "age": 80,
                            "gender": "Male",
                            "id": 2,
                            "name": "Jack Nicholson"
                        }
                    ],
                    "id": 4,
                    "release_date": "09/2020",
                    "title": "John Wick2"
                }
            ],
            "success": true,
            "total_movies": 2
        }


#### GET /actors?page=<page_number>

* Description: Returns a list actors.
* Sample: `http://localhost:5000/actors?page=1`<br>

        {
            "actors": [
                {
                    "age": 65,
                    "gender": "Male",
                    "id": 3,
                    "name": "Jack Nicholson"
                },
                {
                    "age": 65,
                    "gender": "Male",
                    "id": 4,
                    "name": "Jack Nicholson"
                },
                {
                    "age": 80,
                    "gender": "Male",
                    "id": 2,
                    "name": "Jack Nicholson"
                }
            ],
            "success": true,
            "total_actors": 3
        }

#### POST /actors

* Description:
  * Creates a new actor
  * Returns JSON object with newly created actor
* Sample: POST Method`http://localhost:5000/actors'

    - Sample Request Body
    <br>

        {            
            {
                "name":"Jack Nicholson",
                "age":65,
                "gender": "Male"
            }
        }
        
    <br>

    - Sample Response
    <br> 

        {
            "actor_created": "Jack Nicholson",
            "actors": [
                {
                    "age": 65,
                    "gender": "Male",
                    "id": 2,
                    "name": "Jack Nicholson"
                },
                {
                    "age": 65,
                    "gender": "Male",
                    "id": 3,
                    "name": "Jack Nicholson"
                },
                {
                    "age": 65,
                    "gender": "Male",
                    "id": 4,
                    "name": "Jack Nicholson"
                }
            ],
            "success": true,
            "total_actors": 3
        }

#### POST /movies

* Description:
  * Creates a new movie
  * Returns JSON object with newly created movie
* Sample: POST Method`http://localhost:5000/movies'

    - Sample Request Body
    <br>

        {
            "title":"John Wick2",
            "release_date":"09/2020",
            "actors":[2,3]
        }
        
    <br>

    - Sample Response
    <br> 

        {
            "movie_created": "John Wick2",
            "movies": [
                {
                    "id": 3,
                    "release_date": "09/2020",
                    "title": "John Wick2"
                },
                {
                    "id": 4,
                    "release_date": "09/2020",
                    "title": "John Wick2"
                }
            ],
            "success": true,
            "total_movies": 2
        }


#### PATCH /actors

* Description:
  * Update actor
  * Returns JSON object with updated actor
* Sample: PATCH Method`http://localhost:5000/actors/2'

    - Sample Request Body
    <br>

        {
            "age":80
        }
        
    <br>

    - Sample Response
    <br> 

        {
            "actor": {
                "age": 80,
                "gender": "Male",
                "id": 2,
                "name": "Jack Nicholson"
            },
            "success": true
        }   

#### PATCH /movies

* Description:
  * Update movie
  * Returns JSON object with updated movie
* Sample: PATCH Method`http://localhost:5000/movies/3'

    - Sample Request Body
    <br>

        {
            "actors":[2]
        }
        
    <br>

    - Sample Response
    <br> 

        {
            "movie": {
                "actors": [
                    {
                        "age": 80,
                        "gender": "Male",
                        "id": 2,
                        "name": "Jack Nicholson"
                    }
                ],
                "id": 3,
                "release_date": "09/2020",
                "title": "John Wick2"
            },
            "success": true
        }   

#### DELETE /actors/\<int:id\>

* Description:
  * Deletes a actor by id 
  * Returns id of deleted actor upon success.
* Sample: Delete Method `http://localhost:5000/actors/2`<br>

        {
            "actors": 2,
            "success": true
        }


#### DELETE /movies/\<int:id\>

* Description:
  * Deletes a actor by id 
  * Returns id of deleted actor upon success.
* Sample: Delete Method `http://localhost:5000/movies/2`<br>

        {
            "movies": 2,
            "success": true
        }
