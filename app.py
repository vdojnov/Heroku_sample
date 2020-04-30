import os
from flask import Flask
from models import setup_db
from flask_cors import CORS

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        return "First App on Heroku!"

    @app.route('/second')
    def be_cool():
        return "This is the second page on Heroku!"

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
