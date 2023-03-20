# log-in page goes here because it relates to authentication
from flask import Blueprint, render_template, request, flash, redirect, url_for
# to be able to create new user
from .models import User
# to access the database (db) we created in __init__.py
from . import db
# hash used so we don't actually store user's pw as is, rather store them as hash links for security
from werkzeug.security import generate_password_hash, check_password_hash

# set up blueprint for flask application, same name as file not required, but standard
auth = Blueprint('auth', __name__)

# we will define the log-in, sign-up, and log-out in here
@auth.route('/login', methods = ["GET", "POST"])
def login():
    # if user tring to log in
    if request.method == "POST":
        # get email they input and store it in variable email
        email = request.form.get("email")
        # .get("str"), where "str" must match name parameter from login.html div
        password = request.form.get("password")
        # see if email user inputed is already in database
        # we filter all entries in database that match email user inputed, should be one or DNE
        user = User.query.filter_by(email = email).first()
        # if we actually found a matching email:
        if user:
            # check if password associated with that existing user matches password entered by user in login page
            if check_password_hash(user.password, password):
                # proceed to log in
                flash("Logged in successfully.", category="success")
                return redirect(url_for("views.home"))
            # email exists but password is wrong
            else:
                flash("Wrong password. Try again.", category="error")
        # user email does NOT exist
        else:
            flash("Email does NOT exist. Check email is right or sign up.", category="error")


    # to retrieve all data that was sent as part of a form
    # data = request.form
    # print(data)


    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

# methods: we are now able to receive POST and GET requests from these routes
@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    # if the request is user submitting something
    if request.method == 'POST':
        # get all their info and store it
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        lastName = request.form.get("lastName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # variable to check if email inputed already exists in database
        user = User.query.filter_by(email = email).first()

        # check if user entered an existing email
        if user:
            flash("Email already exists. Try loggin in instead.", category="error")
        # checking if the info provided by user is valid
        elif len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        # if passwords don't match, flash a message to user
        elif password1 != password2:
            flash("Passwords do not match.", category="error")
        elif len(password1) < 7:
            flash("Password must be longer than 6 characters.", category="error")
        # if all info is right, proceed to create user
        else:
            # new User obj being created
            # password method is a hash algorithm
            new_user = User(email = email, first_name = firstName, last_name = lastName, password = generate_password_hash(password1, method="sha256"))
            # to add new user to database
            db.session.add(new_user)
            # once we make change in database, we must commit change doing:
            db.session.commit()
            flash("Account successfully created.", category="success")
            # redirect us to the url for the home page after account is created
            # note: url_for("blueprintName.functionName")
            return redirect(url_for("views.home"))

    return render_template("sign_up.html")