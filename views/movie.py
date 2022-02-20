from flask import request
from flask_restx import Resource, Namespace

from models import Movie, MovieSchema
from setup_db import db

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
@movie_ns.route('/')
class BooksView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        if director_id and genre_id:
            movies = Movie.query.filter_by(director_id=director_id, genre_id=genre_id)
        elif director_id:
            movies = Movie.query.filter_by(director_id=director_id)
        elif genre_id:
            movies = Movie.query.filter_by(genre_id=genre_id)
        elif year:
            movies = Movie.query.filter_by(year=year)
        else:
            movies = Movie.query.all()
        return movies_schema.dump(movies), 200, {'Content-Type': 'application/json; charset=utf-8'}

    def post(self):
        req_json = request.json
        movie_add = Movie(**req_json)
        db.session.add(movie_add)
        db.session.commit()
        return '', 201

@movie_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id):
        movie = Movie.query.get(id)
        return movie_schema.dump(movie), 200, {'Content-Type': 'application/json; charset=utf-8'}

    def delete(self, id):
        movie = Movie.query.get(id)
        if movie:
            db.session.delete(movie)
            db.session.commit()
            return '', 200
        else:
            return '', 204

    def put(self, id):
        movie = Movie.query.get(id)
        req_json = request.json
        movie.title = req_json.get('title')
        movie.description = req_json.get('description')
        movie.trailer = req_json.get('trailer')
        movie.year = req_json.get('year')
        movie.rating = req_json.get('rating')
        movie.genre_id = req_json.get('genre_id')
        movie.director_id = req_json.get('director_id')
        db.session.add(movie)
        db.session.commit()
        return '', 204
