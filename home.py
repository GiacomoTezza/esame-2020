from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from .db import get_db

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'SELECT Name, Description '
        'FROM License'
        )

    data = []
    for (name, description) in cursor:
        data.append((name, description))
    
    return render_template('home/index.html', data=data)