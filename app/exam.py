from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from sys import stderr

from .db import get_db

bp = Blueprint('exam', __name__)


@bp.route('/exam', methods=('POST',))
def index():
    """
    Function called when the route in the decorator is visited
    """
    db = get_db()
    cursor = db.cursor()
    data = []
    id_data = []

    # Handling of the POST request operations
    if request.method == 'POST':
        licenseID = request.form['LicenseID']
        clientID = request.form['ClientID']
        date = request.form['StartDate']
        id_data = [licenseID, clientID, date]

        cursor.execute(
            'SELECT C.Name, C.Surname, L.Name, R.StartDate, R.ExamStatus '
            'FROM Client AS C, License AS L, Registration AS R '
            'WHERE R.LicenseID = %s AND R.ClientID = %s AND R.StartDate = %s '
            'AND R.ClientID = C.ID AND R.LicenseID = L.ID',
            (licenseID, clientID, date)
        )
        for (name, surname, license, date, status) in cursor:
            data.append((name, surname, license, date, status))

    s_data = ['Non Fissato', 'Fissato', 'Promosso Teoria',
              'Bocciato Teoria', 'Promosso Pratica', 'Bocciato Pratica']

    return render_template('exam/index.html', data=data, s_data=s_data, id_data=id_data)


@bp.route('/exam/update', methods=('POST',))
def update():
    """
    Function called when the route in the decorator is called with POST
    Route only for requests and handling of the update
    """
    db = get_db()
    cursor = db.cursor()
    
    if request.method == 'POST':
        status = request.form['status']
        licenseID = request.form['LicenseID']
        clientID = request.form['ClientID']
        date = request.form['StartDate']

        cursor.execute(
            'UPDATE Registration '
            'SET ExamStatus = %s '
            'WHERE LicenseID = %s AND ClientID = %s AND StartDate = %s',
            (status, licenseID, clientID, date)
        )
        db.commit()
        return redirect('/client/' + clientID)
    
    return redirect('/subscribers')