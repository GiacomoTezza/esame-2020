from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from .db import get_db

bp = Blueprint('subscribers', __name__)


@bp.route('/subscribers')
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'SELECT C.Surname, C.Name, L.Name, R.ExamStatus, R.StartDate '
        'FROM Client AS C '
        'LEFT JOIN (License AS L, Registration AS R) ON (L.ID = R.LicenseID AND C.ID = R.ClientID)'
        )

    data = []
    for (name, surname, license, exam, date) in cursor:
        data.append((
            name, 
            surname, 
            license if license is not None else '-', 
            exam if exam is not None else '-', 
            date if date is not None else '-'
            ))

    return render_template('subscribers/index.html', data=data)
