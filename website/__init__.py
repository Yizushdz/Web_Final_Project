# set up flask application
from flask import Flask
# to use database
from flask_sqlalchemy import SQLAlchemy
# used to tell flask how we actually log in a user
from flask_login import LoginManager
# to migrate database when needed
from flask_migrate import Migrate
# needed to properly upgrade database after migration, fixes naming convention
from sqlalchemy import MetaData
# to get names form file
import re

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)

# initialize new database, db is an object
db = SQLAlchemy(metadata=metadata)
DB_NAME = "database.db"


# function to read leetcode links and extract the name of problem
def extract_problem_names(file_path):
    problem_names = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(r'https://leetcode.com/problems/([^/]+)/', line)
            if match:
                name = match.group(1).title()
                problem_names.append(name)
    
    # for problem in problem_names:
    #     problem_names.append(problem.replace("-", " "))

    return problem_names

def create_app():
    # initialize the app
    app = Flask(__name__)
    # to secure/encrypt cookies data in our app
    app.config['SECRET_KEY'] = "This is the secret key, don't share with anyone." 
    # my sqlalchemy database is stored/located at: f"sqlite:///{DB_NAME}"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    # initialize database by giving it our flask app
    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)

    # telling flask we have Blueprints for some URLs & where they are. Dot == explicit relative import
    from .views import views
    from .auth import auth

    # to acually register the blueprints
    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    # this will make sure that our database classes are properly created before we actually create the databases
    from .models import User

    with app.app_context():
        db.create_all()

    # creating login class to manage having a user logged in
    login_manager = LoginManager()
    # where should we go if user is not logged in. = 'BlueprintName.funcName'
    login_manager.login_view = 'views.initial'
    # telling login manager which app we are refering to
    login_manager.init_app(app)

    # decorator to help us tell flask how we load a user
    @login_manager.user_loader
    # essentially telling flask what user we are looking for, reference them by their ID
    def load_user(id):
        return User.query.get(int(id))

    return app