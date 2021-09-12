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

