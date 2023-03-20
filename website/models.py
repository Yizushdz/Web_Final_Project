# from the current package (website), import the database
from . import db
# used to help handle user login
from flask_login import UserMixin
# used to get current time and store it for each deck of flashcards
from sqlalchemy.sql import func

# add database related to individual flashcards
# make a 1-to-many relationship between deck and individual flashcards, then 1 user to many decks
class Deck(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # to store date each deck we make
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    # placeholder column, REMOVE
    data = db.Column(db.String(1000))

# class for user data, inherits from db we created in __init__.py, and UserMixin
class User(db.Model, UserMixin):
    '''email, password, first_name, last_name'''
    # define all columns we want to have stored in this table
    # all objects must have a primary key that differentiates them all
    id = db.Column(db.Integer, primary_key = True)
    # email is type string w/ max len() of 150 chars, must be unique, no repeating emails
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
