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
    - Token : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlUzTTViVTlzZEt3SGZHRE1neHVlTyJ9.eyJpc3MiOiJodHRwczovL2x3aW5hZ2VuY3kudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMzg4MWQ5NGZlYzZkMDA2ODJhNGQ0MSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTEwMCIsImlhdCI6MTYzMTg0Mjg0NCwiZXhwIjoxNjMxOTI5MjQ0LCJhenAiOiJ3RVdjSjFWNGQ2NHFDb3Vnc3k5c1o3RTAybmtYaGREVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.l64O81DI1XdY-NQ2ebw3YxhEakjQMurhpPBbhPJTj9AaKAx8Dhnwv9hhahJxRgtCc-eN43JpTff5nCs4ZfhF6PSATy_HddZHFGPlrd_A376bTMb712IU3c2rW1ZNyd0hqeR2ACP8ya7TToCEEq1VKMeMP1ZWJ0LwyJ7wPutHQ1Vaxv-wCrKo6AfcSY5FBDc1D3bu3XsyV7MyxafL1opsAZIqhwhO3FXBnvXaUOR5rxPBfuSjXUOdqX0mk6wuVaNgeuDIHDyA-0pEZdz2uEG97wVIU51LdueY7hTaXjY9kXAYpm8M4N8MXWg5RkiCh-udLzNi2hqUb7V30pbF_R5bWg


- Director
    - Email : director@lwinagency.com
    - Password : Udacity!23
    - Token : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlUzTTViVTlzZEt3SGZHRE1neHVlTyJ9.eyJpc3MiOiJodHRwczovL2x3aW5hZ2VuY3kudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMzg4MjgzY2JkMjcwMDA2OWY4MGM5YSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTEwMCIsImlhdCI6MTYzMTg0MjkwNiwiZXhwIjoxNjMxOTI5MzA2LCJhenAiOiJ3RVdjSjFWNGQ2NHFDb3Vnc3k5c1o3RTAybmtYaGREVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.nQTEMVC_aCXNglVdh588xKLwOj0cnPjvl8n8pxHju9fxSIxEJMw6WzaFJu6BmcTStETlv2gLlGqGTV2D44qrHwE3QmNpsXjAtnkK0vENF5b_ikKAzfDg2jD55ubIfiVOWOozD16avlq_cNy282lkkkEB5wko6eC9qnHZ-T_QzkR91YkzFCGp9JOo4-8X2zGhwpNSvthRIXyHLJ4HgsKGfdvp3td_dMNUkwOwRwS7AEEPfx-CcDG3XaUytTciA8ibZWw4Qve6-YOhF-PLhqks_rbkJMkXRYuQDVNfYmy3NTr4pjvl6hdFYvzQQY0urqv2-yw7zm_Vbpsca4wrJVFVwg

- Producer
    - Email : producer@lwinagency.com
    - Password : Udacity!23
    - Token : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlUzTTViVTlzZEt3SGZHRE1neHVlTyJ9.eyJpc3MiOiJodHRwczovL2x3aW5hZ2VuY3kudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMzg4MmE1NjFiZDFlMDA2ODAxZDg0YyIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTEwMCIsImlhdCI6MTYzMTg0Mjk3MSwiZXhwIjoxNjMxOTI5MzcxLCJhenAiOiJ3RVdjSjFWNGQ2NHFDb3Vnc3k5c1o3RTAybmtYaGREVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.AGAC8tw5OllJhzUhV3sC3jLp4TMdZS7lzXbyhiDtS3FItblBuLK1_3KZ1zCe3VfEE1W6B8l3kfGA_OnqaUbTEBl47k3NGk8SB3EzsDSBbZZnRtE6epE9Io2UGn8loYRr1vBhRHBNZNL-Ef_SQzwuxICvvmDxxmtBBLt55MC95syzUpK5NeQSOaEweElS8bE3N0satzcOUFcGbpegG3QTuGNwH6P6Gxve0QrG8pord6Oi2V4NqNVkXuoWSYr8EjHoqObJnIqDcLaSQ8eadSPNRrPRlK4_6oh5DsSTfPNtI-f_t2T6vo__ezlIs0TrM8HM7Rw2qtO7LGALDPk-QyOaOw


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
