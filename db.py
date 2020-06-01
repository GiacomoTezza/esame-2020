import mysql.connector as mariadb
import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = mariadb.connect(
            user='root', 
            password='123456', 
            database='drivingschool'
        )
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
        

def init_db():
    db = get_db()
    cursor = db.cursor()

    with current_app.open_resource('db/schema.ddl.sql') as f:
        cursor.execute(f.read().decode('utf8'), multi=True)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Database initialized.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)