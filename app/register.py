from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from .db import get_db

bp = Blueprint('register', __name__)


@bp.route('/register', methods=('GET', 'POST'))
def index():
    """
    Function called when the route in the decorator is visited
    """
    db = get_db()
    cursor = db.cursor()

    # Handling of the POST request operations
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        cf = request.form['cf']
        checkbox = request.form['gdpr']

        cursor.execute(
            'INSERT INTO Client (Name, Surname, CF)'
            'VALUES (%s, %s, %s)',
            (name, surname, cf)
        )
        db.commit()
        return redirect('/subscribers')

    return render_template('register/index.html')