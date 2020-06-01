import mysql.connector as mariadb
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = mariadb.connect(
            user='root', 
            password='123456', 
            database='drivingschool'
        )
    return g.db


def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()
        

def init_db():
    db = get_db()
    cursor = db.cursor()

    with current_app.open_resource('db/schema.ddl.sql') as f:
        cursor.execute(f.read().decode('utf8'))