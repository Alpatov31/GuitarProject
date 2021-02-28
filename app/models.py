from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), index = True, unique = True)
    email = db.Column(db.String(128), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    points = db.Column(db.Integer, default = 0)
    level = db.Column(db.Integer, default = 1)
    # songs_learned = db.relationship("Song", backref = "songs_learned_by")
    # chords_learned = db.relationship("Chord", backref = "chords_learned_by")
    # articles_learned = db.relationship("Article", backref = "articles_learned_by")
    def __repr__(self):
        return f"{self.id}: {self.username}"
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    author = db.Column(db.String(128))
    text = db.Column(db.Text)
    points = db.Column(db.Integer)



class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    author = db.Column(db.String(128))
    # chords = db.relationship("Chord", backref = "contained_by")
    # notes = db.Column()
    text = db.Column(db.String(1024))
    points = db.Column(db.Integer)



class Chord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    image = db.Column(db.String(64))
    # sound =
    description = db.Column(db.String(128))
    points = db.Column(db.Integer)
    group = db.Column(db.Integer, default=1)

class ChordLearned(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    chord_id = db.Column(db.Integer)

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    url = db.Column(db.String(512))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# class Article(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(128))
#     text = db.Column(db.Text)
#     pub_time = db.Column(db.DateTime)
#     category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
#     category = db.relationship("Category", backref=db.backref('articles', lazy='dynamic'))
#
#
# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))
