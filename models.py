# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой)

# Пример
from marshmallow import Schema, fields

from setup_db import db

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")

class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))



class MovieSchema(Schema):
    id = fields.Int()
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()

class GenreSchema(Schema):
    id = fields.Int()
    name = fields.String()


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.String()

