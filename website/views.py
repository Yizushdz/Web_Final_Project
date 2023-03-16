# routes for website will be stored here, basically pages user can go to (home,study page, etc...)
# this file will contain URLs for our website
from flask import Blueprint, render_template

# set up blueprint for flask application
views = Blueprint('views', __name__)

# @nameOfBlueprint.route('URL to get to this endpoint')
@views.route('/')
# when user gets to this route, the following function will be ran
def home():
    return render_template("home.html")

@views.route('/study-session')
def study_session():
    return render_template("study_session.html")

@views.route('/practice-problems')
def practice_problems():
    return render_template("practice_problems.html")