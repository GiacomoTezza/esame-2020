from flask import flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "".join( random.choices(string.ascii_lowercase, k=15))

    from . import db
    db.init_app(app)

    return app