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


def execute_file_db(file_path):
    db = get_db()
    cursor = db.cursor()

    with current_app.open_resource(file_path) as f:
        cursor.execute(f.read().decode('utf8'), multi=True)


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    execute_file_db('db/schema.ddl.sql')
    click.echo('Database initialized.')


@click.command('fill-db')
@with_appcontext
def fill_db_command():
    """Insert fake data, develop purpose."""
    execute_file_db('db/data.dump.sql')
    click.echo('Database filled.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(fill_db_command)