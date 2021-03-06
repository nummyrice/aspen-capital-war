from flask import Flask
from flask_migrate import Migrate
from .models import db, Player
from .config import Config
from .routes import api_routes
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(api_routes, url_prefix='/')
db.init_app(app)
Migrate(app, db)
CORS(app)
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

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
