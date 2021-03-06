import os

from flask import (Flask,
                   abort,
                   jsonify,
                   request,
                   render_template,
                   make_response)
from flask_cors import CORS

from src.auth.auth import AuthError, requires_auth
from src.database.models import Actor, Movie, setup_db


def create_app():
    app = Flask(__name__)
    setup_db(app)
    CORS(app, resources={'/': {'origins': '*'}})

    @app.after_request
    def after_request(response):
        '''
        Sets access control.
        '''
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,OPTIONS')

        return response

    def paginate_list(request, selection):
        pages = request.args.get('page', 1, type=int)
        start_value = (pages - 1) * 10
        end_value = start_value + 10

        data = [data.format() for data in selection]
        current_data = data[start_value:end_value]
        return current_data

    @app.route('/')
    def index():
        return make_response(render_template('index.html'))

    '''
    Get Method
    '''

    @app.route('/movies')
    @requires_auth("get:movies")
    def get_all_movies():

        # get total actor and current actor
        total_movie = len(Movie.query.all())
        current_actor = paginate_list(request, Movie.query.all())

        return jsonify({'success': True,
                        'movies': current_actor,
                        'total_movies': total_movie})

    @app.route('/actors')
    @requires_auth("get:actors")
    def get_all_actors():

        # get total actor and current actor
        total_actor = len(Actor.query.all())
        current_actor = paginate_list(request, Actor.query.all())

        return jsonify({'success': True,
                        'actors': current_actor,
                        'total_actors': total_actor})

    '''
    POST Method
    '''

    # Create Actor
    @app.route('/actors', methods=['POST'])
    @requires_auth("post:actors")
    def add_actors():

        # get the request_data
        request_body = request.get_json()

        name = request_body['name']
        age = request_body['age']
        gender = request_body['gender']

        # check the request data is correct or not
        if ((name is None) or (age is None)
                or (gender is None)):
            abort(422)
        try:

            # actor create
            actor = Actor(name, age, gender)
            actor.insert()

            # get total actor and current actor
            total_actor = len(Actor.query.all())
            current_actor = paginate_list(
                request, Actor.query.order_by(
                    Actor.id).all())

            return jsonify({'success': True,
                            'actor_created': actor.name,
                            'actors': current_actor,
                            'total_actors': total_actor})
        except Exception:
            abort(422)

    # Create Movies
    @app.route('/movies', methods=['POST'])
    @requires_auth("post:movies")
    def add_movies():

        # get the request_data
        request_body = request.get_json()

        title = request_body['title']
        release_date = request_body['release_date']
        actors = request_body['actors']

        # check the request data is correct or not
        if ((title is None) or (release_date is None)
                or (actors is None)):
            abort(422)
        try:

            movie = Movie(title, release_date)

            for actor_id in actors:
                actor = Actor.query.filter_by(id=actor_id).one_or_none()

                if(actor is None):
                    abort(422)
                movie.actors.append(actor)

            movie.insert()

            # get total movies and current movies
            total_movies = len(Movie.query.all())
            current_movies = paginate_list(
                request, Movie.query.order_by(
                    Movie.id).all())

            return jsonify({'success': True,
                            'movie_created': movie.title,
                            'movies': current_movies,
                            'total_movies': total_movies})
        except Exception as error:
            print(error)
            abort(422)

    '''
    Edit Method
    '''

    # Update Actor
    @app.route("/actors/<int:actor_id>", methods=["PATCH"])
    @requires_auth("patch:actors")
    def update_actors(actor_id):

        # check the update drink id , return 400 if none
        if actor_id is None:
            abort(400)

        # get the drink by id
        actor = Actor.query.filter_by(id=actor_id).one_or_none()

        # return None, If there is no drink by id
        if actor is None:
            abort(404)

        try:
            request_body = request.get_json()

            if "name" in request_body:
                actor.name = request_body["name"]

            if "age" in request_body:
                actor.age = request_body["age"]

            if "gender" in request_body:
                actor.gender = request_body["gender"]

            actor.update()
            return jsonify({"success": True, "actor": actor.format()})

        except Exception:
            abort(500)

    # Update Movie
    @app.route("/movies/<int:movie_id>", methods=["PATCH"])
    @requires_auth("patch:movies")
    def update_movies(movie_id):

        # check the update movie id , return 400 if none
        if movie_id is None:
            abort(400)

        # get the movie by id
        movie = Movie.query.filter_by(id=movie_id).one_or_none()

        # return None, If there is no movie by id
        if movie is None:
            abort(404)

        try:
            request_body = request.get_json()

            if "title" in request_body:
                movie.title = request_body["title"]

            if "release_date" in request_body:
                movie.release_date = request_body["release_date"]

            if "actors" in request_body:
                movie.actors = []

                actors = request_body["actors"]

                for actor_id in actors:

                    actor = Actor.query.filter_by(id=actor_id).one_or_none()

                    if(actor is None):
                        abort(422)
                    movie.actors.append(actor)

            movie.update()
            return jsonify({"success": True, "movie": movie.format()})

        except Exception as error:
            print(error)
            abort(500)

    '''
    Delete Method
    '''

    # delete actor
    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    @requires_auth("delete:actors")
    def delete_actors(actor_id):

        # check the update actor id , return 400 if none
        if actor_id is None:
            abort(400)

        # get the actor by id
        actor = Actor.query.filter_by(id=actor_id).one_or_none()

        # return None, If there is no actor by id
        if actor is None:
            abort(404)

        try:

            actor.delete()
            return jsonify({"success": True, "actors": actor_id})

        except Exception:
            abort(500)

    # delete movies
    @app.route("/movies/<int:movie_id>", methods=["DELETE"])
    @requires_auth("delete:movies")
    def delete_movies(movie_id):

        # check the update movie id , return 400 if none
        if movie_id is None:
            abort(400)

        # get the movie by id
        movie = Movie.query.filter_by(id=movie_id).one_or_none()

        # return None, If there is no movie by id
        if movie is None:
            abort(404)

        try:

            movie.delete()
            return jsonify({"success": True, "movies": movie_id})

        except Exception:
            abort(500)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource Not Found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable, input syntex error"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request!"
        }), 400

    @app.errorhandler(500)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error! Sry"
        }), 400

    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    return app


app = create_app()


if __name__ == "__main__":
    app.run()
