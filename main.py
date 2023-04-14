# import the website package and grab the create_app function
from website import create_app

app = create_app()

# this will run program only when this specific program is ran, not when main.py is imported somewhere else
if __name__ == '__main__':
    # debug will update website everytime the python file is updated. should be off once it's deployed
    app.run(debug=True, port = 2000)