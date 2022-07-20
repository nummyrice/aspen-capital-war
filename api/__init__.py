from flask import Flask
from flask_migrate import Migrate
from .models import db, Player
from .config import Config
from .routes import api_routes

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(api_routes, url_prefix='/')
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
