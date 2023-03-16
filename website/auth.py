# log-in page goes here because it relates to authentication
from flask import Blueprint, render_template, request, flash

# set up blueprint for flask application, same name as file not required, but standard
auth = Blueprint('auth', __name__)

# we will define the log-in, sign-up, and log-out in here
@auth.route('/login', methods = ["GET", "POST"])
def login():
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

        # checking if the info provided by user is valid
        if len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif password1 != password2:
            # if passwords don't match, flash a message to user
            flash("Passwords do not match.", category="error")
        elif len(password1) < 7:
            flash("Password must be longer than 6 characters.", category="error")
        else:
            flash("Account successfully created.", category="success")

    return render_template("sign_up.html")