# routes for website will be stored here, basically pages user can go to (home,study page, etc...)
# this file will contain URLs for our website
from flask import Blueprint, render_template
# required to deal with user being logged in already and logging out
from flask_login import login_required, current_user

# set up blueprint for flask application
views = Blueprint('views', __name__)

# @nameOfBlueprint.route('URL to get to this endpoint')
@views.route('/home')
@login_required
# when user gets to this route, the following function will be ran
def home():
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