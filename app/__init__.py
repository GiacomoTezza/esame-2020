from flask import Flask
import random, string
from dotenv import load_dotenv

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.secret_key = "".join( random.choices(string.ascii_lowercase, k=15))

    from . import db
    db.init_app(app)

    from . import home
    app.register_blueprint(home.bp)
    app.add_url_rule('/', endpoint='index')

    from . import subscribers
    app.register_blueprint(subscribers.bp)

    from . import register
    app.register_blueprint(register.bp)

    from . import client
    app.register_blueprint(client.bp)

    from . import exam
    app.register_blueprint(exam.bp)

    return app


app = create_app()