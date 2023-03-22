# set up flask application
from flask import Flask
# to use database
from flask_sqlalchemy import SQLAlchemy
# needed to check if a path exists
from os import path
# used to tell flask how we actually log in a user
from flask_login import LoginManager

# initialize new database, db is an object
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    # initialize the app
    app = Flask(__name__)
    # to secure/encrypt cookies data in our app
    app.config['SECRET_KEY'] = "This is the secret key, don't share with anyone." 
    # my sqlalchemy database is stored/located at: f"sqlite:///{DB_NAME}"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    # initialize database by giving it our flask app
    db.init_app(app)

    # telling flask we have Blueprints for some URLs & where they are. Dot == explicit relative import
    from .views import views
    from .auth import auth

    # to acually register the blueprints
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    # this will make sure that our database classes are properly created before we actually create the databases
    from .models import User

    # calling function to create database if not exists
    # create_database(app)

    with app.app_context():
        db.create_all()

    # creating login class to manage having a user logged in
    login_manager = LoginManager()
    # where should we go if user is not logged in. = 'BlueprintName.funcName'
    login_manager.login_view = 'auth.login'
    # telling login manager which app we are refering to
    login_manager.init_app(app)

    # decorator to help us tell flask how we load a user
    @login_manager.user_loader
    # essentially telling flask what user we are looking for, reference them by their ID
    def load_user(id):
        return User.query.get(int(id))

    return app



# to create database, and check if database already exists, if not, create new one
# with app.app_context(): \n db.create_all()
'''NOT CUREENTLY USED, MODIFY'''
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app = app)
        print("Created Database")