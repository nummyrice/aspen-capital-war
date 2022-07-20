from flask import Flask
from flask_migrate import Migrate
from .models import db, Player
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
Migrate(app, db)

'''
    todo:
    SQLALCHEMY_RECORD_QUERIES
        - configure ORM
        - initialize db
        - set environment variables
        - generate models and migrations
        - generate seed data
        - test database
        - create docker file
            - yml file?
        - create html page in jinja?
        - test in heroku or ocean

        notes:
            - remember to excape() user provided values rendered in the output when returning HTML
'''

@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/start-game', ['POST'])
def get_decks():

    '''
        when this route is reached:
            - add player1 and player2 names to the database
            - a deck for player_1 and player_2 are created and returned
    '''

    return "Game Ended"

@app.route('/all-time-record')
def get_records():
    '''
        when this route is reached:
            - the records for player_1 and player_2 are returned

    '''
    return "Record"
