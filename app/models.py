from datetime import datetime
from app import db




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
