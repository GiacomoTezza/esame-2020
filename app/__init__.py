from flask import Flask, render_template
import random, string
from dotenv import load_dotenv

def create_app():
    """
    Function that loads the enviroments variables and
    registers the blueprints of the pages
    """
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

    # 404 error handler
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error/index.html', message="Error 404: Page not found")

    return app


app = create_app()