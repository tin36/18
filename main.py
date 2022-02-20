from flask import Flask
from flask_restx import Api

from app.config import Config
from setup_db import db
from views.genre import genre_ns
from views.movie import movie_ns
from views.director import director_ns

def create_app(config: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.app_context().push()
    return app

def register_extensions(app: Flask):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)

def create_data(app, db):
    with app.app_context():
        db.create_all()
        with db.session.begin():
            db.session.add_all()


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    register_extensions(app)
    app.run()



