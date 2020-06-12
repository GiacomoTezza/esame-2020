from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from .db import get_db

bp = Blueprint('subscribers', __name__)


@bp.route('/subscribers')
def index():
    """
    Function called when the route in the decorator is visited
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'SELECT C.ID, C.Surname, C.Name, L.Name, R.ExamStatus, R.StartDate '
        'FROM Client AS C '
        'LEFT JOIN (License AS L, Registration AS R) ON (L.ID = R.LicenseID AND C.ID = R.ClientID) '
        'ORDER BY C.Surname'
        )

    data = []
    for (id, name, surname, license, exam, date) in cursor:
        data.append((
            id,
            name, 
            surname, 
            license if license is not None else '-', 
            exam if exam is not None else '-', 
            date if date is not None else '-'
            ))

    return render_template('subscribers/index.html', data=data)
