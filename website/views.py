# routes for website will be stored here, basically pages user can go to (home,study page, etc...)
# this file will contain URLs for our website
from flask import Blueprint, render_template, request, redirect, url_for, flash
# required to deal with user being logged in already and logging out
from flask_login import login_required, current_user
# to be able to create new deck
from .models import Deck
# to access the database (db) we created in __init__.py
from . import db

# set up blueprint for flask application
views = Blueprint('views', __name__)

# @nameOfBlueprint.route('URL to get to this endpoint')
@views.route('/home', methods = ['GET', 'POST'])
@login_required
# when user gets to this route, the following function will be ran
def home():
    if request.method == "POST":
        deck_name = request.form.get('deckName')
        try:
            for deck in current_user.decks:
                print(deck.name)
        except:
            print("unable to print user deck")
        deck_exists = Deck.query.filter_by(user_id = current_user.id, name = deck_name).first()
        if deck_exists:
            flash("Deck name already exists. Try a different name.", category='error')
        else:
            new_deck = Deck(name = deck_name, user_id = current_user.id)
            db.session.add(new_deck)
            db.session.commit()
            flash("New Deck Successfully created!", category='success')
            return redirect(url_for('views.home'))
    # passing curr_user allows us to reference user in template to check if authenticated
    return render_template("home.html", user = current_user)


@views.route('/study-session')
def study_session():
    return render_template("study_session.html", user = current_user)


@views.route('/practice-problems')
def practice_problems():
    return render_template("practice_problems.html", user = current_user)


@views.route('/')
def initial():
    return render_template("initial.html", user = current_user)

# to delete a deck from any user
@views.route('/delete/<int:id>')
def delete(id):
    deck_to_delete = Deck.query.get_or_404(id)
    try:
        db.session.delete(deck_to_delete)
        db.session.commit()
        flash("Deck successfully deleted.", category='success')
        return redirect(url_for('views.home'))
    except:
        flash("Unable to delete deck.", category='error')
        return redirect(url_for('views.home'))