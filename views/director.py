from flask_restx import Resource, Namespace
from models import DirectorSchema, Director

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route('/')
class BooksView(Resource):
    def get(self):
        directors = Director.query.all()
        return directors_schema.dump(directors), 200, {'Content-Type': 'application/json; charset=utf-8'}

@director_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id):
        movie = Director.query.get(id)
        return director_schema.dump(movie), 200, {'Content-Type': 'application/json; charset=utf-8'}

