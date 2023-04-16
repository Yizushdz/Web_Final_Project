# from the current package (website), import the database
from . import db
# used to help handle user login
from flask_login import UserMixin

# make a 1-to-many relationship between deck and individual flashcards, then 1 user to many decks

# add database related to individual flashcards
class Flashcard(db.Model):
    '''name, deck_id, user_id'''
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(10000))
    # to store ID of deck each flashcard belongs to, many flashcards will belong to single deck
    deck_id = db.Column(db.Integer, db.ForeignKey('deck.id'))
    # to store user id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        try:
            return f'<Flashcard "{self.name[:10]}">'
        except:
            return f'<Flashcard ID "{self.id}">'

class Deck(db.Model):
    '''name, flashcards, user_id'''
    id = db.Column(db.Integer, primary_key = True)
    # to store date of each deck we make
    name = db.Column(db.String(100))
    # to store all flashcard IDs that belong to this deck
    flashcards = db.relationship('Flashcard', backref = "currDeck")
    # to store ID of user to which the deck belongs to
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Deck "{self.name}">'

# class for user data, inherits from db we created in __init__.py, and UserMixin
class User(db.Model, UserMixin):
    '''email, password, first_name, last_name, decks, flashcards'''
    # define all columns we want to have stored in this table
    # all objects must have a primary key that differentiates them all
    id = db.Column(db.Integer, primary_key = True)
    # email is type string w/ max len() of 150 chars, must be unique, no repeating emails
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    # to store all decks that belong to a single user
    decks = db.relationship('Deck', backref = 'user')
    # to store flashcards that belong to user
    flashcards = db.relationship('Flashcard', backref = 'user')

    # __repr__ will give each obj a string representation for debugging purposes
    def __repr__(self):
        return f'<User "{self.first_name}">'
