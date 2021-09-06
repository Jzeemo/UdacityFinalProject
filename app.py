from flask import Flask, abort, jsonify, request
from flask_cors import CORS
from sqlalchemy.sql.functions import current_date

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
        response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods','GET,PUT,POST,DELETE,OPTIONS')
    
        return response

    def paginate_list(request, selection):
        pages = request.args.get('page', 1, type=int)
        start_value = (pages - 1) * 10
        end_value = start_value + 10

        data = [data.format() for data in selection]
        current_data = data[start_value:end_value]

        return current_data

    @app.route('/movies')
    def get_all_movies():

        #get all category
        movies = Movie.query.all()

        #convert to list
        movies_list = [movies.format() for movie in movies]                

        return jsonify({'success': True,'categories': movies_list}) 
