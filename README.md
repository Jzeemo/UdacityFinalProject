# Udacity Final Project 

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
    - Password : UdacityPassword
    - Token : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlUzTTViVTlzZEt3SGZHRE1neHVlTyJ9.eyJpc3MiOiJodHRwczovL2x3aW5hZ2VuY3kudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMzg4MWQ5NGZlYzZkMDA2ODJhNGQ0MSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTEwMCIsImlhdCI6MTYzMTM1NjkzMCwiZXhwIjoxNjMxNDQzMzMwLCJhenAiOiJ3RVdjSjFWNGQ2NHFDb3Vnc3k5c1o3RTAybmtYaGREVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.qbP7cZTvpknLl0ifoDjJ9TBIQTl94gXIXf21lc6Flxe52E7_0IBUwo6USRLIo3jfGaytSaUUISfaEOYVa3qV0tezsed-sSlvHxSeED_9d5hAQeklnKWe_7YLdp4WWxB1hqpWPKt6OfkjBPfx9wWfvCB52PJsmsXCEr6mShdBzacHO5Pkz7PachFAG7D06bjkdacgpjksUSFXuRQDYfn4N7c7MZDukWcGOyg4jt48ODz55c8oZFGp4ClWrsL11HVLkzvhwCjPk9JOIs945RU5BaLffjD_plCexxiwpPM6NRS6KzOvA578IboXFCyxIatUFCP0XZCx7GdwH1-X3tu3Hg


- Director
    - Email : director@lwinagency.com
    - Password : UdacityPassword
    - Token : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlUzTTViVTlzZEt3SGZHRE1neHVlTyJ9.eyJpc3MiOiJodHRwczovL2x3aW5hZ2VuY3kudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMzg4MjgzY2JkMjcwMDA2OWY4MGM5YSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTEwMCIsImlhdCI6MTYzMTM2MDM0MywiZXhwIjoxNjMxNDQ2NzQzLCJhenAiOiJ3RVdjSjFWNGQ2NHFDb3Vnc3k5c1o3RTAybmtYaGREVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.EOs7D4qq1r91mQ4fscrC6SCJxx3nbfCi3nFhakvFYl39uqcFo9lk8Nl2HZwy5CKnzlKxjBiixZVUhbIZL_se4ZiWy6ukfzlLSlY5_6tUG72vGYbeoT3Jg3lbEj9DYfvTx4WH2PpTMLomQy1NgOwip4mkGvSUxQJaqlK9miDTv2UcIoAvhFgSTE-DSwRJ8vobTjfms-UstXiXBQ9z7acEJ5JaapXb1q32xkzjiWp2-hKMqXV6k6ASzbWGrrXsBHzfKu1Jmi8Kx3jEUmXk5LuSQioLS4YwmRstpO06mcybtDGdf1JD6xRNHYI75LMnrhL5JJXyAvfuFVOPLG_vASyazw

- Producer
    - Email : producer@lwinagency.com
    - Password : UdacityPassword
    - Token : eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlUzTTViVTlzZEt3SGZHRE1neHVlTyJ9.eyJpc3MiOiJodHRwczovL2x3aW5hZ2VuY3kudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMzg4MmE1NjFiZDFlMDA2ODAxZDg0YyIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTEwMCIsImlhdCI6MTYzMTM2MDI4MCwiZXhwIjoxNjMxNDQ2NjgwLCJhenAiOiJ3RVdjSjFWNGQ2NHFDb3Vnc3k5c1o3RTAybmtYaGREVCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.c3nciVkjED8bDwTiMSYcv_XWsdZQLFo5kW70oa6WsCGCg4naKhIE8H-ntiwQ5Yh8vlMw0XXD9iBrYuOwO-RDz07Jyfkt9sEz2TqqNiat3m4E1yr1SEKUXkzpEYd50yDyNU_n1pi_ldRYmYUMhfrbcKkwZUhRxOOsVcqRPJC9UBwwT_0rl737SGuzlWq5VTYzcmdVw3_Gwxhf7JwoRI8GJ3XaYmr_-JmbqqlCU6VJHcIjyvNvwcSgKvg5wwx573D6gbeGyrDjujiCYxE5co337GaxqVdZp5tyJK5TJ6919gr1R51vqq-AG6TnpS_822haIHTFxHf_DAX9TuL3C9k4EQ


### Auth0 Login Url

```bash
https://lwinagency.us.auth0.com/authorize?audience=http://localhost:9100&response_type=token&client_id=wEWcJ1V4d64qCougsy9sZ7E02nkXhdDT&redirect_uri=http://localhost:9100/main
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