from flask_restx import Resource, Namespace
from models import GenreSchema, Genre

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genre_ns.route('/')
class BooksView(Resource):
    def get(self):
        directors = Genre.query.all()
        return genres_schema.dump(directors), 200, {'Content-Type': 'application/json; charset=utf-8'}

@genre_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id):
        movie = Genre.query.get(id)
        return genre_schema.dump(movie), 200, {'Content-Type': 'application/json; charset=utf-8'}

