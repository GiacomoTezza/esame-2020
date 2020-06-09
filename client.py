from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from sys import stderr

from .db import get_db

bp = Blueprint('client', __name__)


@bp.route('/client/<client_id>', methods=('GET', 'POST'))
def index(client_id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        'SELECT ID, Name, Surname '
        'FROM Client '
        'WHERE ID = %s',
        (client_id, )
    )
    p_data = []
    for (c_id, name, surname) in cursor:
        p_data.append((c_id, name, surname))

    cursor.execute(
        'SELECT L.Name, R.StartDate, R.ExamStatus, R.ClientID, R.LicenseId '
        'FROM License AS L, Registration AS R '
        'WHERE R.ClientID = %s AND L.ID = R.LicenseID '
        'ORDER BY R.StartDate',
        (client_id,)
    )
    data = []
    for (license, date, status, cid, lid) in cursor:
        data.append((license, date, status, cid, lid))

    cursor.execute(
        'SELECT ID, Name '
        'FROM License'
    )
    l_data = []
    for (l_id, license) in cursor:
        l_data.append((l_id, license))

    isErrorOccurred = False
    if request.method == 'POST':
        license = request.form['license']
        isAllow = True

        if len(data) > 0:
            for registration in data:
                print(license)
                if registration[0] == license and registration[2] not in ('Bocciato Teoria', 'Bocciato Pratica'):
                    isAllow = False

        if isAllow:
            try:
                cursor.execute(
                    'INSERT INTO Registration (LicenseID, ClientID, StartDate, ExamStatus) '
                    'VALUES (%s, %s, CURRENT_DATE(), %s) ',
                    (license, client_id, "Non Fissato")
                )
                db.commit()
                return redirect('/subscribers')
            except:
                isErrorOccurred = True

    return render_template('client/index.html', p_data=p_data, data=data, data_len=len(data), l_data=l_data, isErrorOccurred=isErrorOccurred)
